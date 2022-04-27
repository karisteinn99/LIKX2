# Generated by Django 4.0.4 on 2022-04-26 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('ects', models.IntegerField()),
                ('slug', models.SlugField()),
                ('text', models.TextField()),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
