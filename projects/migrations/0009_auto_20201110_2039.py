# Generated by Django 3.1.3 on 2020-11-10 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_projects_website_button_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='quotes',
            field=models.ManyToManyField(blank=True, related_name='quotes', to='projects.Quotes'),
        ),
    ]
