# Generated by Django 2.2.6 on 2019-12-18 03:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='creator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_creators', to=settings.AUTH_USER_MODEL),
        ),
    ]
