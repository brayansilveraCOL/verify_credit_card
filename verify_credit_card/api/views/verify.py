# Import Serializers
from verify_credit_card.api.serializers.verify import CreditCardSerializer
# Librerias externas
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def api_view_verify_credit_card(request):
    if request:
        if request.data:
            if request.method == 'POST':
                verify_credit_card = CreditCardSerializer(data=request.data)
                verify_credit_card.is_valid(raise_exception=True)
                return Response(verify_credit_card.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
