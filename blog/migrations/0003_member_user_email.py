# Generated by Django 3.2.16 on 2022-11-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_member_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='user_email',
            field=models.EmailField(blank=True, max_length=70, unique=True),
        ),
    ]
