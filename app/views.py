from rest_framework import viewsets
from .models import HydroponicSystem, Measurement
from .serializers import HydroponicSystemSerializer, MeasurementSerializer
from rest_framework import filters


class HydroponicSystemViewSet(viewsets.ModelViewSet):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = '__all__'

    def get_queryset(self):
        return HydroponicSystem.objects.filter(owner=self.request.user)

    def perform_create(self, serializer: HydroponicSystemSerializer):
        return serializer.save(owner=self.request.user)


class MeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurementSerializer
    filterset_fields = ['hydroponic_system']

    def get_queryset(self):
        return Measurement.objects.filter(hydroponic_system__owner=self.request.user)
