from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'available_riders', ListRidersViewSet, basename="available_riders")
find_customers_router = DefaultRouter()
find_customers_router.register(r'find_customers', FindCustomersViewSet, basename="find_customers")

urlpatterns = [
    path('', include(router.urls)),
    path('', include(find_customers_router.urls)),
]
