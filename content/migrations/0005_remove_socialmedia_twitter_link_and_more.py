# Generated by Django 4.1.1 on 2022-09-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0004_alter_about_age_alter_skill_pct"),
    ]

    operations = [
        migrations.RemoveField(model_name="socialmedia", name="Twitter_link",),
        migrations.AlterField(
            model_name="education",
            name="descriptions",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="experience",
            name="responsibility",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="personal",
            name="link",
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
