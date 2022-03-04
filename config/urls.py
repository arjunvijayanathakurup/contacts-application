from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from contact.views import ContactViewSet
from user.views import TokenObtainPairViewSet

router = DefaultRouter()
router.register('contacts', ContactViewSet, basename='contacts')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/', include(router.urls), name='api-root'),
    path('api/token/', TokenObtainPairViewSet.as_view(), name='token_obtain'),
]
