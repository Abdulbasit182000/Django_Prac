from rest_framework import serializers
from .models import Doctor, Nurse, Patient


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
        x= data['age']
        if x<18:
            raise serializers.ValidationError("Should be atleast 18")

        return data
