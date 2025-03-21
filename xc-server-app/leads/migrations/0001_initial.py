# Generated by Django 5.1 on 2024-08-14 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('company', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(choices=[('New', 'New'), ('Contacted', 'Contacted'), ('Qualified', 'Qualified'), ('Lost', 'Lost')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
