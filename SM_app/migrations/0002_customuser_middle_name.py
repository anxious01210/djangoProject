# Generated by Django 3.2.4 on 2021-06-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SM_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='middle name'),
        ),
    ]