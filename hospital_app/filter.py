import django_filters
from .models import Search_doctors
class Boking(django_filters.FilterSet):
    
    class Meta:
        model=Search_doctors
        fields=['name','specialization']