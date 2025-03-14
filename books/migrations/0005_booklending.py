# Generated by Django 5.1.7 on 2025-03-08 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_bookcopy_is_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookLending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrower_name', models.CharField(max_length=100)),
                ('borrower_email', models.EmailField(max_length=254)),
                ('borrowed_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField()),
                ('returned_date', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('returned', 'Returned'), ('overdue', 'Overdue')], max_length=50)),
                ('book_copy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookLending', to='books.bookcopy')),
            ],
        ),
    ]
