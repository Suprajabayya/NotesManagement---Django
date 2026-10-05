from django.db import models

# Create your models here.
# from django.db import models


class Note(models.Model):

    LANGUAGE_CHOICES = [
        ('Python', 'Python'),
        ('Data Analytics', 'Data Analytics'),
        ('JavaScript', 'JavaScript'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
    ]

    language = models.CharField(
        max_length=50,
        choices=LANGUAGE_CHOICES
    )

    topic = models.CharField(max_length=100)

    question = models.CharField(max_length=255)

    answer = models.TextField()

    def __str__(self):
        return self.question