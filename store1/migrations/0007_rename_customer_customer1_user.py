# Generated by Django 3.2.6 on 2021-08-13 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store1', '0006_auto_20210813_1248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer1',
            old_name='customer',
            new_name='user',
        ),
    ]