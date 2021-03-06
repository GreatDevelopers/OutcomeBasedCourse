# Generated by Django 3.0.1 on 2020-01-27 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0015_outcome_course_outcome"),
    ]

    operations = [
        migrations.AlterField(
            model_name="outcome",
            name="outcome",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name="outcome",
            unique_together={("outcome", "outcome_short_name", "action_verb")},
        ),
    ]
