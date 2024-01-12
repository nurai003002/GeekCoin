from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from apps.users.models import Users
from apps.users.serializers import UsersSerializers
# Create your views here.

class UsersAPI(ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers

class UsersAPICreate(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers

class UsersAPIRetrieve(RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers

class UsersAPIUpdate(UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers


class UsersAPIDestroy(DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers