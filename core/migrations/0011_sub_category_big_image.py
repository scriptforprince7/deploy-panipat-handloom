# Generated by Django 4.2.4 on 2023-09-13 08:13

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_sub_category_awning_canopy_brands"),
    ]

    operations = [
        migrations.AddField(
            model_name="sub_category",
            name="big_image",
            field=models.ImageField(
                default="bigsubcategory.jpg", upload_to=core.models.user_directory_path
            ),
        ),
    ]
