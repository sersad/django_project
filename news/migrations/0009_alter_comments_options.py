# Generated by Django 4.0.6 on 2022-08-04 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_comments_users_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['created_date']},
        ),
    ]
