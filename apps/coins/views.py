from rest_framework.generics import  ListAPIView, CreateAPIView
from apps.coins.models import Coin
from apps.coins.serializers import CoinSerializer
# Create your views here.

class CoinAPI(ListAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer

class CoinCreate(CreateAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
