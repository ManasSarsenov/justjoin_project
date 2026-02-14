from django.db.models import JSONField
from django.db.models.fields import CharField, PositiveIntegerField, PositiveSmallIntegerField, TextField

from apps.models.base import SlugBaseModel, CreatedBaseModel


class Product(SlugBaseModel, CreatedBaseModel):
    name = CharField(max_length=255)
    price = PositiveIntegerField()
    discount = PositiveSmallIntegerField(db_default=0)
    specification = JSONField(default=dict, blank=True)
    description = TextField(blank=True)
