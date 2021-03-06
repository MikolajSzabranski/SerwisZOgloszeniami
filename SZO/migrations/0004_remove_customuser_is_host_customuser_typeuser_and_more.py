# Generated by Django 4.0.3 on 2022-04-23 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SZO', '0003_remove_customuser_typeuser_customuser_is_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_host',
        ),
        migrations.AddField(
            model_name='customuser',
            name='typeUser',
            field=models.CharField(choices=[('Job seeker', 'Job seeker'), ('Host', 'Host')], max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=400)),
                ('title', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
