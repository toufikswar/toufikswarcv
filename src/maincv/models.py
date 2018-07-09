from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime


class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Language(models.Model):
    LANG_LEVEL = (
        ('Basic','BASIC'),
        ('Intermediate','INTERMEDIATE'),
        ('Professional','PROFESSIONAL'),
        ('Native','NATIVE'),
    )
    name = models.CharField(max_length=100, verbose_name="Language Name")
    level = models.CharField(max_length=100, choices=LANG_LEVEL, verbose_name="Level")

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Skill Name")
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True, blank=True, verbose_name="Address")
    birthday = models.DateField(null=True, blank=True, verbose_name="Birthday")
    phone = models.CharField(max_length=100,null=True, blank=True, verbose_name="Phone")
    introduction = models.TextField(blank=True, null=True,max_length=1000, verbose_name="Introduction")
    quote = models.CharField(blank=True, null=True,max_length=400, verbose_name="Quote")
    author = models.CharField(blank=True, null=True,max_length=100, verbose_name="Author")

    # Internal
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)

    #Relationships
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    skill = models.ManyToManyField(Skill)
    

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()





class Experience(models.Model):
    companyName = models.CharField(max_length=100, verbose_name="Company",null=True, blank=True)
    jobTitle = models.CharField(max_length=100, verbose_name='Job Title',null=True, blank=True)
    startDate = models.DateField(verbose_name="Start Date",null=True, blank=True)
    endDate = models.DateField(verbose_name="End Date",null=True, blank=True)
    description = models.TextField(verbose_name="Description",null=True, blank=True)
    
    # Internal
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    # Relationships
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.jobTitle


class Education(models.Model):
    schoolName = models.CharField(max_length=100, verbose_name="School Name",null=True, blank=True)
    degreeName = models.CharField(max_length=100, verbose_name="Degree Name",null=True, blank=True)
    startDate = models.DateField(verbose_name="Start Date",null=True, blank=True)
    endDate = models.DateField(verbose_name="End Date",null=True, blank=True)
    description = models.TextField(verbose_name="Description",null=True, blank=True)
    logoURL = models.CharField(max_length=200, verbose_name="Logo URL",null=True, blank=True)
    
    # Internal
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)

    # Relationships
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.degreeName









