# Generated by Django 5.0.3 on 2024-03-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_user_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="date_played",
            field=models.DateField(auto_now_add=True),
        ),
    ]