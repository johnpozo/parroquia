# Generated by Django 2.1.3 on 2018-12-04 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='comunidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Comunidad'),
        ),
    ]
