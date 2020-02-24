from django.contrib.auth.models import User
from .models import Classroom
from rest_framework import serializers

class Register(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']
    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class List(serializers.ModelSerializer):
    class Meta:
        model= Classroom
        fields= ['subject','name','year','teacher']

class Detail(serializers.ModelSerializer):
    class Meta:
        model= Classroom
        fields= ['subject','name','year','teacher']

class Create(serializers.ModelSerializer):
    class Meta:
        model=Classroom
        fields= ['subject','name','year','teacher']

class Update(serializers.ModelSerializer):
    class Meta:
        model=Classroom
        fields= ['subject','name','year',]
