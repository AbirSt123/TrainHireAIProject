# Generated by Django 5.1.4 on 2025-02-07 23:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_remove_user_mdp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='entretien',
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='entretien',
        ),
        migrations.RemoveField(
            model_name='reponse',
            name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='contenu',
            new_name='question_text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='type',
        ),
        migrations.AddField(
            model_name='question',
            name='question_order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('transcription', models.TextField()),
                ('facial_expression_data', models.JSONField(blank=True, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='common.question')),
            ],
        ),
        migrations.CreateModel(
            name='InterviewSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='session',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='common.interviewsession'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Entretien',
        ),
        migrations.DeleteModel(
            name='Rapport',
        ),
        migrations.DeleteModel(
            name='Reponse',
        ),
    ]
