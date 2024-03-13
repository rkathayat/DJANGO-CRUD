from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  # fields to display in list view
    search_fields = ('name', 'email')  # fields to search in list view
    list_filter = ('age',)  # fields to filter in list viewadmin.site.register(Student, StudentAdmin)from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'address', 'gender')
    search_fields = ('name', 'email', 'address')
    list_filter = ('age', 'gender')

admin.site.register(Student, StudentAdmin)

