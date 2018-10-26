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
