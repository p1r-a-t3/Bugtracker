# Generated by Django 2.2 on 2019-05-29 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0045_auto_20190522_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttoken',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bugtracker.Projects'),
        ),
    ]
