# Generated by Django 3.2.16 on 2022-11-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_member_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='content',
            new_name='blurb',
        ),
        migrations.AddField(
            model_name='member',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
