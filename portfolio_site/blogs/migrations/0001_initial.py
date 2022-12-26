# Generated by Django 4.1.4 on 2022-12-26 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_heading', models.CharField(max_length=100)),
                ('blog_text', models.CharField(max_length=1000)),
                ('date_published', models.DateTimeField(verbose_name='date published')),
                ('images', models.CharField(max_length=500)),
            ],
        ),
    ]