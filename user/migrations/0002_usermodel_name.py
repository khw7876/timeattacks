# Generated by Django 3.2.5 on 2022-06-17 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='name',
            field=models.CharField(default=1, max_length=128, verbose_name='이름'),
            preserve_default=False,
        ),
    ]
