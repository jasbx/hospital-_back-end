from django.contrib import admin
from.models import *
# Register your models here.
class Show(admin.ModelAdmin):
    
    list_display=['name1','number','doctor','age','gender','data']
    list_display_links=['number','doctor','age','gender','data']
    
    search_fields=['number','doctor','age','gender','data']
    list_filter=['number','doctor','age','gender','data']
from .models import LOGIN
admin.site.register(LOGIN,Show)

admin.site.site_header='Hospital manage system'
admin.site.site_title='Hospital system'

admin.site.site_url='name'

admin.site.register(Search_doctors)