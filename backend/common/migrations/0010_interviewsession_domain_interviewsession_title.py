# Generated by Django 5.1.4 on 2025-02-16 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_question_audio_file_alter_answer_audio_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewsession',
            name='domain',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='interviewsession',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
