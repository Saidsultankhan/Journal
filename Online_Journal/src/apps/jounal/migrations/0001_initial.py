# Generated by Django 4.2.7 on 2023-11-27 12:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField()),
                ('type', models.CharField(choices=[('a', 'a'), ('б', 'б'), ('в', 'в'), ('г', 'г'), ('д', 'д')], max_length=1)),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=255)),
                ('name_ru', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Parent',
                'verbose_name_plural': 'Parents',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=255)),
                ('name_ru', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
        migrations.CreateModel(
            name='SubjectTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_teacher_class', to='jounal.class')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_teacher_subject', to='jounal.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_teacher_teacher', to='jounal.teacher')),
            ],
            options={
                'verbose_name': 'Subject-Teacher',
                'verbose_name_plural': 'Subjects-Teachers',
            },
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=255)),
                ('name_ru', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255)),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_pupil', to='jounal.class')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pupil_parent', to='jounal.parent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pupil_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pupil',
                'verbose_name_plural': 'Pupils',
            },
        ),
        migrations.CreateModel(
            name='DairyOfClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('quarter', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dairy_of_class', to='jounal.class')),
                ('pupil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pupil', to='jounal.pupil')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='jounal.subject')),
            ],
            options={
                'verbose_name': 'DairyOfClass',
                'verbose_name_plural': 'DairiesOfClass_class',
            },
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_teacher', to='jounal.teacher'),
        ),
    ]
