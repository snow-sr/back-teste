from rest_framework.viewsets import ModelViewSet
from core.models import Atleta, Treino, Modalidade
from core import serializer
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, User):
        token = super().get_token(User)

        # Add custom claims
        token["id"] = User.id
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class AtletaViewSet(ModelViewSet):
    queryset = Atleta.objects.all()
    serializer_class = serializer.AtletaSerializer


class TreinoViewSet(ModelViewSet):
    queryset = Treino.objects.all()
    serializer_class = serializer.TreinoSerializer


class ModalidadeViewSet(ModelViewSet):
    queryset = Modalidade.objects.all()
    serializer_class = serializer.ModalidadeSerializer
