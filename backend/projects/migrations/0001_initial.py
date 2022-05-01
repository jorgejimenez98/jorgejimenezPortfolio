# Generated by Django 3.1.7 on 2022-05-01 16:36

from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('technologie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('repositoryUrl', models.URLField(default='', null=True)),
                ('technologies', models.ManyToManyField(related_name='projects', to='technologie.Technologie')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('image', models.ImageField(blank=True, null=True, upload_to=projects.models.uploadProjectItemPath)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectItems', to='projects.project')),
            ],
        ),
    ]
