# Generated by Django 3.0.8 on 2020-08-04 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200804_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='body_title',
            field=models.CharField(default='Body_title', max_length=50),
        ),
    ]