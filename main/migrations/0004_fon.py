# Generated by Django 5.0 on 2024-01-13 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_otziv_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto1', models.ImageField(blank=True, upload_to='upload')),
                ('foto2', models.ImageField(blank=True, upload_to='upload')),
                ('foto3', models.ImageField(blank=True, upload_to='upload')),
            ],
        ),
    ]
