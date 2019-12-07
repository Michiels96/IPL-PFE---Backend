# Generated by Django 3.0 on 2019-12-05 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('session_question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='professionnel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]