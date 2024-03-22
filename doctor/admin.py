from django.contrib import admin
from doctor.models import Doctor,DoctorDetail,DoctorAvailableDate
# Register your models here.

admin.site.register(Doctor)
admin.site.register(DoctorDetail)
admin.site.register(DoctorAvailableDate)

