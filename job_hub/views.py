from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
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
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
