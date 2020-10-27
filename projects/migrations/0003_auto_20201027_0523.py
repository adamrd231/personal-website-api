# Generated by Django 3.1.2 on 2020-10-27 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20201027_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='projects.categories'),
        ),
    ]
