# Generated by Django 3.2.5 on 2021-10-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loto', '0010_testtable_t_jour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testtable',
            name='t_tirage',
            field=models.CharField(db_column='Tirages', max_length=300, unique=True),
        ),
    ]