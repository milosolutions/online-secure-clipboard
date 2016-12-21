# -*- coding: utf-8 -*-
from rest_framework import viewsets, mixins

from .serializers import EncryptedPasteSerializer

from pastes.models import EncryptedPaste


class EncryptedPasteViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = EncryptedPasteSerializer
    queryset = EncryptedPaste.objects.all()
