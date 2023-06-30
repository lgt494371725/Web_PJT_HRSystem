# Generated by Django 3.2 on 2023-06-30 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_tool', '0002_auto_20230628_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcareerlevel',
            name='id',
            field=models.SmallAutoField(primary_key=True, serialize=False, verbose_name='マネジメントレベルid'),
        ),
        migrations.AlterField(
            model_name='mcareerlevel',
            name='level',
            field=models.SmallIntegerField(verbose_name='マネジメントレベル'),
        ),
        migrations.AlterField(
            model_name='mcareerlevel',
            name='name',
            field=models.CharField(max_length=64, verbose_name='マネジメントレベルの名称'),
        ),
        migrations.AlterField(
            model_name='user',
            name='career_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_cl', to='hr_tool.mcareerlevel', verbose_name='マネジメントレベル'),
        ),
    ]
