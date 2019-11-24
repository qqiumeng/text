# Generated by Django 2.0 on 2019-08-10 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_auto_20190810_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charge_manage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_cellectable', models.CharField(max_length=20)),
                ('charge_amount', models.FloatField()),
                ('exam_date', models.DateTimeField(auto_now_add=True)),
                ('all_charge', models.FloatField()),
            ],
        ),
    ]