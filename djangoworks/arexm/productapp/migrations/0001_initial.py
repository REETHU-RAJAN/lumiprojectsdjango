# Generated by Django 4.2.5 on 2023-12-19 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productapp.category')),
            ],
        ),
    ]
