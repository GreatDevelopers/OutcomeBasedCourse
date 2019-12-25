from django.db import models
from OutcomeBasedCourse.config.verbose_names import *

# from djmoney.models.fields import MoneyField
import uuid


class Institute(models.Model):
    institute_id = models.UUIDField(
        verbose_name=INSTITUTE_SINGULAR + " id",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    institute_name = models.CharField(
        verbose_name=INSTITUTE_SINGULAR + " name", max_length=300
    )

    def __str__(self):
        return self.institute_name

    class Meta:
        verbose_name = INSTITUTE_SINGULAR
        verbose_name_plural = INSTITUTE_PLURAL


class Level(models.Model):
    level_id = models.UUIDField(
        verbose_name=LEVEL_SINGULAR + " id",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    level_name = models.CharField(
        verbose_name=LEVEL_SINGULAR + " name", max_length=50
    )
    institute = models.ManyToManyField(
        Institute, verbose_name=INSTITUTE_PLURAL, blank=True
    )

    def __str__(self):
        return self.level_name

    class Meta:
        verbose_name = LEVEL_SINGULAR
        verbose_name_plural = LEVEL_PLURAL


class Programme(models.Model):
    programme_code = models.CharField(
        verbose_name=PROGRAMME_SINGULAR + " code",
        primary_key=True,
        max_length=10,
    )
    programme_name = models.CharField(
        verbose_name=PROGRAMME_SINGULAR + " name", max_length=50
    )
    programme_fees = models.FloatField(
        verbose_name=PROGRAMME_SINGULAR + " fees", blank=True, null=True
    )
    # Will be used for currency fields
    # programme_fees = MoneyField(
    #     max_digits=10, decimal_places=2, null=True, default_currency="INR"
    # )
    level = models.ForeignKey(
        Level,
        verbose_name=LEVEL_PLURAL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.programme_name

    class Meta:
        verbose_name = PROGRAMME_SINGULAR
        verbose_name_plural = PROGRAMME_PLURAL


class Discipline(models.Model):
    discipline_code = models.CharField(
        verbose_name=DISCIPLINE_SINGULAR + " code",
        primary_key=True,
        max_length=10,
    )
    discipline_name = models.CharField(
        verbose_name=DISCIPLINE_SINGULAR + " name", max_length=50
    )
    total_credits = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    programme = models.ForeignKey(
        Programme,
        verbose_name=PROGRAMME_PLURAL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.discipline_name

    class Meta:
        verbose_name = DISCIPLINE_SINGULAR
        verbose_name_plural = DISCIPLINE_PLURAL


class Course(models.Model):
    course_id = models.CharField(
        verbose_name=COURSE_SINGULAR + " id", primary_key=True, max_length=20
    )
    course_title = models.CharField(
        verbose_name=COURSE_SINGULAR + " title", max_length=200
    )
    course_overview = models.TextField(
        verbose_name=COURSE_SINGULAR + " overview", blank=True, null=True
    )
    course_outcome = models.TextField(
        verbose_name=COURSE_SINGULAR + " outcome", blank=True, null=True
    )
    course_objective = models.TextField(
        verbose_name=COURSE_SINGULAR + " objective", blank=True, null=True
    )
    course_credit = models.DecimalField(
        verbose_name=COURSE_SINGULAR + " credit", max_digits=4, decimal_places=2
    )
    contact_hours_per_week = models.DecimalField(max_digits=4, decimal_places=2)
    course_resources = models.TextField(
        verbose_name=COURSE_SINGULAR + " resources", blank=True, null=True
    )
    course_test = models.TextField(
        verbose_name=COURSE_SINGULAR + " test", blank=True, null=True
    )
    discipline = models.ManyToManyField(
        Discipline, verbose_name=DISCIPLINE_PLURAL, blank=True
    )

    def __str__(self):
        return self.course_title

    class Meta:
        verbose_name = COURSE_SINGULAR
        verbose_name_plural = COURSE_PLURAL


class Module(models.Model):
    module_id = models.UUIDField(
        verbose_name=MODULE_SINGULAR + " id",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    module_title = models.CharField(
        verbose_name=MODULE_SINGULAR + " title", max_length=200
    )
    module_overview = models.TextField(
        verbose_name=MODULE_SINGULAR + " overview", blank=True, null=True
    )
    module_outcome = models.TextField(
        verbose_name=MODULE_SINGULAR + " outcome", blank=True, null=True
    )
    module_objective = models.TextField(
        verbose_name=MODULE_SINGULAR + " objective", blank=True, null=True
    )
    module_body = models.TextField(
        verbose_name=MODULE_SINGULAR + " body", blank=True, null=True
    )
    module_resources = models.TextField(
        verbose_name=MODULE_SINGULAR + " resources", blank=True, null=True
    )
    module_test = models.TextField(
        verbose_name=MODULE_SINGULAR + " test", blank=True, null=True
    )
    course = models.ManyToManyField(
        Course, verbose_name=COURSE_PLURAL, blank=True
    )

    def __str__(self):
        return self.module_title

    class Meta:
        verbose_name = MODULE_SINGULAR
        verbose_name_plural = MODULE_PLURAL


class Unit(models.Model):
    unit_number = models.AutoField(
        verbose_name=UNIT_SINGULAR + " number", primary_key=True
    )
    unit_name = models.CharField(
        verbose_name=UNIT_SINGULAR + " name",
        max_length=200,
        blank=True,
        null=True,
    )
    unit_overview = models.TextField(
        verbose_name=UNIT_SINGULAR + " overview", blank=True, null=True
    )
    unit_outcome = models.TextField(
        verbose_name=UNIT_SINGULAR + " outcome", blank=True, null=True
    )
    unit_objective = models.TextField(
        verbose_name=UNIT_SINGULAR + " objective", blank=True, null=True
    )
    unit_body = models.TextField(
        verbose_name=UNIT_SINGULAR + " body", blank=True, null=True
    )
    unit_resources = models.TextField(
        verbose_name=UNIT_SINGULAR + " resources", blank=True, null=True
    )
    unit_test = models.TextField(
        verbose_name=UNIT_SINGULAR + " test", blank=True, null=True
    )
    module = models.ManyToManyField(
        Module, verbose_name=MODULE_PLURAL, blank=True
    )

    def __str__(self):
        return (
            "Unit "
            + str(self.unit_number)
            + (". " + self.unit_name if self.unit_name else "")
        )

    class Meta:
        verbose_name = UNIT_SINGULAR
        verbose_name_plural = UNIT_PLURAL
