# Generated by Django 3.2.4 on 2021-06-14 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('course', '0002_alter_course_table'),
        ('participant', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='courseparticipant',
            unique_together={('student', 'course')},
        ),
    ]