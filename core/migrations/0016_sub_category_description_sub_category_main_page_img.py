# Generated by Django 4.2.4 on 2023-09-15 10:29

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_main_category_icon_img"),
    ]

    operations = [
        migrations.AddField(
            model_name="sub_category",
            name="description",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sub_category",
            name="main_page_img",
            field=models.ImageField(
                default="mainpageimg.jpg", upload_to=core.models.user_directory_path
            ),
        ),
    ]
