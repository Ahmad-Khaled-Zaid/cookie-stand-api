from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Marshmello
from .permissions import IsOwnerOrReadOnly
from .serializers import ThingSerializer


class MarshmelloList(ListCreateAPIView):
    queryset = Marshmello.objects.all()
    serializer_class = ThingSerializer


class MarshmelloDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Marshmello.objects.all()
    serializer_class = ThingSerializer
