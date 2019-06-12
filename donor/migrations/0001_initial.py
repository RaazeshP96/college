# Generated by Django 2.2.1 on 2019-06-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('blood_group', models.CharField(choices=[('A +ve', 'A +ve'), ('B +ve', 'B +ve'), ('AB +ve', 'AB +ve'), ('O +ve', 'O +ve'), ('A -ve', 'A -ve'), ('B -ve', 'B -ve'), ('AB -ve', 'AB -ve'), ('O -ve', 'O -ve')], max_length=7)),
                ('contact_no', models.CharField(max_length=10)),
            ],
        ),
    ]