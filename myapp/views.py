from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.db.models import Q

def welcome(request):
    return render(request, "welcome.html")

def load_form(request):
    form = EmployeeForm
    return render(request, "index.html", {'form': form})

def add(request):
    form = EmployeeForm(request.POST)
    form.save()
    return redirect('/show')

def show(request):
    search = request.GET.get('name')
    employee = Employee.objects.all()
    employee = employee.filter(Q(ename__icontains=search)) if search else employee
    return render(request, "show.html", {'employee': employee})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, "edit.html", {'employee': employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    form.save()
    return redirect('/show')

def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')


def search(request):
    search = request.GET.get("search")
    print(search)
    employee = Employee.objects.filter(ename_icontains=search)
    return render(request, "show.html", {'employee': employee})
