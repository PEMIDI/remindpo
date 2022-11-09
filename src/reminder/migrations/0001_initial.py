# Generated by Django 3.2 on 2022-11-09 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified_time')),
                ('title', models.CharField(max_length=32, verbose_name='title')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified_time')),
                ('title', models.CharField(max_length=32, verbose_name='title')),
                ('message', models.CharField(blank=True, max_length=500, null=True, verbose_name='message')),
                ('scheduled_at', models.DateTimeField(verbose_name='scheduled at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='created by')),
            ],
            options={
                'verbose_name': 'reminder',
                'verbose_name_plural': 'reminders',
                'db_table': 'reminder',
            },
        ),
        migrations.CreateModel(
            name='ReminderCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified_time')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='reminder.category', verbose_name='category')),
                ('reminder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='reminder.reminder', verbose_name='reminder')),
            ],
            options={
                'db_table': 'ReminderCategory',
            },
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created_time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified_time')),
                ('alert_time', models.DateTimeField(verbose_name='alert time')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('reminder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to='reminder.reminder', verbose_name='reminder')),
            ],
            options={
                'verbose_name': 'alert',
                'verbose_name_plural': 'alerts',
                'db_table': 'alert',
            },
        ),
    ]
