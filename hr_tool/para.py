from .models import User, TSkill, TAssignExp, TAccount
from django.db.models.functions import ExtractYear, ExtractMonth
import pandas as pd
from django.db.models import Count


def cross_query(row, col, val):
    df = get_join_data()
    row_data = df[row] if row else None
    col_data = df[col] if col else None
    val_data = df[val] if val else None
    return row_data, col_data, val_data

def getYearMonth(model, key):
    year = list(model.objects.annotate(year_=ExtractYear(key)).values_list('year_', flat=True))
    month = list(model.objects.annotate(month_=ExtractMonth(key)).values_list('month_', flat=True))
    year_month = list(zip(year, month))
    return year_month


def get_join_data():
    """
    TSKill.eid -> t_skill_exp_eid
    get account from project and get project from TAssignExp -> t_assign_exp_eid__project__account
    """
    data = []
    users = User.objects.prefetch_related('t_skill_exp_eid', 't_assign_exp_eid').all()
    for user in users:
        user_skills = user.t_skill_exp_eid.all()
        user_assign_exps = user.t_assign_exp_eid.all()
        row = {
                'id': user.id,
                'management_level': 'ML'+str(user.career_level.level),
                'home_office': user.homeoffice.name,
                'DTE': user.dte.name,
            }
        if not user_skills:
            row['skill'] = None
            row['assign_role'] = None
            row['industry'] = None
            data.append(row)
        for skill in user_skills:
            row['skill'] = skill.skill.name
            if not user_assign_exps:
                row['assign_role'] = None
                row['industry'] = None
                data.append(row)
            for assign_exp in user_assign_exps:
                row['assign_role'] = assign_exp.role
                row['industry'] = assign_exp.project.account.industry
                data.append(row)

    df = pd.DataFrame(data)

    return df


def generate_mapping_dict():
    mapping_dict = {'birth_year':[User, list(User.objects.annotate(birth_year=ExtractYear('birthday')).values_list('birth_year', flat=True))],
                'birth_month': [User, list(User.objects.annotate(birth_month=ExtractMonth('birthday')).values_list('birth_month', flat=True))],  #
                'birth_year_month': [User, getYearMonth(User, 'birthday')],
                'management_level': [User, list(User.objects.values_list('career_level__level', flat=True))],
                'home_office': [User, list(User.objects.values_list('homeoffice__name', flat=True))],
                'DTE': [User, list(User.objects.values_list('dte__name', flat=True))],
                'join_year': [User, list(User.objects.annotate(join_year=ExtractYear('join_of')).values_list('join_year', flat=True))],
                'join_month': [User, list(User.objects.annotate(join_month=ExtractYear('join_of')).values_list('join_month', flat=True))],
                'join_year_month': [User, getYearMonth(User, 'join_of')],
                # multi join
                'skill': [TSkill, list(TSkill.objects.values_list('skill__name', flat=True))],  # join

                'num_projects': [TAssignExp, list(User.objects.annotate(num_projects=Count('t_assign_exp_eid__project', distinct=True)).values_list('num_projects', flat=True))],
                # 'assign_role': [TAssignExp, TAssignExp.role],  # join
                # 'assign_industry': [TAccount, TAccount.industry]
                }  # join
    return mapping_dict
