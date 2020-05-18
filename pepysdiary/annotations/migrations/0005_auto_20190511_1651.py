# Generated by Django 2.1.8 on 2019-05-11 16:51

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("annotations", "0004_reset_ids_20190511_1549"),
    ]

    operations = [
        migrations.AddField(
            model_name="annotation",
            name="search_document",
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddIndex(
            model_name="annotation",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["search_document"], name="annotations_search__ab8015_gin"
            ),
        ),
    ]
