# Generated by Django 5.1.4 on 2024-12-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(max_length=500),
        ),
    ]