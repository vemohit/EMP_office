from http.client import HTTPResponse
from re import template
from xml.dom.minicompat import EmptyNodeList
from .models import Employee, Role, Department
from django.shortcuts import render

# Create your views here.
def index(requeset):
    return render(requeset,'index.html')

def all_emp(requeset):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(requeset,'all_emp.html',context)

def add_emp(requeset):
    return render(requeset,'add_emp.html')

def remove_emp(requeset):
    return render(requeset,'remove_emp.html')

def filter_emp(requeset):
    return render(requeset,'filter_emp.html')