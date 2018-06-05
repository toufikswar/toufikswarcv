from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.forms import formset_factory
import smtplib
import re

from django.core.mail import EmailMessage

from .models import Curriculum, Experience, Technology
from .forms import ContactForm
#from .forms import CurriculumModelForm, ExperienceModelForm, SkillModelForm,ExperienceModelFormSet, EducationModelFormSet, SkillModelFormSet, SkillModelFormSetHelper

# Create your views here.

def home(request):

    form = ContactForm(request.POST or None)
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
                "form": form,

    }
    return render(request, "cv/index.html", context)


def cv(request):
    person_info = get_object_or_404(Curriculum, id=1)
    person_experiences_list = person_info.experience_set.all().order_by("-StartDate")
    person_education_list = person_info.education_set.all().order_by("-StartDate")

    technology_list = Technology.objects.values('Name','HtmlCode')

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

    return render(request, "cv/myonlinecv.html", context)

def contact(request):
    if request.is_ajax():
        response = {}
        form = ContactForm(request.POST)
        if form.is_valid():
            data = {}

            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            email = EmailMessage(
                subject=full_name + " sent a message",
                body=message,
                from_email='toufik.swar@outlook.fr',
                to=['toufik.swar@outlook.fr',],
            )
        
            email.content_subtype = "html"

            try:
                email.send(fail_silently=False)
                response['status'] = "sent"
            except:
                response['status'] = "failed"
                print(response)
            
            return JsonResponse(response)

        else:
            print("form is not valid")
            errors_dic = form.errors.as_data()
            f = {x:re.sub(r"[^\w\s\.]",'',str(errors_dic[x][0])) for x in errors_dic}
            print(f)
            response['status'] = "form error"
            response['errors'] = f 

            return JsonResponse(response)
        

        