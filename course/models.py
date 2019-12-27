from django.db import models
from OutcomeBasedCourse.config.verbose_names import *

# from djmoney.models.fields import MoneyField
import uuid


class CognitiveLevel(models.Model):
    cognitive_level = models.CharField(max_length=100, unique=True)
    cognitive_level_short_name = models.CharField(
        max_length=10, blank=True, null=True
    )

    def __str__(self):
        return self.cognitive_level


class ActionVerb(models.Model):
    action_verb = models.CharField(max_length=20)
    action_verb_short_name = models.CharField(
        max_length=10, blank=True, null=True
    )
    cognitive_level = models.ForeignKey(
        CognitiveLevel, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.action_verb


class Outcome(models.Model):
    outcome = models.CharField(max_length=255, unique=True)
    outcome_short_name = models.CharField(max_length=10, blank=True, null=True)
    action_verb = models.ForeignKey(ActionVerb, on_delete=models.CASCADE)

    def __str__(self):
        return self.outcome


class Objective(models.Model):
    objective = models.CharField(max_length=255, unique=True)
    objective_short_name = models.CharField(
        max_length=10, blank=True, null=True
    )

    def __str__(self):
        return self.objective


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
    institute_short_name = models.CharField(
        verbose_name=INSTITUTE_SINGULAR + " short name",
        max_length=10,
        blank=True,
        null=True,
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
    level_short_name = models.CharField(
        verbose_name=LEVEL_SINGULAR + " short name",
        max_length=10,
        blank=True,
        null=True,
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
    programme_short_name = models.CharField(
        verbose_name=PROGRAMME_SINGULAR + " short name",
        max_length=10,
        blank=True,
        null=True,
    )
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


class Department(models.Model):
    department_code = models.CharField(
        verbose_name=DEPARTMENT_SINGULAR + " code",
        primary_key=True,
        max_length=10,
    )
    department_name = models.CharField(
        verbose_name=DEPARTMENT_SINGULAR + " name", max_length=255, unique=True
    )
    department_short_name = models.CharField(
        verbose_name=DEPARTMENT_SINGULAR + " short name",
        max_length=10,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.department_name

    class Meta:
        verbose_name = DEPARTMENT_SINGULAR
        verbose_name_plural = DEPARTMENT_PLURAL


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
    discipline_short_name = models.CharField(
        verbose_name=DISCIPLINE_SINGULAR + " short name",
        max_length=10,
        blank=True,
        null=True,
    )
    programme = models.ForeignKey(
        Programme,
        verbose_name=PROGRAMME_PLURAL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    offered_by = models.ForeignKey(
        Department,
        verbose_name=DEPARTMENT_SINGULAR,
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
    course_short_name = models.CharField(
        verbose_name=COURSE_SINGULAR + " short name",
        max_length=10,
        blank=True,
        null=True,
    )
    course_overview = models.TextField(
        verbose_name=COURSE_SINGULAR + " overview", blank=True, null=True
    )
    course_credit = models.DecimalField(
        verbose_name=COURSE_SINGULAR + " credit", max_digits=4, decimal_places=2
    )
    lecture_contact_hours_per_week = models.DecimalField(
        max_digits=4, decimal_places=2
    )
    tutorial_contact_hours_per_week = models.DecimalField(
        max_digits=4, decimal_places=2
    )
    practical_contact_hours_per_week = models.DecimalField(
        max_digits=4, decimal_places=2
    )
    course_resources = models.TextField(
        verbose_name=COURSE_SINGULAR + " resources", blank=True, null=True
    )
    course_test = models.TextField(
        verbose_name=COURSE_SINGULAR + " test", blank=True, null=True
    )
    course_outcome = models.ManyToManyField(
        Outcome, verbose_name=COURSE_SINGULAR + " outcome", blank=True
    )
    course_objective = models.ManyToManyField(
        Objective, verbose_name=COURSE_SINGULAR + " objective", blank=True
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
    module_short_name = models.CharField(
        verbose_name=MODULE_SINGULAR + " short name",
        max_length=10,
        blank=True,
        null=True,
    )
    module_overview = models.TextField(
        verbose_name=MODULE_SINGULAR + " overview", blank=True, null=True
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
    module_outcome = models.ManyToManyField(
        Outcome, verbose_name=MODULE_SINGULAR + " outcome", blank=True
    )
    module_objective = models.ManyToManyField(
        Objective, verbose_name=MODULE_SINGULAR + " objective", blank=True,
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
    unit_body = models.TextField(
        verbose_name=UNIT_SINGULAR + " body", blank=True, null=True
    )
    unit_resources = models.TextField(
        verbose_name=UNIT_SINGULAR + " resources", blank=True, null=True
    )
    unit_test = models.TextField(
        verbose_name=UNIT_SINGULAR + " test", blank=True, null=True
    )
    unit_short_name = models.CharField(
        verbose_name=UNIT_SINGULAR + " short name",
        max_length=10,
        blank=True,
        null=True,
    )
    unit_outcome = models.ManyToManyField(
        Outcome, verbose_name=UNIT_SINGULAR + " outcome", blank=True
    )
    unit_objective = models.ManyToManyField(
        Objective, verbose_name=UNIT_SINGULAR + " objective", blank=True,
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
