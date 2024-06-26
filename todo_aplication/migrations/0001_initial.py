# Generated by Django 4.2.13 on 2024-05-16 23:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('completed_task', models.BooleanField(default=False)),
                ('date_completed', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
