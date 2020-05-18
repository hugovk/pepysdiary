# Generated by Django 2.0.1 on 2018-01-15 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("indepth", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="intro",
            field=models.TextField(help_text="Can use Markdown."),
        ),
        migrations.AlterField(
            model_name="article",
            name="intro_html",
            field=models.TextField(
                blank=True,
                help_text="The intro field, with Markdown etc, turned into HTML.",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.SlugField(unique_for_date="date_published"),
        ),
        migrations.AlterField(
            model_name="article",
            name="status",
            field=models.IntegerField(
                choices=[(10, "Draft"), (20, "Published")], default=10
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="text",
            field=models.TextField(
                blank=True,
                help_text="Can use Markdown. Any images should be put in `pepysdiary/indepth/static/img/indepth/`.",  # noqa: E501
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="text_html",
            field=models.TextField(
                blank=True,
                help_text="The text field, with Markdown etc, turned into HTML.",
            ),
        ),
    ]
