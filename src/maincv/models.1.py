from django.db import models
from django.urls import reverse

# Create your models here.
class Curriculum(models.Model):
    FirstName = models.CharField(max_length=200, verbose_name="First Name")
    LastName = models.CharField(max_length=200, verbose_name="Last Name")
    Email = models.EmailField(verbose_name="Email Address")
    Phone = models.CharField(blank=True, null=True, max_length=200, verbose_name="Phone Number")
    #can be blank in the form and null in the DB
    FullAddress = models.CharField(blank=True, null=True,max_length=200, verbose_name="Address")
    Timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    UpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    Quote = models.CharField(blank=True, null=True,max_length=400, verbose_name="Quote")
    Introduction = models.CharField(blank=True, null=True,max_length=1000, verbose_name="Presentation")
    HasFacebook = models.BooleanField(verbose_name="Facebook")
    HasTwitter = models.BooleanField(verbose_name="Twitter")
    HasLinkedIn = models.BooleanField(verbose_name="LinkedIn")
    HasGitHub= models.BooleanField(verbose_name="GitHub")

    def __str__(self):
        return self.Email

    def get_absolute_url(self):
        """ method to create an absolute URL for the CV page"""
        return reverse("cv:edit", kwargs={'id': self.pk, 'section': "about"})


class Experience(models.Model):
    Title = models.CharField(max_length=200, verbose_name="Position Title")
    Company = models.CharField(max_length=200, verbose_name="Company Name")
    ExperienceDescription = models.TextField(verbose_name="Job Description")
    #ExperienceDescription = HTMLField('Description')
    StartDate = models.DateField(verbose_name="Start Date")
    EndDate = models.DateField(verbose_name="End Date")
    IsCurrent = models.BooleanField(default=False,verbose_name="Is my current job")
    Timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    UpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    curriculum = models.ForeignKey('Curriculum', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        """ method to create an absolute URL for the Experience page"""
        return reverse("cv:edit", kwargs={'id': self.curriculum.pk, 'section': "experience"}) # pylint: disable=E1101


class Education(models.Model):
    SchoolName = models.CharField(max_length=200, verbose_name="School Name")
    DegreeName = models.CharField(max_length=200, verbose_name="Degree Name")
    StartDate = models.DateField(verbose_name="Start Date")
    EndDate = models.DateField(verbose_name="End Date")
    DegreeDescription = models.TextField('Description')
    #Description = models.TextField(blank=True, null=True, verbose_name="Degree Description")
    Timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    UpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)
    curriculum = models.ForeignKey('Curriculum', on_delete=models.CASCADE, default=1)
    LogoURL = models.CharField(max_length=200, verbose_name="Logo URL", default="put a URL")

    def __str__(self):
        return self.DegreeName
    
    def get_absolute_url(self):
        """ method to create an absolute URL for the Experience page"""
        return reverse("cv:edit", kwargs={'id': self.curriculum.pk, 'section': "education"}) # pylint: disable=E1101

class Technology(models.Model):
    Name = models.CharField(max_length=200, verbose_name="Skill Name")
    HtmlCode = models.TextField(verbose_name="Html Code")
    Timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    UpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.Name


class Skill(models.Model):
    curriculum = models.ForeignKey('Curriculum', on_delete=models.CASCADE, default=1)
    technology = models.ForeignKey('Technology', on_delete=models.CASCADE, null=True)
    Level = models.CharField(blank=True, null=True, max_length=200, verbose_name="Level")
    Timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    UpdatedOn = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.technology.Name # pylint: disable=E1101

    def get_absolute_url(self):
        """ method to create an absolute URL for the Experience page"""
        return reverse("cv:edit", kwargs={'id': self.curriculum.pk, 'section': "skill"}) # pylint: disable=E1101


