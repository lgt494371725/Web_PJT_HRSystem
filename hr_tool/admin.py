from django.contrib import admin

from .models import (MCareerLevel, MDte, MHomeoffice, MIndustry, MSkill,
                     MSkillCategory, TAccount, TAssignExp, TPreCareer,
                     TProject, TSkill, TTraining, TTrainingExp, User)

admin.site.register(MCareerLevel)
admin.site.register(MDte)
admin.site.register(MHomeoffice)
admin.site.register(MIndustry)
admin.site.register(MSkill)
admin.site.register(MSkillCategory)
admin.site.register(TAccount)
admin.site.register(TAssignExp)
admin.site.register(TPreCareer)
admin.site.register(TProject)
admin.site.register(TSkill)
admin.site.register(TTraining)
admin.site.register(TTrainingExp)
admin.site.register(User)
