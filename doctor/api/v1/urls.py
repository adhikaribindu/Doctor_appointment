from doctor.api.v1.views import DoctorList,DoctorDetailAPIView,DoctorSave
from django.urls import path

urlpatterns = [
    path('test/',DoctorList.as_view(),name='list-api-view'),
    path('doctor_detail/<pk>/',DoctorDetailAPIView.as_view(),name='detail-api-view'),
    path('doctor_save/',DoctorSave.as_view(),name="detail_save_view")
    
]

