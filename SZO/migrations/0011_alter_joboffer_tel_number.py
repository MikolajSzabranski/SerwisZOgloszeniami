# Generated by Django 4.0.3 on 2022-05-08 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SZO', '0010_delete_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joboffer',
            name='tel_number',
            field=models.CharField(max_length=9),
        ),
    ]
