# Generated by Django 5.0.6 on 2024-05-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_name', models.CharField(max_length=150)),
                ('todo_desc', models.CharField(max_length=250)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
