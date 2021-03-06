# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-15 13:03
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
            name='Chama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, unique=True)),
                ('paybillNo', models.PositiveIntegerField(unique=True)),
                ('contribution_amnt', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contribution_interval', models.CharField(blank=True, choices=[('d', 'Daily'), ('w', 'Weekly'), ('m', 'Monthly'), ('q', 'Quartely')], default='d', help_text='Contribution Intervals', max_length=1)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['Name'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='photos')),
                ('description', models.CharField(max_length=255)),
                ('Adress', models.EmailField(blank=True, max_length=254)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('group_name',),
            },
        ),
        migrations.CreateModel(
            name='Group_contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount_contributed', models.CharField(max_length=150)),
                ('contribution_date', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mychama.Group')),
            ],
            options={
                'ordering': ('group',),
            },
        ),
        migrations.CreateModel(
            name='Group_member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=150)),
                ('natinal_id', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='photos')),
                ('contact_adress', models.CharField(max_length=150)),
                ('EmailAdress', models.EmailField(blank=True, max_length=254)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mychama.Group')),
            ],
            options={
                'ordering': ('member_name',),
            },
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('avartar', models.ImageField(upload_to='photos')),
                ('contact_adress', models.CharField(max_length=150)),
                ('EmailAdress', models.EmailField(blank=True, max_length=254)),
                ('natinal_id', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Individual_contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount_contributed', models.CharField(max_length=150)),
                ('contribution_date', models.DateTimeField(auto_now_add=True)),
                ('individual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mychama.Individual')),
            ],
            options={
                'ordering': ('individual',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(upload_to='profiles/')),
                ('bio', models.CharField(max_length=250)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['bio'],
            },
        ),
    ]
