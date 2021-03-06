# Generated by Django 4.0.3 on 2022-05-12 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('interaction_idx', models.AutoField(primary_key=True, serialize=False)),
                ('interaction_type', models.CharField(choices=[('pause', 'pause'), ('redo', 'redo'), ('fast_forward', 'fast_forward'), ('rewind', 'rewind')], max_length=20)),
                ('interaction_time_real', models.CharField(max_length=20)),
                ('interaction_time_lecture', models.CharField(max_length=20)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interaction_lecture', to='subject.lecture')),
            ],
        ),
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('anlysis_idx', models.AutoField(primary_key=True, serialize=False)),
                ('concentration_rate', models.FloatField()),
                ('review_section', models.CharField(max_length=20)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analysis_lecture', to='subject.lecture')),
            ],
        ),
    ]
