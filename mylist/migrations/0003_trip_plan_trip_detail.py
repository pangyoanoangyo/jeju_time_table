# Generated by Django 4.1.3 on 2023-02-16 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mylist', '0002_profile_add'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('content', models.TextField(null=True)),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
                ('location_tx', models.TextField()),
                ('location_rx', models.TextField()),
                ('hotel', models.TextField()),
                ('memo', models.TextField()),
                ('details', models.TextField()),
                ('etc', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Trip_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('content', models.TextField(null=True)),
                ('t08', models.TextField()),
                ('t09', models.TextField()),
                ('t10', models.TextField()),
                ('t11', models.TextField()),
                ('t12', models.TextField()),
                ('t13', models.TextField()),
                ('t14', models.TextField()),
                ('t15', models.TextField()),
                ('t16', models.TextField()),
                ('t17', models.TextField()),
                ('t18', models.TextField()),
                ('t19', models.TextField()),
                ('t20', models.TextField()),
                ('t21', models.TextField()),
                ('t22', models.TextField()),
                ('t23', models.TextField()),
                ('t24', models.TextField()),
                ('stert_day', models.DateField()),
                ('end_day', models.DateField()),
                ('location', models.TextField()),
                ('memo', models.TextField()),
                ('details', models.TextField()),
                ('etc', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mylist.trip_plan')),
            ],
        ),
    ]
