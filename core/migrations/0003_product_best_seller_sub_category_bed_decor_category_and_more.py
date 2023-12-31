# Generated by Django 4.2.4 on 2023-08-29 09:12

from django.db import migrations, models
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_product_best_deal"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="best_seller",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="sub_category",
            name="bed_decor_category",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="sub_category",
            name="best_seller",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="sub_category",
            name="door_mats_category",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="sub_category",
            name="exteriors_category",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="sub_category",
            name="flooring_category",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="sub_category",
            name="wallpaper_category",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="sub_category",
            name="window_blinds_category",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="category",
            name="cid",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet="abcdefgh12345",
                length=22,
                max_length=30,
                prefix="cat",
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="main_category",
            name="mid",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet="abcdefgh12345",
                length=22,
                max_length=30,
                prefix="main_cat",
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="sid",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet="abcdefgh12345",
                length=22,
                max_length=30,
                prefix="sub_cat",
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="sub_category",
            name="sid",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet="abcdefgh12345",
                length=22,
                max_length=30,
                prefix="sub_cat",
                unique=True,
            ),
        ),
    ]
