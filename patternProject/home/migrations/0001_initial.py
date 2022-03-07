# Generated by Django 4.0.2 on 2022-03-07 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=10)),
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('lec_idx', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=20)),
                ('professor', models.CharField(max_length=10)),
                ('class_time', models.TimeField()),
                ('learing_time', models.TimeField()),
                ('completion', models.DateTimeField()),
                ('student', models.ForeignKey(db_column='student', on_delete=django.db.models.deletion.CASCADE, related_name='student', to='home.user')),
            ],
        ),
    ]