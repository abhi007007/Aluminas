# Generated by Django 4.0.4 on 2022-10-14 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField()),
                ('name', models.TextField()),
                ('dob', models.DateField()),
                ('gender', models.TextField()),
                ('phone', models.TextField()),
                ('course', models.TextField()),
            ],
        ),
    ]
