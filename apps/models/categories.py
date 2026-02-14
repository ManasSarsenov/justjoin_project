from django.db.models.fields import CharField, IntegerField

from apps.models.base import SlugBaseModel


class Category(SlugBaseModel):
    name = CharField(max_length=255)
    description = CharField(max_length=255)
    price = IntegerField()

