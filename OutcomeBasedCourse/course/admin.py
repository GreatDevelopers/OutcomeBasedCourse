from django.contrib import admin
from .models import CognitiveLevel
from .models import ActionVerb
from .models import Outcome
from .models import Institute
from .models import Level
from .models import Programme
from .models import Department
from .models import Discipline
from .models import Course
from .models import Module
from .models import Unit

admin.site.site_header = "Outcome Based Course"
admin.site.register(CognitiveLevel)
admin.site.register(ActionVerb)
admin.site.register(Outcome)
admin.site.register(Institute)
admin.site.register(Level)
admin.site.register(Programme)
admin.site.register(Department)
admin.site.register(Discipline)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Unit)
