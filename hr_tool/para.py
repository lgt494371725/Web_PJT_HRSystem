from .models import *


# key:[model, Field]
mapping_dict = {'birth_year':[User, User.birthday], #
                'birth_month': [User, User.birthday],  #
                'birth_year_month': [User, User.birthday],  #
                'career_level': [User,User.career_level],  # join
                'home_office': [User, User.homeoffice],  # join
                'DTE': [User, User.dte],  # join
                'skill': [TSkill, TSkill.skill],  # join
                'join_year': [User, User.join_of], #  
                'join_month': [User, User.join_of], #
                'join_year_month': [User, User.join_of], #
                'assign_role': [TAssignExp, TAssignExp.role],  # join
                'assign_experience': [TAssignExp, None],
                'assign_industry': [TAccount, TAccount.industry]}  # join