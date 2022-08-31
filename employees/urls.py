from django.urls import path, include
from .views import emp_list, view_emp, emp_add, emp_details, EmpListApi, EmpAddApi, EmpEditApi, EmpDetailsApi

urlpatterns = [
    path('list_emp', emp_list),
    path('view_emp/<int:emp_id>', view_emp),
    path('details_emp/<str:id>/', emp_details),
    path('add_emp', emp_add),
    #api
    path('list_emp_api/', EmpListApi.as_view()),
    path('add_emp_api/', EmpAddApi.as_view()),
    path('edit_emp_api/', EmpEditApi.as_view()),
    path('details_emp_api/<str:id>/', EmpDetailsApi.as_view()),

]
