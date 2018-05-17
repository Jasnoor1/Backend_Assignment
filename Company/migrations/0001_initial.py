# Generated by Django 2.0.5 on 2018-05-13 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('CompanyName', models.CharField(max_length=250)),
                ('Age', models.IntegerField()),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=10)),
                ('Zip', models.IntegerField()),
                ('Email', models.CharField(max_length=250)),
                ('Web', models.CharField(max_length=250)),
            ],
        ),
    ]
