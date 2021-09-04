# Generated by Django 3.2.7 on 2021-09-04 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='', verbose_name='/profile')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='', verbose_name='/profile')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Council',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='', verbose_name='/council')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=100)),
                ('rotaryid', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='', verbose_name='/council')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('img', models.ImageField(upload_to='', verbose_name='/gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Hero_Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('text_subtitle', models.CharField(max_length=500)),
                ('img_mobile', models.ImageField(upload_to='', verbose_name='/mobile')),
                ('img_web', models.ImageField(upload_to='', verbose_name='/web')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='International',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='', verbose_name='/profile')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=500)),
                ('date', models.DateField(blank=True, default=datetime.date.today)),
                ('img', models.ImageField(upload_to='', verbose_name='/profile')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='', verbose_name='/profile')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Vocational',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='', verbose_name='/profile')),
                ('url', models.URLField()),
            ],
        ),
    ]