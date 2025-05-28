from django.db import models # type: ignore

class Type(models.Model):
    name = models.CharField(max_length=100)

class Level(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.RESTRICT)

class Question(models.Model):
    description = models.TextField()
    level = models.ForeignKey(Level, on_delete=models.RESTRICT)

class Option(models.Model):
    description = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.RESTRICT)