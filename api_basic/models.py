from django.db import models


class Quote(models.Model):
    quote = models.CharField(max_length=225)
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote
