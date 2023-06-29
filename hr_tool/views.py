from django.shortcuts import render
from .models import MSkill,MSkillCategory,MCareerLevel,MIndustry,MHomeoffice,MDte
from django.http import JsonResponse
from django.forms.models import model_to_dict
# Create your views here.
def employee_list(request):
    return render(request, 'list.html')

def detail(request, pk):
    return render(request, 'detail.html')


def to_json(queryset):
   return [model_to_dict(r) for r in queryset]

def all_skills(request):
    ret = MSkill.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def all_skillCategories(request):
    ret = MSkillCategory.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def skills_in_categories(request,category_id):
    ret = MSkill.objects.filter(skill_category=category_id)
    return JsonResponse(to_json(ret),safe=False)

def all_careerLevels(request):
    ret = MCareerLevel.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def all_industries(request):
    ret = MIndustry.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def all_dtes(request):
    ret = MDte.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def all_homeoffices(request):
    ret = MHomeoffice.objects.all()
    return JsonResponse(to_json(ret),safe=False)

def dropdown_test(request):
   return render(request, 'dropdown_test.html')

