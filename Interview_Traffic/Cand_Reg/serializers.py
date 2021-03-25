from rest_framework import serializers
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id','name','registration_type','email_id','available_start_date','available_end_date')

class FreeSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id','available_start_date','available_end_date')


        
