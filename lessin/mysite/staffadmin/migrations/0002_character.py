# Generated by Django 2.0.6 on 2018-06-12 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
