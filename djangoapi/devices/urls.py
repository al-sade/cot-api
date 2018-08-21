from django.urls import path
from . import views

urlpatterns = [
    path('device/create/', views.DeviceCreate.as_view()),
    path('device/update/<int:pk>/', views.DeviceUpdate.as_view()),
    path('device/delete/<int:pk>/', views.DeviceDelete.as_view()),
    path('device/', views.DeviceList.as_view()),
    path('device/<int:pk>/', views.DeviceDetail.as_view()),

    path('property/create/', views.PropertyCreate.as_view()),
    path('property/update/<int:pk>/', views.PropertyUpdate.as_view()),
    path('property/delete/<int:pk>/', views.PropertyDelete.as_view()),
    path('property/', views.PropertyList.as_view()),
    path('property/<int:pk>/', views.PropertyDetail.as_view()),
]