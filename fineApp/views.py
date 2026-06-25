from django.shortcuts import render,redirect
from fineApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

# authenticate section

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        con_password = request.POST.get('con_password')

        if password != con_password:
            messages.warning(request,'Invalid Password')
            return redirect('register_view')

        user_exist = UserModel.objects.filter(username= username).exists()
        if user_exist:
            messages.warning(request,'User Already exist!!')
            return redirect('register_view')

        UserModel.objects.create_user(
            username = username,
            email = email,
            password = password,
        )

        return redirect('login_view')
    
    return render(request,'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username , password = password)
        if user :
            login(request,user)
            messages.success(request,'Login successsfully!!')
            return redirect('homepage_view')
        
        else:
            messages.warning(request,'Invalid login information')
            return redirect('login_view')
        
    return render(request,'login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request,'Successfully Logout')
    return redirect('login_view')

@login_required
def homepage_view(request):
    return render(request,'HomePage.html')


# student page infooo

def student_show(request):
    stu_info = studentModel.objects.all()

    context = {
        'stu_info' : stu_info
    }
    return render(request,"studentShow.html", context)

def student_add(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        image = request.FILES.get('image')

        studentModel.objects.create(
            name = name,
            phone = phone,
            image = image,
        )

        return redirect('student_show')
    return render(request,"studentAdd.html")


def student_update(request,id):
    stu_data = studentModel.objects.get(id = id)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        image = request.FILES.get('image')

        stu_data.name = name
        stu_data.phone = phone
        if image:
            stu_data.image = image

        stu_data.save()

        return redirect('student_show')

    context = {
        'stu_data' : stu_data
    }    
    return render(request,"studentUpdate.html",context)

def student_delete(request,id):
    studentModel.objects.get(id = id).delete()
    return redirect('student_show')


