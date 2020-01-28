# Generated by Django 3.0.1 on 2019-12-27 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0011_auto_20191228_2318"),
    ]

    operations = [
        migrations.AlterField(
            model_name="institute",
            name="institute_short_name",
            field=models.CharField(
                blank=True,
                max_length=10,
                null=True,
                verbose_name="Institute short name",
            ),
        ),
        migrations.AlterField(
            model_name="level",
            name="level_name",
            field=models.CharField(
                max_length=50, unique=True, verbose_name="Level name"
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="programme_fees",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Programme fees"
            ),
        ),
    ]
