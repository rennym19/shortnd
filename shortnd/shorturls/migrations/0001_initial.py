# Generated by Django 3.0.4 on 2020-03-21 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.TextField()),
                ('key', models.CharField(max_length=7, null=True, unique=True)),
                ('title', models.CharField(max_length=255, null=True)),
                ('visit_count', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
