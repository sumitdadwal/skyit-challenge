# Generated by Django 3.2.10 on 2022-02-01 20:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('firstcarapi', '0002_auto_20220201_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='updated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='car',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='UpdatedMileage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstcarapi.car')),
            ],
        ),
    ]
