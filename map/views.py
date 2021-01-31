from django.http import HttpResponse
from django.http import JsonResponse
from map.models import MapUser
import json
from rest_framework import  viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from django.core import serializers
from map.serializer import UserSerializer


class MapViewSet(viewsets.GenericViewSet):
    # permission_classes = (IsAuthenticated,)

    @action(methods=['post'], detail=False, url_path='update')
    def update_location(self,request):
        if request.method == 'POST':
            try:

                json_data = json.loads(request.body.decode())
                lat = json_data['lat']
                long = json_data['long']
                user_id = json_data['user_id']
                # max_lat = json_data['up_right'][0]
                # max_long = json_data['up_right'][1]
                # min_lat = json_data['down_left'][0]
                # min_long = json_data['down_left'][1]

                max_lat = json_data['lat'] + json_data['lat_distance']
                max_long = json_data['long'] + json_data['long_distance']
                min_lat = json_data['lat'] - json_data['lat_distance']
                min_long = json_data['long'] - json_data['long_distance']

                user = MapUser.objects.filter(user_id=user_id)
                neighbors = MapUser.objects.filter(long__gte=min_long, long__lte=max_long, lat__gte=min_lat,
                                                lat__lte=max_lat)
                user.update(long=long, lat=lat)
                # serializer = UserSerializer(neighbors, many=True)
                # print("1",serializer.data)

                return_dict = {'neighbors': []}

                for index, item in enumerate(neighbors):
                    return_dict['neighbors'].append({
                        "user_id": neighbors[index].user_id,
                        "lat": neighbors[index].lat,
                        "long": neighbors[index].long,
                        "last_update": neighbors[index].last_updated
                    })
                print(return_dict)


            except json.JSONDecodeError as e:
                HttpResponse("json error")

        else:
            HttpResponse("method should be post")
        return JsonResponse(return_dict)


