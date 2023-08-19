"""
URL mapping for the user API.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
