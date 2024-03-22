from django.shortcuts import render,redirect
from django.http import HttpResponse
from doctor.form import RegistrationForm,LoginForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login,authenticate
# from doctor.models import Doctor,DoctorDetail
User=get_user_model()
# Create your views here.


def home(request):
    return HttpResponse("This is a home page")

def register(request):
    form=RegistrationForm
    context={'form':form}
    return render(request,"register.html",context=context)

def save_user(request):
    if request.method=="POST":
        form=RegistrationForm(data=request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(form.cleaned_data)

        user=User.objects.create(
            username=data.get("username"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            email=data.get("email")
        )
        user.set_password(data.get("password"))
        user.save()

    return redirect('login_view')

def login_view(request):
    if request.method=="POST":
        form=LoginForm(data=request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(form.cleaned_data)

            user=authenticate(request, username=data.get('username'), password=data.ger('oassword'))
            login(request,user)
    return redirect('login')

def login(request):
    form=LoginForm
    context={'form':form}
    return render(request,'login.html',context=context)


def logout(request):
    pass


# def doctor_detail(request,detailid):
#     doctor_id=request.GET.get('doctor_id')
#     if doctor_id:
#         doctor=Doctor.objects.get(id=doctor_id)
#         doctor_detail=DoctorDetail.objects.filter(doctor=doctor)
#     else:
#         doctor=None
#         doctor_detail=None    
#     return render(request,'details.html',{'doctor':doctor,'doctor_detail':doctor_detail})