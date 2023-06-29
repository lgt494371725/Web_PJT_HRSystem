# Generated by Django 3.2 on 2023-06-28 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MCareerLevel',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False, verbose_name='キャリアレベルid')),
                ('name', models.CharField(max_length=64, verbose_name='キャリアレベルの名称')),
                ('level', models.SmallIntegerField(verbose_name='キャリアレベル')),
            ],
        ),
        migrations.CreateModel(
            name='MDte',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='部門id')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='部門名')),
            ],
        ),
        migrations.CreateModel(
            name='MHomeoffice',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='ホームオフィスid')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='ホームオフィス名')),
            ],
        ),
        migrations.CreateModel(
            name='MIndustry',
            fields=[
                ('id', models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='インダストリid')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='インダストリ名')),
            ],
        ),
        migrations.CreateModel(
            name='MSkill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='スキルid')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='スキル名')),
            ],
        ),
        migrations.CreateModel(
            name='MSkillCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='スキルカテゴリid')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='スキルカテゴリ名前')),
            ],
        ),
        migrations.CreateModel(
            name='TAccount',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='アカウントid')),
                ('name', models.CharField(max_length=64, verbose_name='アカウント名')),
                ('description', models.TextField(max_length=1024, null=True, verbose_name='アカウント説明')),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taccount_industry', to='hr_tool.mindustry', verbose_name='インダストリ')),
            ],
        ),
        migrations.CreateModel(
            name='TTraining',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='トレーニングid')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='トレーニング名')),
                ('description', models.TextField(max_length=1024, verbose_name='トレーニング説明')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='社員番号')),
                ('last_name', models.CharField(max_length=32, verbose_name='姓')),
                ('first_name', models.CharField(max_length=32, verbose_name='名')),
                ('middle_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='ミドルネーム')),
                ('birthday', models.DateField(verbose_name='誕生日')),
                ('is_hr', models.BooleanField()),
                ('join_of', models.DateField(verbose_name='入社日')),
                ('career_level', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_cl', to='hr_tool.mcareerlevel', verbose_name='キャリアレベル')),
                ('dte', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_dte', to='hr_tool.mdte')),
                ('homeoffice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_homeoffice', to='hr_tool.mhomeoffice')),
            ],
            options={
                'db_table': 't_employee',
            },
        ),
        migrations.CreateModel(
            name='TTrainingExp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='トレーニング経験id')),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='t_training_exp_eid', to='hr_tool.user', verbose_name='社員番号')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='t_training_exp_training', to='hr_tool.ttraining', verbose_name='トレーニング')),
            ],
        ),
        migrations.CreateModel(
            name='TSkill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='スキル経験id')),
                ('updated_date', models.DateField(verbose_name='更新日')),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='t_skill_exp_eid', to='hr_tool.user', verbose_name='社員番号')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='t_skill_m_skill', to='hr_tool.mskill', verbose_name='スキル')),
            ],
        ),
        migrations.CreateModel(
            name='TProject',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='プロジェクトid')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='プロジェクト名')),
                ('description', models.TextField(max_length=1024, verbose_name='プロジェクト説明')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tproject_account', to='hr_tool.taccount', verbose_name='アカウント')),
            ],
        ),
        migrations.CreateModel(
            name='TPreCareer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='入社前経験id')),
                ('role', models.CharField(max_length=64, verbose_name='ロール')),
                ('start_date', models.DateField(verbose_name='開始日')),
                ('end_date', models.DateField(verbose_name='終了日')),
                ('exp_detail', models.TextField(max_length=512, verbose_name='経験詳細')),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='t_pre_career_eid', to='hr_tool.user', verbose_name='社員番号')),
            ],
        ),
        migrations.CreateModel(
            name='TAssignExp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='アサイン経験id')),
                ('role', models.CharField(max_length=64, verbose_name='ロール')),
                ('start_date', models.DateField(verbose_name='開始日')),
                ('end_date', models.DateField(verbose_name='終了日')),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='t_assign_exp_eid', to='hr_tool.user', verbose_name='社員番号')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='t_assign_exp_project', to='hr_tool.tproject', verbose_name='プロジェクト')),
            ],
        ),
        migrations.AddField(
            model_name='mskill',
            name='skill_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mkill_mkillcategory', to='hr_tool.mskillcategory'),
        ),
    ]
