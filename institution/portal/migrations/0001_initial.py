# Generated by Django 3.2.8 on 2021-11-18 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Constituency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='SubCounty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('county', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portal.county')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(blank=True, max_length=50, null=True)),
                ('disability', models.CharField(blank=True, max_length=50, null=True)),
                ('nationalid', models.IntegerField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('homeaddress', models.CharField(blank=True, max_length=50, null=True)),
                ('constituency', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.constituency')),
                ('county', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.county')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.gender')),
                ('maritalstatus', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.maritalstatus')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('nationality', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.nationality')),
                ('religion', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.religion')),
                ('subcounty', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.subcounty')),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('relationship', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portal.relationship')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portal.student')),
            ],
        ),
        migrations.CreateModel(
            name='Dependant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=50, null=True)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('relationship', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portal.relationship')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portal.student')),
            ],
        ),
        migrations.AddField(
            model_name='constituency',
            name='subcounty',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portal.subcounty'),
        ),
    ]