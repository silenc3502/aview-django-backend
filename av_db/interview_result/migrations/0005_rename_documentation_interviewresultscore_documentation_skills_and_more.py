# Generated by Django 5.1.6 on 2025-05-20 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("interview_result", "0004_alter_interviewresultqas_question"),
    ]

    operations = [
        migrations.RenameField(
            model_name="interviewresultscore",
            old_name="documentation",
            new_name="documentation_skills",
        ),
        migrations.RenameField(
            model_name="interviewresultscore",
            old_name="decision_making",
            new_name="problem_solving",
        ),
        migrations.RenameField(
            model_name="interviewresultscore",
            old_name="development",
            new_name="technical_skills",
        ),
    ]
