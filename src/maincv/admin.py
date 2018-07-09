from django import forms
from mycv.widgets import HtmlEditor
from django.contrib import admin
from .models import Experience, Education, Skill, Location, Profile, Language

# Register your models here.

# class EducationAdminForm(forms.ModelForm):
#     model = Education
#     class Meta:
#         fields = '__all__'
#         widgets = {
#             'DegreeDescription': HtmlEditor(attrs={'style': 'width: 90%; height: 100%;'}),
#         }

# class ExperienceAdminForm(forms.ModelForm):
#     model = Experience
#     class Meta:
#         fields = '__all__'
#         widgets = {
#             'ExperienceDescription': HtmlEditor(attrs={'style': 'width: 90%; height: 100%;'}),
#         }


# class CurriculumAdmin(admin.ModelAdmin):
#     list_display = ['__str__', "FirstName", "UpdatedOn", "HasFacebook"]
#     list_display_links = ['FirstName']
#     class Meta:
#         model = Curriculum


# class EducationAdmin(admin.ModelAdmin):
#     form = EducationAdminForm
#     list_display = ['__str__', 'SchoolName', 'DegreeName', 'StartDate', 'EndDate']
#     class Meta:
#         model = Education

# class ExperienceAdmin(admin.ModelAdmin):
#     form = ExperienceAdminForm
#     list_display = ['__str__', 'Title', 'Company']
#     class Meta:
#         model = Experience





#admin.site.register(Curriculum, CurriculumAdmin)
admin.site.register(Education)#, EducationAdmin)
admin.site.register(Experience)#, ExperienceAdmin)
#admin.site.register(Technology)
admin.site.register(Skill)
admin.site.register(Location)
admin.site.register(Profile)
admin.site.register(Language)