from django.contrib import admin
from .models import Module
from .models import Course
from .models import Lecture

# Register your models here.

admin.site.register(Lecture)
admin.site.register(Module)
admin.site.register(Course)
