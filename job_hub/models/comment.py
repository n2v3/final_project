from django.db import models
from .vacancy import Vacancy


class Comment(models.Model):
    comment_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    vacancy = models.ForeignKey(
        Vacancy, on_delete=models.CASCADE, null=True, related_name="comments"
    )
