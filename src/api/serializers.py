from rest_framework import serializers

from .models import ListAll


class ListAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListAll
        fields = '__all__'


class ListWithoutDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListAll
        fields = 'Stage_user', 'Foiv', 'Document_type', 'Document_number', 'Stage_name'
