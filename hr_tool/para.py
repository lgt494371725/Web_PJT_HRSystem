from .models import *


# key:[model, Field]
mapping_dict = {'誕生日(年)':[User, User.birthday], #
                '誕生日(月)': [User, User.birthday],  #
                '誕生日(年月)': [User, User.birthday],  #
                'career level': [User,User.career_level_id],  # join
                'home_office': [User, User.homeoffice_id],  # join
                'DTE': [],
                'skill': [],
                '入社日(年)': [],
                '入社日(月)': [],
                '入社日(年月)': [],
                'assign role': [],
                'assign経験数': [],
                'assign industry': []}