# Generated by Django 2.2 on 2020-12-04 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20201203_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
