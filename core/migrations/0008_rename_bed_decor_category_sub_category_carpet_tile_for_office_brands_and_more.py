# Generated by Django 4.2.4 on 2023-09-12 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_rename_title_main_category_main_title"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sub_category",
            old_name="bed_decor_category",
            new_name="carpet_tile_for_office_brands",
        ),
        migrations.RenameField(
            model_name="sub_category",
            old_name="door_mats_category",
            new_name="curtain_sofa_brands",
        ),
        migrations.RenameField(
            model_name="sub_category",
            old_name="exteriors_category",
            new_name="curtains_rods_channel_brands",
        ),
        migrations.RenameField(
            model_name="sub_category",
            old_name="flooring_category",
            new_name="foam_material_brands",
        ),
        migrations.RenameField(
            model_name="sub_category",
            old_name="window_blinds_category",
            new_name="hospital_walls_brands",
        ),
        migrations.AddField(
            model_name="sub_category",
            name="mattresses_brands",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="sub_category",
            name="rugs_brands",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="sub_category",
            name="window_blinds_brands",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="sub_category",
            name="wooden_laminate_flooring_brands",
            field=models.BooleanField(default=False),
        ),
    ]
