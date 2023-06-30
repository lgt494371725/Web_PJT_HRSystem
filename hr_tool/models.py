from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# マスタテーブルjoin_month
class MSkillCategory(models.Model):
    id = models.AutoField('スキルカテゴリid', primary_key=True)
    name = models.CharField('スキルカテゴリ名前', max_length=64, unique=True)

    def __str__(self):
        return self.name


class MSkill(models.Model):
    id = models.AutoField('スキルid', primary_key=True)
    name = models.CharField('スキル名', max_length=64, unique=True)
    skill_category = models.ForeignKey(MSkillCategory, on_delete=models.CASCADE, to_field='id', related_name='mkill_mkillcategory')

    def __str__(self):
        return self.name


class MCareerLevel(models.Model):
    id = models.SmallAutoField('マネジメントレベルid', primary_key=True)
    name = models.CharField('マネジメントレベルの名称', max_length=64)
    level = models.SmallIntegerField('マネジメントレベル')

    def __str__(self):
        return f'{self.name} (ML: {self.level})'


class MIndustry(models.Model):
    id = models.SmallIntegerField('インダストリid', primary_key=True)
    name = models.CharField('インダストリ名', max_length=64, unique=True)

    def __str__(self):
        return self.name


class MDte(models.Model):
    id = models.SmallIntegerField('部門id', primary_key=True)
    name = models.CharField('部門名', max_length=64, unique=True)

    def __str__(self):
        return self.name


class MHomeoffice(models.Model):
    id = models.SmallIntegerField('ホームオフィスid', primary_key=True)
    name = models.CharField('ホームオフィス名', max_length=64, unique=True)

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):

    def create_user(self, id, password = None, **extra_fields):
        if not id:
            raise ValueError('Users must have an id')

        import datetime
        extra_fields.setdefault('birthday', datetime.date(1970, 1, 1))
        extra_fields['join_of'] = datetime.date.today()
        extra_fields['is_hr'] = False
        extra_fields['career_level'] = MCareerLevel.objects.filter(level=11)[0]

        print(extra_fields)

        user = self.model(
            id = id,
            **extra_fields
        )

        user.set_password(password)
        user.save(using = self.db)

        return user

    def create_hruser(self, id, password):
        user = self.create_user(
            id = id
        )
        user.set_password(password)
        user.is_hr = True
        user.save(using=self._db)
        return user

    def create_superuser(self, id,last_name, password):
        user = self.create_user(
            id = id,
            last_name = last_name,
        )
        user.set_password(password)
        user.is_hr = True
        user.save(using=self._db)
        return user

AUTH_USER_MODEL = 'hr_tool.User'

# トランザクションテーブル
class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 't_employee'

    id = models.CharField('社員番号', max_length=8, primary_key=True)
    last_name = models.CharField('姓', max_length=32)
    first_name = models.CharField('名', max_length=32)
    middle_name = models.CharField('ミドルネーム', max_length=32, blank=True, null=True)
    birthday = models.DateField('誕生日')

    career_level = models.ForeignKey(MCareerLevel, verbose_name='マネジメントレベル', on_delete=models.PROTECT, to_field='id', related_name='user_cl')
    is_hr = models.BooleanField()
    join_of = models.DateField('入社日')
    homeoffice = models.ForeignKey(MHomeoffice, on_delete=models.PROTECT, to_field='id', related_name='user_homeoffice')
    dte = models.ForeignKey(MDte, on_delete=models.PROTECT, to_field='id', related_name='user_dte')

    # TODO: 後で直す！！
    is_staff = models.BooleanField('is_staff', default=True)
    is_superuser = models.BooleanField('is_superuser', default=True)

    USERNAME_FIELD = 'id'

    def __str__(self):
        return f'{self.last_name} {self.first_name} ({self.id})'

    objects = UserManager()



class TPreCareer(models.Model):
    id = models.AutoField('入社前経験id', primary_key=True)
    eid = models.ForeignKey(User, verbose_name='社員番号', on_delete=models.CASCADE, to_field='id', related_name='t_precareer_eid')
    role = models.CharField('ロール', max_length=64)
    start_date = models.DateField('開始日')
    end_date = models.DateField('終了日')
    exp_detail = models.TextField('経験詳細', max_length=512)

    def __str__(self):
        return self.exp_detail


class TAccount(models.Model):
    id = models.IntegerField('アカウントid', primary_key=True)
    name = models.CharField('アカウント名', max_length=64)
    industry = models.ForeignKey(MIndustry, verbose_name='インダストリ', on_delete=models.CASCADE, to_field='id', related_name='taccount_industry')
    description = models.TextField('アカウント説明', max_length=1024, null=True)

    def __str__(self):
        return self.name


class TProject(models.Model):
    id = models.IntegerField('プロジェクトid', primary_key=True)
    name = models.CharField('プロジェクト名', max_length=64, unique=True)
    description = models.TextField('プロジェクト説明', max_length=1024)
    account = models.ForeignKey(TAccount, verbose_name='アカウント', on_delete=models.CASCADE, to_field='id', related_name='tproject_account')

    def __str__(self):
        return self.name


class TAssignExp(models.Model):
    id = models.AutoField('アサイン経験id', primary_key=True)
    eid = models.ForeignKey(User, verbose_name='社員番号', on_delete=models.CASCADE, to_field='id', related_name='t_assign_exp_eid')
    project = models.ForeignKey(TProject, verbose_name='プロジェクト', on_delete=models.CASCADE, to_field='id', related_name='t_assign_exp_project')
    role = models.CharField('ロール', max_length=64)
    start_date = models.DateField('開始日')
    end_date = models.DateField('終了日')

    def __str__(self):
        return f'{self.eid.last_name} の {self.project.name}'


class TTraining(models.Model):
    id = models.IntegerField('トレーニングid', primary_key=True)
    name = models.CharField('トレーニング名', max_length=64, unique=True)
    description = models.TextField('トレーニング説明', max_length=1024)

    def __str__(self):
        return self.name


class TTrainingExp(models.Model):
    id = models.AutoField('トレーニング経験id', primary_key=True)
    training = models.ForeignKey(TTraining, verbose_name='トレーニング', on_delete=models.CASCADE, to_field='id', related_name='t_training_exp_training')
    eid = models.ForeignKey(User, verbose_name='社員番号', on_delete=models.CASCADE, to_field='id', related_name='t_training_exp_eid')

    def __str__(self):
        return f'{self.eid.last_name} の {self.training.name}'


class TSkill(models.Model):
    id = models.AutoField('スキル経験id', primary_key=True)
    eid = models.ForeignKey(User, verbose_name='社員番号', on_delete=models.CASCADE, to_field='id', related_name='t_skill_exp_eid')
    skill = models.ForeignKey(MSkill, verbose_name='スキル', on_delete=models.CASCADE, to_field='id', related_name='t_skill_m_skill')
    updated_date = models.DateField('更新日')

    def __str__(self):
        return f'{self.eid.last_name} の {self.skill.name}'
