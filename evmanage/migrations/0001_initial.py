# Generated by Django 3.0.5 on 2020-06-05 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('E_id', models.CharField(max_length=100)),
                ('E_name', models.CharField(max_length=100)),
                ('E_type', models.CharField(max_length=100)),
                ('E_location', models.CharField(max_length=100)),
                ('E_time', models.TimeField()),
                ('E_coordinator_no', models.CharField(max_length=100)),
                ('E_image', models.ImageField(default='static/image1.jpg', upload_to='pics')),
            ],
            options={
                'db_table': 'Event',
            },
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USN', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=30)),
                ('sem', models.IntegerField(max_length=5)),
                ('college', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(default=0, max_length=100)),
                ('payment_mode', models.CharField(default=0, max_length=100)),
                ('account_no', models.CharField(default=0, max_length=100)),
                ('cvv', models.IntegerField(default=0)),
                ('exp_date', models.DateField(default=1987)),
                ('E_id', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT, to='evmanage.Event')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]