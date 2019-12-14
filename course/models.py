from django.db import models
import uuid

# Create your models here.

class Unit(models.Model):
    unit_number = models.AutoField(primary_key=True)
    overview = models.TextField()
    objective = models.TextField()
    outcome = models.TextField()
    resources = models.TextField()
    test = models.TextField()

    def __str__(self):
        return self.unit_number

class Module(models.Model):
    module_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    overview = models.TextField()
    objective = models.TextField()
    outcome = models.TextField()
    resources = models.TextField()
    test = models.TextField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=20)
    title = models.CharField(max_length=200)
    overview = models.TextField()
    outcome = models.TextField()
    objective = models.TextField()
    credit = models.DecimalField(max_digits=4, decimal_places=2)
    contact_hours_per_week = models.DecimalField(max_digits=4, decimal_places=2)
    resources = models.TextField()
    test = models.TextField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
