# Generated by Django 4.0.4 on 2022-06-12 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
                ('roll', models.CharField(blank=True, max_length=225, null=True)),
                ('city', models.CharField(blank=True, max_length=225, null=True)),
            ],
        ),
    ]