# Generated by Django 5.0.3 on 2024-04-05 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rol',
            field=models.CharField(choices=[('student', 'student'), ('teacher', 'teacher')], max_length=30),
        ),
    ]
