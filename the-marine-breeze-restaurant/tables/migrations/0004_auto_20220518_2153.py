# Generated by Django 3.2 on 2022-05-18 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0003_alter_tables_table_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tables',
            name='table_date',
        ),
        migrations.RemoveField(
            model_name='tables',
            name='table_end',
        ),
        migrations.RemoveField(
            model_name='tables',
            name='table_start',
        ),
        migrations.AlterField(
            model_name='tables',
            name='table_no',
            field=models.CharField(choices=[('1', 'ONE'), ('2', 'TWO'), ('3', 'THREE'), ('4', 'FOUR')], max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='tables',
            name='table_status',
            field=models.CharField(choices=[('AVL', 'ACTIVE'), ('BKD', 'COMPLETE'), ('OFF', 'CANCELLED')], default='Active', max_length=10),
        ),
    ]
