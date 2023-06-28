# Generated by Django 4.2.2 on 2023-06-25 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelTestRandomField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RenameModel(
            old_name='MyModel',
            new_name='ModelwithTupleTuple',
        ),
    ]