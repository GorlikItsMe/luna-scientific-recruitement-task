from rest_framework import viewsets
from .models import HydroponicSystem, Measurement
from .serializers import HydroponicSystemSerializer, MeasurementSerializer


class HydroponicSystemViewSet(viewsets.ModelViewSet):
    serializer_class = HydroponicSystemSerializer

    def get_queryset(self):
        return HydroponicSystem.objects.filter(owner=self.request.user)

    def perform_create(self, serializer: HydroponicSystemSerializer):
        return serializer.save(owner=self.request.user)


class MeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurementSerializer

    def get_queryset(self):
        return Measurement.objects.filter(hydroponic_system__owner=self.request.user)
