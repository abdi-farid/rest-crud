from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from sampleCrudApi.models import Person
from sampleCrudApi.serializer import PersonSerializer


# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [AllowAny]
