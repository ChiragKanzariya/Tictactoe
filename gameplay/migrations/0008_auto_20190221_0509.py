# Generated by Django 2.1.5 on 2019-02-21 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0007_auto_20190221_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='by_first_player',
            field=models.BooleanField(editable=False),
        ),
    ]
