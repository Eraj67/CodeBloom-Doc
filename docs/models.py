from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Document(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    syntax = models.TextField()
    key = models.TextField()
    example = models.TextField()
    mistake = models.TextField()
    summary = models.TextField()

    def __str__(self):
        return self.title