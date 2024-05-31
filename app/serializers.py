from .models import HydroponicSystem, Measurement
from rest_framework import serializers


class SimpleMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'ph', 'water_temp', 'tds', 'created_at']


class HydroponicSystemSerializer(serializers.ModelSerializer):
    last_10_measurements = SimpleMeasurementSerializer(
        many=True, read_only=True,
    )

    class Meta:
        model = HydroponicSystem
        fields = ['id', 'name', 'description',
                  'last_10_measurements', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class OwnerFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(OwnerFilteredPrimaryKeyRelatedField, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(owner=request.user)


class MeasurementSerializer(serializers.ModelSerializer):

    # only owned by the user
    hydroponic_system = OwnerFilteredPrimaryKeyRelatedField(
        queryset=HydroponicSystem.objects
    )

    class Meta:
        model = Measurement
        fields = '__all__'
