# Generated by Django 3.2.16 on 2022-11-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20221110_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]