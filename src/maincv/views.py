from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.urls import reverse
from django.forms import formset_factory
import smtplib
import re

from django.core.mail import EmailMessage

from .models import Experience
from .forms import ContactForm
#from .forms import CurriculumModelForm, ExperienceModelForm, SkillModelForm,ExperienceModelFormSet, EducationModelFormSet, SkillModelFormSet, SkillModelFormSetHelper

# Create your views here.

def home(request):

    form = ContactForm(request.POST or None)
    context = {
                "form": form,

    }
    return render(request, "cv/index.html", context)


def cv(request):
    person = get_object_or_404(User, id=1)
    experiences = person.profile.experience_set.all().order_by("-startDate")
    educations = person.profile.education_set.all().order_by("-startDate")

    context = {
            "person": person,
            "experiences": experiences,
            "educations": educations,
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
            except smtplib.SMTPException as e:
                response['status'] = "failed"
                print(e)
                print(email)
            
            return JsonResponse(response)

        else:
            print("form is not valid")
            errors_dic = form.errors.as_data()
            f = {x:re.sub(r"[^\w\s\.]",'',str(errors_dic[x][0])) for x in errors_dic}
            print(f)
            response['status'] = "form error"
            response['errors'] = f 

            return JsonResponse(response)
        

