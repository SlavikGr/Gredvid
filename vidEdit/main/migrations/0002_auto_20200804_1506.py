# Generated by Django 3.0.8 on 2020-08-04 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='text',
            field=models.TextField(max_length=130),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
