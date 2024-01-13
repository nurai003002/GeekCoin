from rest_framework import serializers

from apps.transactions.models import Transactions

class TransactionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'
        