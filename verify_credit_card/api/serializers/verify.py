# Utils
from verify_credit_card.utils.validate_card import validate_credit_Card, validate_type_credit_card

# Libreria restframework
from rest_framework import serializers


class CreditCardSerializer(serializers.Serializer):
    creditCard = serializers.CharField(max_length=19)
    typeCreditCard = serializers.CharField(required=False, max_length=250, read_only=True)

    def validate(self, attrs):
        response = validate_credit_Card(attrs['creditCard'])
        if response['status'] == 1:
            raise serializers.ValidationError({'message': response})
        response_type = validate_type_credit_card(response['numberCard'])
        attrs['typeCreditCard'] = response_type['type']
        return attrs
