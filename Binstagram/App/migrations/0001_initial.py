# Generated by Django 5.0.7 on 2024-07-26 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='siteuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Password', models.CharField(max_length=255)),
            ],
        ),
    ]
