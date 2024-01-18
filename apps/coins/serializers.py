from rest_framework import serializers

from apps.coins.models import Coin

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ('id','to_username', 'from_username', 'amount')

    def create(self, validated_data):
        user = validated_data.pop('user', None)

        coin = Coin.objects.create(**validated_data)
        # coin = Coin.objects.create(
        #     to_username=validated_data['to_username'],
        #     from_username=validated_data['from_username'],
        #     amount=validated_data['amount']
        # )
        if user:
            coin.user = user
            coin.save()
        return coin

