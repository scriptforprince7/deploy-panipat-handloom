# Generated by Django 4.2.4 on 2023-10-15 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0035_alter_productvarient_pid"),
    ]

    operations = [
        migrations.DeleteModel(name="ProductVarient",),
    ]
