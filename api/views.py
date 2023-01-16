from rest_framework import viewsets

from api.models import *
from api.serializers import *

# Create your views here.


class Plan(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class Addon(viewsets.ModelViewSet):
    querset = Addon.objects.all()
    serializer_class = AddonSerializer
