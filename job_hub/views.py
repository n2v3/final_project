from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.response import Response

from .serializers import RegistrationSerializer


@swagger_auto_schema(
    methods=['post'],
    request_body=RegistrationSerializer,
    responses={200: "OK"},
)
@api_view(["POST"])
@permission_classes([])
@authentication_classes([])
def registration_view(request):
    registration_data = request.data

    serializer = RegistrationSerializer(data=registration_data)

    if serializer.is_valid():
        user = serializer.save()
        # Generate a token for the registered user
        token, created = Token.objects.get_or_create(user=user)
        message = {
            'detail': 'You successfully registered',
            'Save your token': token.key
        }

        return Response(message, status=status.HTTP_201_CREATED)
