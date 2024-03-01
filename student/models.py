from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=255, null=False)
    registration_id = models.CharField(unique=True, null=False, max_length=10)
    email_id = models.EmailField(max_length=50)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

