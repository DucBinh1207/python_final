# Generated by Django 4.0.3 on 2022-06-21 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkingmanage', '0011_alter_parkinglog_vehicle_alter_vehicle_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='parkingmanage.user'),
        ),
    ]
