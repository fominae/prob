# Generated by Django 4.2.5 on 2023-12-25 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monolit', '0003_profile_basket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='username',
            new_name='user',
        ),
    ]