from core.models import Atleta, Treino, Modalidade
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password, check_password


class AtletaSerializer(ModelSerializer):
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super(AtletaSerializer, self).create(validated_data)

    class Meta:
        model = Atleta
        fields = "__all__"


class TreinoSerializer(ModelSerializer):
    class Meta:
        model = Treino
        fields = "__all__"


class ModalidadeSerializer(ModelSerializer):
    class Meta:
        model = Modalidade
        fields = "__all__"
