# Generated by Django 4.1 on 2022-08-24 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0003_alter_domainpage_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domainpage',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания'),
        ),
    ]