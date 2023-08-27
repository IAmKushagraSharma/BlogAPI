from django.conf import settings
from django.db import models


class Post(models.Model):

    title = models.CharField(("title"), max_length=200)
    body = models.TextField(("body"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(("created_at"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(("updated_at"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = ("post")
        verbose_name_plural = ("posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
