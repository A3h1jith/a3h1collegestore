# Generated by Django 4.2.1 on 2023-05-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_order_materials_provide_alter_order_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], max_length=25),
        ),
    ]
