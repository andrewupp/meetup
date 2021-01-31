from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from map.views import MapViewSet
from accounts.views import AccountsViewSet


router = DefaultRouter() # 只需要实现一次
router.register(r'', MapViewSet, basename='accounts')
app_name = "accounts"
urlpatterns = [path("", include(router.urls)), ]