# Generated by Django 3.0.5 on 2021-04-18 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0016_remove_teacherextra_company_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, null=True)),
                ('salary', models.IntegerField()),
                ('education', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
            ],
        ),
    ]
