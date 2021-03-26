from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import UserTokenSerializer
from django.contrib.auth import get_user_model, authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from authentication.models import SpTnstate,Districts,Blocks
from django.core.serializers import serialize

# Create your views here.
class UserLogin(APIView):
    """return user token if user credetials are correct"""
    serializer_class = UserTokenSerializer

    def get(self, request, format=None):
        """user sign in form"""
        serializer = UserTokenSerializer()
        return Response(status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """post user request"""
        serializer = UserTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.data.get('username'),
                password=serializer.data.get('password'))
            if user is not None:
                token, create_or_fetch = Token.objects.get_or_create(
                    user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            msg = 'Wrong credentials. Please try again'
            return Response({'message': msg}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TnState(APIView):
    def get(self, request, format=None):
        data = serialize('geojson', SpTnstate.objects.all(),geometry_field='geom',fields=('state_name',))
        return Response({'tn_state': data}, status=status.HTTP_200_OK)

class TnDistrict(APIView):
    def get(self, request, format=None):
        data = serialize('geojson', Districts.objects.all(),geometry_field='geom',fields=('gid','district',))
        return Response({'tn_district': data}, status=status.HTTP_200_OK)

class TnBlock(APIView):
    def get(self, request, format=None):
        data = serialize('geojson', Blocks.objects.all(),geometry_field='geom',fields=('gid','district','blkname'))
        return Response({'tn_blocks': data}, status=status.HTTP_200_OK)
        