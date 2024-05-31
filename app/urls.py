from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'hydroponicsystem', views.HydroponicSystemViewSet, 'hydroponicsystem')
router.register(r'measurement', views.MeasurementViewSet, 'measurement')


urlpatterns = [
    path('', include(router.urls)),
]
