from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from apps.transactions.models import Transactions
from apps.transactions.serializers import TransactionsSerializers

# Create your views here.
class TransactionsAPI(ListAPIView):
        queryset = Transactions.objects.all()
        serializer_class = TransactionsSerializers

class TransactionsAPICreate(CreateAPIView):
        queryset = Transactions.objects.all()
        serializer_class = TransactionsSerializers


class TransactionsAPIRetrieve(RetrieveAPIView):
        queryset = Transactions.objects.all()
        serializer_class = TransactionsSerializers

class TransactionsAPIUpdate(UpdateAPIView):
        queryset = Transactions.objects.all()
        serializer_class = TransactionsSerializers

class TransactionsAPIDestroy(DestroyAPIView):
        queryset = Transactions.objects.all()
        serializer_class = TransactionsSerializers

