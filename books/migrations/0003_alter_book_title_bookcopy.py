# Generated by Django 5.1.7 on 2025-03-08 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='BookCopy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_number', models.CharField(max_length=100, unique=True)),
                ('condition', models.CharField(choices=[('new', 'New'), ('good', 'Good'), ('fair', 'Fair'), ('poor', 'Poor')], default='good', max_length=100)),
                ('is_available', models.BooleanField(default=False)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookCopy', to='books.book')),
            ],
        ),
    ]
