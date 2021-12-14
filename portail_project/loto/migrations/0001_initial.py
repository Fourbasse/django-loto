# Generated by Django 3.2.5 on 2021-12-14 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EuromillionTirage',
            fields=[
                ('te_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('te_jour', models.CharField(db_column='Jour', max_length=300)),
                ('te_numeros', models.CharField(db_column='Numeros', max_length=300)),
                ('te_numeros_comp', models.CharField(db_column='Complementaire', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='LotoTirage',
            fields=[
                ('tl_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('tl_jour', models.CharField(db_column='Jour', max_length=300)),
                ('tl_tirage', models.CharField(db_column='Tirages', max_length=300)),
            ],
        ),
    ]
