# Generated by Django 3.2.7 on 2021-09-25 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comments',
            field=models.TextField(default='S', max_length=100),
        ),
    ]