# Generated by Django 4.0.3 on 2022-04-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SZO', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='typeUser',
            field=models.CharField(choices=[('seeker', 'Seeker'), ('host', 'Host')], max_length=100, null=True),
        ),
    ]
