# Generated by Django 4.0.6 on 2022-11-24 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tg_bot', '0007_alter_course_ctg_alter_sub_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub',
            name='course',
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tg_bot.course')),
            ],
        ),
        migrations.AddField(
            model_name='sub',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tg_bot.teachers'),
        ),
    ]
