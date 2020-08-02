# Generated by Django 3.0.8 on 2020-07-22 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20200719_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Question')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Answer')),
            ],
        ),
    ]
