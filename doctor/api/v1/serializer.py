from rest_framework import serializers
from doctor.models import Doctor,DoctorDetail,DoctorAvailableDate
from django.contrib.auth import get_user_model

User=get_user_model()


class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=(
            'doctor_name',
            'contact',
            'address',
            'specification',
            'qualification',
            'available_date',
            'checkin_time',
            'checkout_time'
        )

class DoctorDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model=DoctorDetail
        fields=(
            'doctor_id',
            'appointment_fees',
            'average_rating',
            'experienced_years'
        )

class DoctorAvailableDateSerializers(serializers.ModelSerializer):
    class Meta:
        model=DoctorAvailableDate
        fields=(
            'doctor_id',
            'available_day',
            'availabletime_slot'
        )

class DoctorSaveSerializers(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=(
            'doctor_name',
            'contact',
            'address',
            'specification',
            'qualification',
            'available_date',
            'checkin_time',
            'checkout_time'
        )