from rest_framework import serializers
from .models import Doctor, Nurse, Patient
from django.contrib.auth.models import User


class RegisterSerizlizer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username= data['username']).exists():
                raise serializers.ValidationError('username is taken')

        if data['email']:
            if User.objects.filter(email= data['email']).exists():
                raise serializers.ValidationError('email is taken') 
        
        return data
    def create(self, validated_data):
        user = User.objects.create(username= validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Doctor
        fields = "__all__"  # for all fields, if you want specific use fields=['name','x','y']
        depth = 1

    def validate(self, data):
        if "+" in data["contact_number"]:
            raise serializers.ValidationError("nuber should not have + sign")

        return data


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = "__all__"  # for all fields, if you want specific use fields=['name','x','y']
        depth = 1

    def validate(self, data):
        if "+" in data["contact_number"]:
            raise serializers.ValidationError("nuber should not have + sign")

        return data


class PatientSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(many=True, required=False)
    nurse = NurseSerializer(required=False)

    class Meta:
        model = Patient
        fields = [
            "name",
            "doctor",
            "nurse",
            "age",
        ]  # for all fields, if you want specific use fields=['name','x','y']
        # depth = 1

    def validate(self, data):
<<<<<<< HEAD
<<<<<<< HEAD
        x = data["age"]
        if x < 18:
=======
        x= data['age']
        if x<18:
>>>>>>> 5c4e8d6 (Rest FRamework started)
=======
        x = data["age"]
        if x < 18:
>>>>>>> 5dc18be (Rest FRamework more work)
            raise serializers.ValidationError("Should be atleast 18")

        return data
