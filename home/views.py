from django.shortcuts import render,redirect
from .forms import student,admin
from .models import Amodel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.
def add(request): 
    if request.method=="POST":
        fm =student(request.POST)
        if fm.is_valid():
            fm.save()
        fm = student()
        stu=Amodel.objects.all()

    else:
        fm = student()
        stu=Amodel.objects.all()
    return render(request,'add.html',{'fm':fm,'stu':stu})

# def view(request):
#     stu=Amodel.objects.all()
#     return render(request,'add.html',{'fm':fm,'stu':stu})


def delete(request,id):
    stu=Amodel.objects.get(id=id)
    stu.delete()
    return redirect("add")
    
    
    
def edit(request,id):
    # stu=Amodel.objects.get(id=id)
    # return redirect("add")
    if request.method=="POST":
        fm =student(request.POST)
        if fm.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            Amodel.objects.filter(id=id).update(name=name,email=email,password=password)
            
        fm = student()
        stu=Amodel.objects.all()
        return redirect("add")
    else:
        vl = Amodel.objects.get(id=id)
        fm = student(instance=vl)
        stu=Amodel.objects.all()
    return render(request,'add.html',{'fm':fm,'stu':stu})



def login(request):
    form = admin( None or request.POST)
    if request.method == 'POST':
            name = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username = name,password = password)
            #print(user)
            if user is not None:
                if user.is_active:
                    return redirect('add')
    return render(request,'login.html',{'form':form})



def logout(request):
    return redirect(request,"userlogin")



def register(request):
    form = student(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('userlogin')
    return render(request,'register.html',{'form':form})



def home(request):
    return render(request,'home.html')


def userlogin(request):
    form = student(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            try:
                user = Amodel.objects.get(name=name)
            except :
                pass
            else:
                if user is not None:
                    if user.password == password and user.email == email:
                        return redirect("home")
    return render(request,'userlogin.html',{'form':form})

