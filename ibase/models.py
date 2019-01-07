import uuid

from django.db import models

"""
order_with_respect_to = 'question'
get_latest_by = "order_date"

class Meta:
    db_table = 'music_album'
    ordering = ('-created_at',)
"""


class TimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ObjectModel(TimeModel):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
