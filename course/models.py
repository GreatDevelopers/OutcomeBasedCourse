from django.db import models
import uuid


class Unit(models.Model):
    unit_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    outcome = models.TextField(blank=True, null=True)
    resources = models.TextField(blank=True, null=True)
    test = models.TextField(blank=True, null=True)

    def __str__(self):
        return (
            "Unit "
            + str(self.unit_number)
            + (". " + self.name if self.name else "")
        )


class Module(models.Model):
    module_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    title = models.CharField(max_length=200)
    overview = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    outcome = models.TextField(blank=True, null=True)
    resources = models.TextField(blank=True, null=True)
    test = models.TextField(blank=True, null=True)
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.title


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=20)
    title = models.CharField(max_length=200)
    overview = models.TextField(blank=True, null=True)
    outcome = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    credit = models.DecimalField(max_digits=4, decimal_places=2)
    contact_hours_per_week = models.DecimalField(max_digits=4, decimal_places=2)
    resources = models.TextField(blank=True, null=True)
    test = models.TextField(blank=True, null=True)
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.title


class Discipline(models.Model):
    discipline_code = models.CharField(primary_key=True, max_length=10)
    discipline_name = models.CharField(max_length=50)
    total_credits = models.DecimalField(max_digits=5, decimal_places=2)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.discipline_name


class Programme(models.Model):
    programme_code = models.CharField(primary_key=True, max_length=10)
    programme_name = models.CharField(max_length=50)
    programme_fees = models.IntegerField()
    discipline = models.ForeignKey(
        Discipline, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.programme_name


class Level(models.Model):
    """Level can be: U.G., P.G., etc.
    """

    level_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    level_name = models.CharField(max_length=50)
    programme = models.ForeignKey(
        Programme, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.level_name


class Institute(models.Model):
    institute_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    institute_name = models.CharField(max_length=300)
    level = models.ForeignKey(
        Level, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.institute_name
