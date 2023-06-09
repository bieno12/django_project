# Generated by Django 4.1.7 on 2023-03-12 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(max_length=12),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.DO_NOTHING, to='management.department'),
        ),
    ]
