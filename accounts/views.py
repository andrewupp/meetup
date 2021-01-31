from django.http import HttpResponse
from django.http import JsonResponse
from accounts.models import Users
import json
from rest_framework import  viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import action

from django.core import serializers
from map.serializer import UserSerializer


class AccountsViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)

    @action(methods=['post'], detail=False, url_path='register')
    def update_location(self,request):
        if request.method == 'POST':
            try:




                user = Users.objects.filter(user_id=user_id)





            except json.JSONDecodeError as e:
                HttpResponse("json data error")

        else:
            HttpResponse("method should be post")
        return JsonResponse('ok')



