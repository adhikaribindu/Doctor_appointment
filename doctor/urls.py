from doctor.views import home,register,save_user,login_view,login
from django.urls import path

urlpatterns = [
    path('home',home,name='home'),
    path('register',register,name='register'),
    path('save',save_user,name="save_user"),
    path('login_view',login_view,name='login_view'),
    path('login',login,name='login'),
    # path('doctor_detail/<detailid>',doctor_detail,name='doctor_detail')
]
