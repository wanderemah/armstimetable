# Generated by Django 2.1 on 2018-08-02 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('armstimetable', '0009_auto_20180802_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='event',
            name='tutor',
        ),
        migrations.RemoveField(
            model_name='responses',
            name='query',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='user',
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.DeleteModel(
            name='allowedCourse',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Lecturer',
        ),
        migrations.DeleteModel(
            name='Responses',
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
        migrations.DeleteModel(
            name='Specialty',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]