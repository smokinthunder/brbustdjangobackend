# Generated by Django 5.0.2 on 2024-02-24 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_videos_videosdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videosdb',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
