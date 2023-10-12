# Generated by Django 4.2.5 on 2023-10-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0003_post_body"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=128, unique=True)),
                ("img_url", models.URLField(blank=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="course",
            name="category",
        ),
        migrations.AddField(
            model_name="course",
            name="img_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="news",
            name="img_url",
            field=models.URLField(blank=True),
        ),
        migrations.DeleteModel(
            name="CourseCategory",
        ),
    ]
