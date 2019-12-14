from django.db import models
import uuid

# Create your models here.

class Lecture(models.Model):
    lecture_number = models.AutoField(primary_key=True)
    objective = models.TextField()
    resources = models.TextField()

class Module(models.Model):
    module_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    outcome = models.TextField()
    overview = models.TextField()
    resources = models.TextField()
    test = models.TextField()
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

class Course(models.Model):
    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    outcome = models.TextField()
    objective = models.TextField()
    test = models.TextField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
