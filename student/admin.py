from django.contrib import admin

# Register your models here.
from .models import Section, Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('registration_id', 'name', 'email_id', 'section')

admin.site.register(Section)
admin.site.register(Student, StudentAdmin)
