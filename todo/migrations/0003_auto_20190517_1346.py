# Generated by Django 2.2.1 on 2019-05-17 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20190517_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(auto_now=True, verbose_name='마감일'),
        ),
    ]