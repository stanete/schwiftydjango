from rest_framework import viewsets
from .models import Character, Origin
from .serializers import CharacterSerializer, OriginSerializer
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class OriginView(viewsets.ModelViewSet):
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer
    pagination_class = PageNumberPagination


class CharacterView(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    pagination_class = PageNumberPagination
