# Generated by Django 4.1.6 on 2023-02-13 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raghad', '0003_alter_client_email_alter_sign_up_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=700),
        ),
    ]
