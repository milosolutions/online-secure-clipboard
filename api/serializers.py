# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer

from pastes.models import EncryptedPaste


class EncryptedPasteSerializer(ModelSerializer):

    class Meta:
        model = EncryptedPaste
        fields = '__all__'
