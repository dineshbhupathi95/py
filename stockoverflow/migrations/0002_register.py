# Generated by Django 2.1.5 on 2019-02-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockoverflow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.IntegerField(max_length=10)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
