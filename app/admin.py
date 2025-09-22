from django.contrib import admin
from .models import Department, Teacher, Program, Discipline, HomePageText

admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Program)
admin.site.register(Discipline)
admin.site.register(HomePageText)
