# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-01-26 21:10
from __future__ import unicode_literals

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
            name='MedRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chief_complaint', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=250)),
                ('medications', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinician', models.CharField(max_length=250)),
                ('pat_name', models.CharField(max_length=500)),
                ('bloodtype', models.CharField(max_length=100)),
                ('pat_img', models.FileField(upload_to='')),
                ('contact', models.CharField(max_length=100)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='medrecord',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ehealth.Patient'),
        ),
    ]
