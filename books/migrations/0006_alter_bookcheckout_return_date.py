# Generated by Django 3.2.1 on 2021-05-10 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_bookcheckout_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcheckout',
            name='return_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
