from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
def employee_list(request):
    employee = Employee.objects.all()
    return render(request, 'employeeregister/employee_list.html', {'employee':employee})

def employee_form(request, id=0):
    if request.method == 'GET':
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance = employee)
        return render(request, 'employeeregister/employee_form.html', {'form':form})
    else:
        if id==0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
        return redirect('list')


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('list')
