# Generated by Django 4.1.7 on 2023-06-15 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rules_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='highlightedIndices',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='example',
            name='rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examples', to='rules_app.rule'),
        ),
        migrations.AlterField(
            model_name='example',
            name='sentence',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='rule',
            name='rule',
            field=models.CharField(max_length=500),
        ),
    ]
