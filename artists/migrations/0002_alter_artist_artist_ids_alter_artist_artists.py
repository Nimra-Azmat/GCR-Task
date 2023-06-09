# Generated by Django 4.1.7 on 2023-05-09 10:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("artists", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artist",
            name="artist_ids",
            field=models.CharField(
                max_length=400, primary_key=True, serialize=False, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="artist",
            name="artists",
            field=models.CharField(max_length=400),
        ),
    ]
