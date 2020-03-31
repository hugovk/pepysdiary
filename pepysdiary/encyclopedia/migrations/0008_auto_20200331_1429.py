# Generated by Django 3.0.4 on 2020-03-31 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('encyclopedia', '0007_populate_topic_search_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='summary_author',
            field=models.ForeignKey(blank=True, default=None, help_text='Optional. Used if Summary Publication Date is set.', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='topic_summaries', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='topic',
            name='summary_publication_date',
            field=models.DateField(blank=True, help_text='Optional. Used if Summary Author is set.', null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='map_category',
            field=models.CharField(blank=True, choices=[('area', 'Area'), ('gate', 'Gate'), ('home', "Pepys' home(s)"), ('misc', 'Miscellaneous'), ('road', 'Road or Street'), ('stair', 'Stair or Pier'), ('town', 'Town or Village')], db_index=True, help_text='(UNUSED?) The type of object this is on maps', max_length=20),
        ),
    ]
