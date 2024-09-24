# Generated by Django 4.1 on 2024-09-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0002_actor_genre_alter_movie_options_movie_actors_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CinemaHall",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("rows", models.IntegerField()),
                ("seats_in_row", models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name="genre",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]