# Generated by Django 5.0.3 on 2024-03-29 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_rename_avater_user_avatar"),
    ]

    operations = [
        migrations.RenameField(
            model_name="game",
            old_name="winner",
            new_name="result",
        ),
    ]
