# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from .views import EncryptedPasteViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'pastes', EncryptedPasteViewSet, base_name='pastes')

urlpatterns = [
    url(r'^', include(router.urls)),
]
