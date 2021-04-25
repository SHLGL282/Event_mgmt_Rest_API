# Generated by Django 3.2 on 2021-04-25 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMaster',
            fields=[
                ('category_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('parent_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EventMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('cast', models.CharField(max_length=100)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_app.categorymaster')),
            ],
        ),
    ]
