# Generated by Django 4.2.7 on 2024-01-10 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jounal', '0002_alter_dairyofclass_pupil_alter_class_unique_together'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Class',
            new_name='Grade',
        ),
    ]