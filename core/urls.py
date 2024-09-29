from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('add_attendance/<int:employment_id>/', views.add_attendance, name='add_attendance'),
    path('add_cash_handover/<int:employment_id>/', views.add_cash_handover, name='add_cash_handover'),
    path('employee/<int:employee_id>/', views.employee_details, name='employee_details'),
]
