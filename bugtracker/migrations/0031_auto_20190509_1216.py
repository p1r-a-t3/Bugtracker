# Generated by Django 2.2 on 2019-05-09 12:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0030_auto_20190509_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errors',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('555d4b2d-7061-4930-891a-042accb52581'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='errors',
            name='logged_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 9, 12, 16, 44, 686471, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='logs',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('b3d6a59b-6c2a-46aa-9c5b-9979f9b040ae'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='logs',
            name='logged_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 9, 12, 16, 44, 687106, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projects',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('b8b753e3-e512-4a7e-835c-8b14d47d58a9'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_id',
            field=models.UUIDField(default=uuid.UUID('634acf49-a7ab-48cd-a2e8-c441e4bff454'), unique=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 9, 12, 16, 44, 684050, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projecttoken',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('16b5dc2b-8249-4bbc-a434-3de79bed50f0'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projecttoken',
            name='generated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 9, 12, 16, 44, 685962, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='projecttoken',
            name='refresh_token',
            field=models.UUIDField(default=uuid.UUID('615e5830-a647-4d55-b867-79b60942ed41'), unique=True),
        ),
        migrations.AlterField(
            model_name='projecttoken',
            name='token',
            field=models.UUIDField(default=uuid.UUID('be367bcb-693c-46a8-9b2f-faa2579f0d96'), unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='_id',
            field=models.UUIDField(default=uuid.UUID('bfdc7b96-025d-47bd-ac15-48729a211e5b'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='generated_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 9, 12, 16, 44, 683213, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='refresh_token',
            field=models.UUIDField(default=uuid.UUID('342a0a91-75c2-4203-82ec-5be9ebcbd954'), unique=True),
        ),
        migrations.AlterField(
            model_name='usertoken',
            name='token',
            field=models.UUIDField(default=uuid.UUID('24dd46ed-8801-409c-a7ed-e5a0e0fcf631'), unique=True),
        ),
    ]