from django import forms
from .models import Employee, Employment, Attendance, CashHandover
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class EmployeeForm(forms.ModelForm):
    working_hours = forms.FloatField()
    salary = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Employee
        fields = ['name', 'gender', 'profession', 'aadhar_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhar_number': forms.TextInput(attrs={'class': 'form-control'}),
            'working_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class EmploymentForm(forms.ModelForm):
    class Meta:
        model = Employment
        fields = ['employee', 'working_hours', 'salary']
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'working_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['date', 'present']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'present': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class CashHandoverForm(forms.ModelForm):
    class Meta:
        model = CashHandover
        fields = ['date', 'amount']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
