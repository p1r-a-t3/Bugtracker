# Generated by Django 2.2.4 on 2019-09-29 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('error_logger', '0007_verboselog_identifier'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='errorlog',
            options={'ordering': ['logged_on'], 'verbose_name_plural': 'errorLogs'},
        ),
        migrations.AlterModelOptions(
            name='verboselog',
            options={'verbose_name_plural': 'verboseLogs'},
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='error_description',
            field=models.TextField(max_length=500, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='identifier',
            field=models.CharField(blank=True, default='Anonymous', max_length=50, null=True, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='errorlog',
            name='point_of_origin',
            field=models.CharField(max_length=100, verbose_name='origin'),
        ),
        migrations.AlterField(
            model_name='verboselog',
            name='identifier',
            field=models.CharField(blank=True, default='Anonymous', max_length=50, null=True, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='verboselog',
            name='log_description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='verboselog',
            name='point_of_origin',
            field=models.CharField(max_length=100, verbose_name='origin'),
        ),
    ]