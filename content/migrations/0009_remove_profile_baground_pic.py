# Generated by Django 4.1.1 on 2022-10-06 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0008_profile_baground_pic_alter_contact_email"),
    ]

    operations = [
        migrations.RemoveField(model_name="profile", name="baground_pic",),
    ]