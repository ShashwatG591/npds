# Generated by Django 4.1.1 on 2022-11-24 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('npDetection', '0005_authorities'),
    ]

    operations = [
        migrations.CreateModel(
            name='NormalUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
            ],
        ),
    ]
