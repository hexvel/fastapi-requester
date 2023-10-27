from tortoise.models import Model
from tortoise import fields


class Bot(Model):
    user_id = fields.IntField(pk=True)
    history = fields.JSONField(default=dict)
    role = fields.CharField(max_length=100, default="default")
    is_active = fields.BooleanField(default=False)
    is_blocked = fields.BooleanField(default=False)
    is_admin = fields.BooleanField(default=False)
