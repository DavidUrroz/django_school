from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash = False)

urlpatterns = [
    
]

urlpatterns += router.urls