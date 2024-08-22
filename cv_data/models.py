from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return self.name

class Contact(models.Model):
    TYPE_CHOICES = [
        ('email','Email'),
        ('phone','Phone'),
        ('adress','Adress'),
        ('github','Github'),
        ('linkedin','Linkedin'),
        ('facebook','Facebook'),
        ('instagram','Instagram'),
        ('twitter','Twitter'),
        ('other','Other'),
    ]
    value = models.CharField(max_length=50, null=False)
    kind = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.kind} : {self.value}"

class Language(models.Model):
    name = models.CharField(max_length=20, null=False)
    proficiency = models.IntegerField()

    def __str__(self):
        return self.name

class Aptitude(models.Model):
    value = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.value

class Skill(models.Model):
    value = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.value

class Education(models.Model):
    institution = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=30)
    start_date = models.IntegerField(null=False)
    end_date = models.IntegerField(null=True)

    def __str__(self):
        return self.institution

