from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.

def home(request):
    return render(request,'home.html')

def emp(request):
    if request.method == 'POST':
        Emp_name = request.POST['Emp_name']
        Emp_age = request.POST['Emp_age']
        Salary = request.POST['Salary']

        eid = Emp.objects.create(Emp_name=Emp_name,Emp_age=Emp_age,Salary=Salary)
        eid.save()

    return render(request,'emp.html')

def emp_record(request):
    aid = Emp.objects.all()

    Ts = 0
    for i in aid:
        Ts = Ts + i.Salary

    print(Ts)
    context = {
        'aid': aid,
        'Ts' : Ts
    }
    return render(request,'emp_record.html',context)

def update(request,id):
    if request.method == 'POST':
        Emp_name = request.POST['Emp_name']
        Emp_age = request.POST['Emp_age']
        Salary = request.POST['Salary']

        uid = Emp.objects.get(id=id)

        uid.Emp_name = Emp_name
        uid.Emp_age = Emp_age
        uid.Salary = Salary

        uid.save()

    return redirect('emp_record')

def Delete(request,id):

    uid = Emp.objects.get(id=id)

    uid.delete()

    return redirect('emp_record')