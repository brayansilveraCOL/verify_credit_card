from rest_framework import serializers


class CreditCardSerializer(serializers.Serializer):
    creditCard = serializers.CharField(max_length=19)

    def validate(self, attrs):
        print(attrs['creditCard'])
        return attrs
