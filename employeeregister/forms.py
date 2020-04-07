from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = ('name', 'mobile', 'emp_code', 'position')
        labels = {
            'name' : "Full Name",
            'emp-code' : "Employee Code"
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "-- select --"
        self.fields['emp_code'].required = False
