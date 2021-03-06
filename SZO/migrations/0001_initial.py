# Generated by Django 4.0.3 on 2022-04-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('password1', models.CharField(max_length=30)),
                ('password2', models.CharField(max_length=30)),
                ('typeUser', models.CharField(choices=[('Job seeker', 'Job seeker'), ('Host', 'Host')], max_length=100, null=True)),
            ],
        ),
    ]
