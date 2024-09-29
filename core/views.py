from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee, Employment, Attendance, CashHandover
from .forms import EmployeeForm, EmploymentForm, AttendanceForm, CashHandoverForm, UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def dashboard(request):
    employments = Employment.objects.filter(employer=request.user)
    return render(request, 'core/dashboard.html', {'employments': employments})


@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            Employment.objects.create(employee=employee, employer=request.user,
                                      working_hours=form.cleaned_data['working_hours'],
                                      salary=form.cleaned_data['salary']
                                      )
            return redirect('dashboard')
    else:
        form = EmployeeForm()
    return render(request, 'core/add_employee.html', {'form': form})


@login_required
def add_attendance(request, employment_id):
    employment = Employment.objects.get(id=employment_id)
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.employment = employment
            attendance.save()
            return redirect('dashboard')
    else:
        form = AttendanceForm()
    return render(request, 'core/add_attendance.html', {'form': form, 'employment': employment})


@login_required
def add_cash_handover(request, employment_id):
    employment = Employment.objects.get(id=employment_id)
    if request.method == 'POST':
        form = CashHandoverForm(request.POST)
        if form.is_valid():
            handover = form.save(commit=False)
            handover.employment = employment
            handover.save()
            return redirect('dashboard')
    else:
        form = CashHandoverForm()
    return render(request, 'core/add_cash_handover.html', {'form': form, 'employment': employment})


@login_required
def employee_details(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employments = Employment.objects.filter(employee=employee)

    attendance_records = Attendance.objects.filter(employment__employee=employee).order_by('-date')
    cash_handovers = CashHandover.objects.filter(employment__employee=employee).order_by('-date')

    context = {
        'employee': employee,
        'employments': employments,
        'attendance_records': attendance_records,
        'cash_handovers': cash_handovers,
    }
    return render(request, 'core/employee_details.html', context)
