from django.db import models
from django.utils.html import mark_safe
import markdown


class Snippet(models.Model):
    code = models.TextField()

    def __str__(self):
        return self.code.replace('\n', ' ')[:100]

class News(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.text.split('\n', 1)[0]

    def html(self):
        return mark_safe(markdown.markdown(self.text))