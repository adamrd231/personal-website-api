# Generated by Django 3.1.3 on 2020-11-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20201114_0820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='project_image',
        ),
        migrations.AddField(
            model_name='photos',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
