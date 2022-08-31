from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Employee


def emp_list(request):
    employees = Employee.objects.filter().all()
    return render(request, 'employees/emp_list.html', {'employees': employees})


def view_emp(request, emp_id):
    employees = Employee.objects.get(emp_id=emp_id)
    return HttpResponseRedirect(reverse('index'))


def emp_details(request, id):
    # employees = Employee.objects.filter().all()
    return render(request, 'employees/emp_details.html')


def emp_add(request):
    return render(request, 'employees/emp_add.html')


from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from .serializers import EmpListSerializer


class EmpListApi(ListAPIView):
    permission_classes = []

    def get(self, request):
        emp_id = request.GET.get('emp_id')
        first_name = request.GET.get('first_name')
        emp_data_list = Employee.objects.filter().all()
        if emp_id:
            emp_data_list = emp_data_list.filter(emp_id__icontains=emp_id).all()
        if first_name:
            emp_data_list = emp_data_list.filter(first_name__icontains=first_name).all()

        emp_data_list = EmpListSerializer(emp_data_list, many=True).data
        return Response(emp_data_list)


from rest_framework.utils import json


class EmpAddApi(CreateAPIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        try:
            data_value = json.loads(request.body)
            employee = Employee()
            if 'emp_id' not in data_value or data_value['emp_id'] == '':
                return Response("Please Provide Your ID")
            employee.emp_id = data_value['emp_id']
            employee.first_name = data_value['first_name']
            employee.last_name = data_value['last_name']
            employee.gender = data_value['gender']
            employee.designation = data_value['designation']
            employee.phone = data_value['phone']
            employee.email = data_value['email']
            employee.birth_date = data_value['birth_date']
            employee.blood_group = data_value['blood_group']
            employee.district = data_value['district']
            employee.save()
            return Response("Success")

        except Exception as ex:
            return Response({"Massage": str(ex)}, status=400)


class EmpEditApi(CreateAPIView):
    permission_classes = []

    def put(self, request, *args, **kwargs):
        try:
            data_value = json.loads(request.body)
            employee = Employee.objects.filter(id=self.kwargs['id']).first()
            if employee:
                employee.first_name = data_value['first_name']
                employee.last_name = data_value['last_name']
                employee.gender = data_value['gender']
                employee.designation = data_value['designation']
                employee.phone = data_value['phone']
                employee.email = data_value['email']
                employee.birth_date = data_value['birth_date']
                employee.blood_group = data_value['blood_group']
                employee.district = data_value['district']
                employee.save()
                return Response("Success")
            else:
                return Response('Employee Not In Database')

        except Exception as ex:
            return Response({"Massage": str(ex)}, status=400)


class EmpDetailsApi(ListAPIView):
    permission_classes = []

    def get(self, request, id):
        emp_id = request.GET.get('emp_id')
        first_name = request.GET.get('first_name')
        emp_data_list = Employee.objects.filter(id=id).first()

        if emp_id:
            emp_data_list = emp_data_list.filter(emp_id__icontains=emp_id).all()
        if first_name:
            emp_data_list = emp_data_list.filter(first_name__icontains=first_name).all()

        emp_data_list = EmpListSerializer(emp_data_list).data
        return Response(emp_data_list)