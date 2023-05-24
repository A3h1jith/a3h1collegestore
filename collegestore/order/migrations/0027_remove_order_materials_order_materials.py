# Generated by Django 4.2.1 on 2023-05-23 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0001_initial'),
        ('order', '0026_delete_materials'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='materials',
        ),
        migrations.AddField(
            model_name='order',
            name='materials',
            field=models.ManyToManyField(to='credentials.material'),
        ),
    ]