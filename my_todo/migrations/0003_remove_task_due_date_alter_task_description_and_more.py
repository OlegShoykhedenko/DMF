# Generated by Django 4.0.3 on 2022-03-18 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_todo', '0002_alter_task_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='due_date',
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
