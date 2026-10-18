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
    mistake = models.TextField()
    summary = models.TextField()

    def __str__(self):
        return self.title


class Example(models.Model):
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name='examples'
    )
    language = models.CharField(max_length=50)
    code = models.TextField()

    def __str__(self):
        return f"Example: {self.document.title} - {self.language}"