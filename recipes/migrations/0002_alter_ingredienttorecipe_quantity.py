# Generated by Django 4.2.6 on 2023-12-02 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredienttorecipe',
            name='quantity',
            field=models.FloatField(blank=True, null=True),
        ),
    ]