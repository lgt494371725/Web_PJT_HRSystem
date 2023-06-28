from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# マスタテーブル
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
    id = models.SmallAutoField('キャリアレベルid', primary_key=True)
    name = models.CharField('キャリアレベルの名称', max_length=64)
    level = models.SmallIntegerField('キャリアレベル')

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


# トランザクションテーブル
class User(AbstractBaseUser):
    class Meta:
        db_table = 't_employee'

    id = models.CharField('社員番号', max_length=8, primary_key=True)
    last_name = models.CharField('姓', max_length=32)
    first_name = models.CharField('名', max_length=32)
    middle_name = models.CharField('ミドルネーム', max_length=32, blank=True, null=True)
    birthday = models.DateField('誕生日')

    career_level = models.ForeignKey(MCareerLevel, verbose_name='キャリアレベル', on_delete=models.PROTECT, to_field='id', related_name='user_cl')
    is_hr = models.BooleanField()
    join_of = models.DateField('入社日')
    homeoffice = models.ForeignKey(MHomeoffice, on_delete=models.PROTECT, to_field='id', related_name='user_homeoffice')
    dte = models.ForeignKey(MDte, on_delete=models.PROTECT, to_field='id', related_name='user_dte')

    USERNAME_FIELD = 'id'

    def __str__(self):
        return f'{self.last_name} {self.first_name} ({self.id})'

    # TODO: 認証機能
    # password =


class TPreCareer(models.Model):
    id = models.AutoField('入社前経験id', primary_key=True)
    eid = models.ForeignKey(User, verbose_name='社員番号', on_delete=models.CASCADE, to_field='id', related_name='t_pre_career_eid')
    role = models.CharField('ロール', max_length=64)
    start_date = models.DateField('開始日')
    end_date = models.DateField('終了日')
    exp_detail = models.TextField('経験詳細', max_length=512)

    def __str__(self):
        return self.id


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
    training_id = models.ForeignKey(TTraining, verbose_name='トレーニング', on_delete=models.CASCADE, to_field='id', related_name='t_training_exp_training')
    eid = models.ForeignKey(User, verbose_name='社員番号', on_delete=models.CASCADE, to_field='id', related_name='t_training_exp_eid')

    def __str__(self):
        return f'{self.eid.last_name} の {self.training_id.name}'


class TSkill(models.Model):
    id = models.AutoField('スキル経験id', primary_key=True)
    eid = models.ForeignKey(User, verbose_name='社員番号', on_delete=models.CASCADE, to_field='id', related_name='t_skill_exp_eid')
    skill = models.ForeignKey(MSkill, verbose_name='スキル', on_delete=models.CASCADE, to_field='id', related_name='t_skill_m_skill')
    updated_date = models.DateField('更新日')

    def __str__(self):
        return f'{self.eid.last_name} の {self.skill.name}'
