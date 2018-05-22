from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms import formset_factory


from .models import Curriculum, Experience, Technology
#from .forms import CurriculumModelForm, ExperienceModelForm, SkillModelForm,ExperienceModelFormSet, EducationModelFormSet, SkillModelFormSet, SkillModelFormSetHelper

# Create your views here.

def home(request):

    person_info = get_object_or_404(Curriculum, id=1)
    person_experiences_list = person_info.experience_set.all().order_by("-StartDate")
    person_education_list = person_info.education_set.all().order_by("-StartDate")
    #person_technology_db_request = get_list_or_404(Technology.objects.filter(skill__curriculum__id = 1).values_list('HtmlCode')) # pylint: disable=E1101
    #person_technology_list = [x[0] for x in person_technology_db_request]
    #person_skill_list = person_info.skill_set.all()
    technology_list = Technology.objects.values('Name','HtmlCode')

    
    # We put all the techno logos in a dict from Technology table
    technology_dict = {}
    for x in technology_list:
        technology_dict[x['Name']] = x['HtmlCode']



    context = {
                "person": person_info,
                "exps_list": person_experiences_list,
                "educ_list": person_education_list,
                #"techno_list": person_technology_list,
                #"skill_list": person_skill_list,
                "technology_dict" : technology_dict,

    }
    return render(request, "cv/index.html", context)


