# Generated by Django 4.0.1 on 2022-04-17 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=200)),
                ('manufacturer', models.CharField(max_length=200)),
                ('cost', models.IntegerField(max_length=8)),
            ],
            options={
                'db_table': 'Cars',
            },
        ),
    ]
