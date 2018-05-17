from .models import Employee
import django_filters

class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model =Employee
        fields = ['first_name','last_name','age',]