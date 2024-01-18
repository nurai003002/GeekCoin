from rest_framework import serializers
from apps.transactions.models import Transactions

class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transactions
        fields = ('id', 'from_user', 'to_user', 'is_complated', 'create_at', 'amount')

    def create(self, validated_data):
        # Extract 'user' from validated_data
        user = validated_data.pop('user', None)

        # Create the Transactions instance without the 'user' field
        transaction = Transactions.objects.create(**validated_data)

        # If 'user' is provided, set it separately
        if user:
            transaction.user = user
            transaction.save()

        return transaction
