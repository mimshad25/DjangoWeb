# Generated by Django 3.0.2 on 2020-02-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=155, null=True),
        ),
    ]
