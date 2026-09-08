from django.contrib import admin
from .models import Division, Employee, LearningCourse, PersonalInfo



@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('div_name', 'in_scope')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'division', 'priority')


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('employee', 'tel', 'address')

    
@admin.register(LearningCourse)
class LearningCourseAdmin(admin.ModelAdmin):
    filter_horizontal = ('employee',)
    list_display = (
        'title',
        'level',
       
    )