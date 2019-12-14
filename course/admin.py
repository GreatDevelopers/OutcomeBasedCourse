from django.contrib import admin
from .models import Module
from .models import Course
from .models import Unit

# Register your models here.

admin.site.register(Unit)
admin.site.register(Module)
admin.site.register(Course)
