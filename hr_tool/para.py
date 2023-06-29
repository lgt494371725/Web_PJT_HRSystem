from .models import User, TSkill, TAssignExp, TAccount
from django.db.models.functions import ExtractYear, ExtractMonth
from django.db.models import Count


def getYearMonth(model, key):
    year = list(model.objects.annotate(year_=ExtractYear(key)).values_list('year_', flat=True))
    month = list(model.objects.annotate(month_=ExtractMonth(key)).values_list('month_', flat=True))
    year_month = list(zip(year, month))
    return year_month

# key:[model, Field]
mapping_dict = {'birth_year':[User, list(User.objects.annotate(birth_year=ExtractYear('birthday')).values_list('birth_year', flat=True))], 
                'birth_month': [User, list(User.objects.annotate(birth_month=ExtractMonth('birthday')).values_list('birth_month', flat=True))],  #
                'birth_year_month': [User, getYearMonth(User, 'birthday')],  #
                'career_level': [User, list(User.objects.values_list('career_level__name', flat=True))],  # join
                'home_office': [User, list(User.objects.values_list('homeoffice__name', flat=True))],  # join
                'DTE': [User, list(User.objects.values_list('dte__name', flat=True))],  # join
                'join_year': [User, list(User.objects.annotate(join_year=ExtractYear('join_of')).values_list('join_year', flat=True))], #  
                'join_month': [User, list(User.objects.annotate(join_month=ExtractYear('join_of')).values_list('join_month', flat=True))], #
                'join_year_month': [User, [User.objects.annotate(join_year=ExtractYear('join_of')).values_list('join_year', flat=True),
                                            User.objects.annotate(join_month=ExtractMonth('join_of')).values_list('join_month', flat=True)]], #
                'skill': [TSkill, list(TSkill.objects.values_list('skill__name', flat=True))],  # join
                'assign_role': [TAssignExp, TAssignExp.role],  # join
                'assign_experience': [TAssignExp, list(User.objects.annotate(projects=Count('t_assign_exp_eid__project', distinct=True)))],
                'assign_industry': [TAccount, TAccount.industry]}  # join


