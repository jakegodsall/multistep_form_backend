from django.urls import path

from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('plan', views.Plan, basename='plan')
router.register('addon', views.Addon, basename='addon')

urlpatterns = router.urls
