import uuid
from django.db import models
from django.utils import timezone

# It should be analogous to the Flask's User dataclass
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)