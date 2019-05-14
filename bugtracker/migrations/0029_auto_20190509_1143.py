# Generated by Django 2.2 on 2019-05-09 11:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0028_auto_20190509_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errors',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('c0a295be-ba93-48ff-9a66-d51bcbacae7a'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='errors',
            name='logged_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 9, 11, 43, 3, 360418, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='logs',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('31761a52-5ec1-4288-af31-fdc661b49e16'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='logs',
            name='logged_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 9, 11, 43, 3, 361795, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projects',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('a7b6e53c-ccb9-415d-9c8f-fa45e0f40f48'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_id',
            field=models.UUIDField(default=uuid.UUID('839e66ee-4419-4340-82c8-744b16bd467c'), unique=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 9, 11, 43, 3, 357828, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projecttoken',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('9b6b8193-3058-443b-9bef-8680d3f0d096'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projecttoken',
            name='generated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 9, 11, 43, 3, 359146, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projecttoken',
            name='refresh_token',
            field=models.UUIDField(default=uuid.UUID('b2f59ee7-d9a1-4350-8809-da45429ec136'), unique=True),
        ),
        migrations.AlterField(
            model_name='projecttoken',
            name='token',
            field=models.UUIDField(default=uuid.UUID('5ab2ae72-40ba-483d-83d4-7847d21233e0'), unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default=uuid.UUID('5857d157-52ef-451d-b29b-5d16dfae913d'), primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('266026ed-9e09-4c6a-a447-0958c0be8256'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='generated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 9, 11, 43, 3, 356150, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='refresh_token',
            field=models.UUIDField(default=uuid.UUID('6230db29-db3f-489b-9e81-473d97cc2601'), unique=True),
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='token',
            field=models.UUIDField(default=uuid.UUID('1beef465-d082-449e-bcb3-5c3d34fbfc56'), unique=True),
        ),
    ]