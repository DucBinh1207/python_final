# Generated by Django 4.0.3 on 2022-06-21 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkingmanage', '0014_merge_20220621_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkingmanage.user'),
        ),
    ]
