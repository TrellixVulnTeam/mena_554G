# Generated by Django 4.0 on 2021-12-10 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kabinet', '0006_profile_alter_adres_data_start_alter_adres_data_stop_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='image/avatar/', verbose_name='Миниатюра'),
        ),
    ]
