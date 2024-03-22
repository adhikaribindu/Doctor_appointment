from rest_framework.response import Response
from rest_framework.views import APIView
from doctor.models import Doctor,DoctorDetail,DoctorAvailableDate
from .serializer import DoctorSerializers,DoctorDetailSerializers,DoctorAvailableDateSerializers,DoctorSaveSerializer
from django.contrib.auth import get_user_model

User=get_user_model()

class DoctorList(APIView):
    def get(self,request,*args,**kwargs):
        queryset=Doctor.objects.all()
        serializers=DoctorSerializers(queryset,many=True)
        return Response(serializers.data)
    
class DoctorDetailAPIView(APIView):
    def get(self,request,*args,**kwargs):
        doctor=DoctorDetail.objects.get(id=kwargs.get("pk"))
        queryset=DoctorAvailableDate.objects.filter(doctor_id_id=kwargs.get("pk"))
        available_date_serializer=DoctorAvailableDateSerializers(queryset,many=True)
        serializers=DoctorDetailSerializers(doctor)
        response = {
            "detail": serializers.data,
            "available_date": available_date_serializer.data
        }
        return Response(response)

class DoctorSave(APIView):
    def post(self,request,*args,**kwargs):
        doctor=DoctorDetail.objects.get(id=kwargs.post)
        queryset=DoctorAvailableDate.objects.filter(doctor_id_id=kwargs.post)
        available_date_serializer=DoctorAvailableDateSerializers(queryset,many=True)
        serializers=DoctorDetailSerializers(doctor)
        response = {
            "detail": serializers.data,
            "available_date": available_date_serializer.data
        }
        return Response(response)
    
class DoctorSaveAPI(APIView):
    def post(self,request,*args,**kwargs):
        serializers=DoctorSaveSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

    


    