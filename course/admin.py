from django.contrib import admin
from .models import Unit
from .models import Module
from .models import Course
from .models import Discipline
from .models import Programme
from .models import Level
from .models import Institute

admin.site.site_header = "Outcome Based Course"
admin.site.register(Unit)
admin.site.register(Module)
admin.site.register(Course)
admin.site.register(Discipline)
admin.site.register(Programme)
admin.site.register(Level)
admin.site.register(Institute)
