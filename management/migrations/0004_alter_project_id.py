# Generated by Django 5.1.4 on 2024-12-22 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_alter_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
