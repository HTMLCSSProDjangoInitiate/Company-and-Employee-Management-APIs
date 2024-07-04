# Generated by Django 5.0.6 on 2024-07-02 13:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('about', models.TextField()),
                ('position', models.CharField(choices=[('Manager', 'manager'), ('Software Developer', 'SD'), ('Project Leader', 'PL')], max_length=100)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.company')),
            ],
        ),
    ]