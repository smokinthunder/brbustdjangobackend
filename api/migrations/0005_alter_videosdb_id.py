# Generated by Django 5.0.2 on 2024-02-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_videosdb_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videosdb',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
