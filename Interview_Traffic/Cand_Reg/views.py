from django.shortcuts import render
from rest_framework import viewsets
from .models import UserModel
from .serializers import UserSerializer,FreeSlotsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
import django_filters
from django.http import JsonResponse
import json
import datetime


class UserView(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class AvailableSlotsView(APIView):
    
    def get(self,request):
        user_id_new = self.request.query_params.get("userId")
        inter_id_new = self.request.query_params.get("interId")

        user_details = UserModel.objects.filter(id=user_id_new)
        freeslot_serializers1 = FreeSlotsSerializer(user_details, many=True)
        
        user_start = freeslot_serializers1.data[0]['available_start_date']
        user_stop = freeslot_serializers1.data[0]['available_end_date']
        start_u = datetime.datetime.strptime(user_start, '%Y-%m-%dT%H:%M:%SZ')
        stop_u = datetime.datetime.strptime(user_stop, '%Y-%m-%dT%H:%M:%SZ')

        interviewer_details = UserModel.objects.filter(id=inter_id_new)
        freeslots_serializers2 = FreeSlotsSerializer(interviewer_details, many=True)
        interviewer_start = freeslots_serializers2.data[0]['available_start_date']
        interviewer_stop = freeslots_serializers2.data[0]['available_end_date']
        start_i = datetime.datetime.strptime(interviewer_start, '%Y-%m-%dT%H:%M:%SZ')
        stop_i = datetime.datetime.strptime(interviewer_stop, '%Y-%m-%dT%H:%M:%SZ')


        if start_i <= stop_u:
            if start_i <= start_u and stop_i <= stop_u:
                start_time = start_u

            else:
                start_time = start_i


            if start_i >= start_u and stop_i >= stop_u:
                stop_time = stop_u
            else:
                stop_time = stop_i
        else:
            return Response('Unable to find free slots')

        hours = []
        mystring = []

        starttime = start_time.time().isoformat()
        stoptime = stop_time.time().isoformat()

        slot_time = datetime.timedelta(hours=1)

        date = start_time.date()
        if date == stop_time.date():
            time = datetime.datetime.strptime(starttime, '%H:%M:%S')
            end = datetime.datetime.strptime(stoptime, '%H:%M:%S')

            while time < end:
                hours.append(time.strftime("%H:%M:%S"))
                mystring.append(
                    "{:%H:%M:%S} - {:%H:%M:%S}".format(time, time+slot_time))
                time += datetime.timedelta(hours=1)
        else:
            return Response('No slots Available')
        return Response(mystring)
