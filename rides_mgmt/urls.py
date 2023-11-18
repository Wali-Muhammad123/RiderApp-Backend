from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'', ListRidersViewSet, basename="available_riders")
find_customers_router = DefaultRouter()
find_customers_router.register(r'', FindCustomersViewSet, basename="find_customers")

urlpatterns = [
    path('available_riders/', include(router.urls)),
    path('find_customers/', include(find_customers_router.urls)),
]
