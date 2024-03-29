# Generated by Django 3.2.8 on 2021-11-18 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constituency',
            name='subcounty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.subcounty'),
        ),
        migrations.AlterField(
            model_name='student',
            name='constituency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.constituency'),
        ),
        migrations.AlterField(
            model_name='student',
            name='county',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.county'),
        ),
        migrations.AlterField(
            model_name='student',
            name='maritalstatus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.maritalstatus'),
        ),
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.nationality'),
        ),
        migrations.AlterField(
            model_name='student',
            name='religion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.religion'),
        ),
        migrations.AlterField(
            model_name='student',
            name='subcounty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.subcounty'),
        ),
        migrations.AlterField(
            model_name='subcounty',
            name='county',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.county'),
        ),
    ]
