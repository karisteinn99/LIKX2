# Generated by Django 4.0.4 on 2022-05-05 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('department_name', models.CharField(max_length=255)),
                ('semester_name', models.CharField(max_length=255)),
                ('semester_type', models.CharField(max_length=255, null=True)),
                ('ects', models.IntegerField()),
                ('description', models.TextField(null=True)),
                ('teaching_language', models.CharField(max_length=255)),
                ('has_prerequisite', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Semesters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='CourseSemester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseselect.course')),
                ('semesterid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseselect.semesters')),
            ],
        ),
        migrations.CreateModel(
            name='CourseHasPrerequisite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prereq_course_code', models.CharField(max_length=255)),
                ('parallel_enrollment', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id1', to='courseselect.course')),
                ('prereq_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id2', to='courseselect.course')),
            ],
        ),
    ]
