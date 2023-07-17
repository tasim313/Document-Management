# Generated by Django 4.2.2 on 2023-07-17 17:20

import autoslug.fields
import core.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_document"),
    ]

    operations = [
        migrations.CreateModel(
            name="DocumentShare",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.basemodel",
                    ),
                ),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False,
                        null=True,
                        populate_from=core.utils.get_document_share_slug,
                        unique=True,
                    ),
                ),
                (
                    "document",
                    models.ManyToManyField(
                        related_name="document_share_info", to="core.document"
                    ),
                ),
                (
                    "share_person",
                    models.ManyToManyField(
                        related_name="person_share_info", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            bases=("core.basemodel",),
        ),
    ]
