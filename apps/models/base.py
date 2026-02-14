from django.db.models import Model
from django.db.models.fields import SlugField, DateTimeField
from django.utils.text import slugify


class SlugBaseModel(Model):
    slug = SlugField(max_length=255, unique=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            if hasattr(self, 'name'):
                self.slug = slugify(self.name)

            if hasattr(self, 'title'):
                self.slug = slugify(self.title)
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


class CreatedBaseModel(Model):
    updated_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
