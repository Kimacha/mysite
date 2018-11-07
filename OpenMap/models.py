from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.


class AboutOpenMap(models.Model):
    about_us = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    objectives = models.TextField()

    def __str__(self):
        return "About Open maps"

    def save(self, *args, **kwargs):
        if AboutOpenMap.objects.exists() and not self.pk:
            raise ValidationError('There can only be one instance of this class')
        return super(AboutOpenMap, self).save(*args, **kwargs)


class WhatWeDo(models.Model):
    about = models.ForeignKey(AboutOpenMap, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    details = models.TextField()
    image = models.ImageField()

    class Meta:
        verbose_name_plural = 'What We Do'


class OurProjects(models.Model):
    title = models.CharField(max_length=128)
    details = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Our Projects'


class TeamMembers(models.Model):
    name = models.CharField(max_length=128)
    position = models.CharField(max_length=128)
    bio = models.TextField()
    image = models.ImageField()
    email = models.EmailField()
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    skype = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Team members"
        verbose_name = "Team Member"


class Phrase(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content


class Library(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Libraries"
        verbose_name = "Library"


class projectPage(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField()
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "project page"
        verbose_name = "project page"


class WhatWeDoPhrase(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "WhatWeDoPhrase"
        verbose_name = "WhatWeDoPhrase"


class ProjectPhrase(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "ProjectPhrase"
        verbose_name = "ProjectPhrase"


class TeamPhrase(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "TeamPhrase"
        verbose_name = "TeamPhrase"


class LibraryPhrase(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "LibraryPhrase"
        verbose_name = "LibraryPhrase"


class BlogPhrase(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "BlogPhrase"
        verbose_name = "BlogPhrase"


class ContactPhrase(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "ContactPhrase"
        verbose_name = "ContactPhrase"