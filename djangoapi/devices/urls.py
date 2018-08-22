from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'device', views.DeviceViewSet, base_name='device')
router.register(r'property', views.PropertyViewSet, base_name='property')
urlpatterns = router.urls
