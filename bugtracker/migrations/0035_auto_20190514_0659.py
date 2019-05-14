# Generated by Django 2.2 on 2019-05-14 06:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0034_auto_20190514_0626'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='errors',
            options={'ordering': ['logged_at'], 'verbose_name_plural': 'Errors'},
        ),
        migrations.AlterModelOptions(
            name='errorstatus',
            options={'verbose_name_plural': 'ErrorStatus'},
        ),
        migrations.AlterModelOptions(
            name='logs',
            options={'verbose_name_plural': 'Logs'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterModelOptions(
            name='projecttoken',
            options={'verbose_name_plural': 'ProjectToken'},
        ),
        migrations.AlterModelOptions(
            name='projectupdate',
            options={'verbose_name_plural': 'ProjectUpdate'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'get_latest_by': ['created_at'], 'verbose_name_plural': 'User'},
        ),
        migrations.AlterField(
            model_name='errors',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('7311b60b-ac23-4878-aedb-9489630278e6'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='errors',
            name='logged_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 14, 6, 59, 32, 893970, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='errorstatus',
            name='resolved_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 14, 6, 59, 32, 894491, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='errorstatus',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 14, 6, 59, 32, 894512, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='logs',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('cd86b73b-3143-4294-bf5e-5b2989dc720f'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='logs',
            name='logged_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 14, 6, 59, 32, 895027, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projects',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('2e270ef3-959e-4b48-8288-3bc9a6a68c56'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_id',
            field=models.UUIDField(default=uuid.UUID('e2014feb-4787-4bce-a9a1-d02b72e982f7'), unique=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 14, 6, 59, 32, 892599, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projecttoken',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('20c88361-f277-49e6-9c46-e7006bf86435'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projecttoken',
            name='generated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 14, 6, 59, 32, 893542, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projecttoken',
            name='refresh_token',
            field=models.UUIDField(default=uuid.UUID('0f4bde24-6369-444c-8ea5-d9a0ba2fb60d'), unique=True),
        ),
        migrations.AlterField(
            model_name='projecttoken',
            name='token',
            field=models.UUIDField(default=uuid.UUID('3866f2b0-c5a6-4198-b465-2c8177357804'), unique=True),
        ),
        migrations.AlterField(
            model_name='projectupdate',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 14, 6, 59, 32, 893068, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('00b043d7-1c64-4afd-82ee-982f42a1d677'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='generated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 14, 6, 59, 32, 891366, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='refresh_token',
            field=models.UUIDField(default=uuid.UUID('b213f8a9-36df-4392-a54d-924b0d54b1d8'), unique=True),
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='token',
            field=models.UUIDField(default=uuid.UUID('2dcd8e28-a157-43f2-93b5-26a5b195082c'), unique=True),
        ),
    ]
