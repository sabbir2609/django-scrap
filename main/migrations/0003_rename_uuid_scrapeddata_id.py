# Generated by Django 5.1.1 on 2024-10-02 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_scrapeddata_created_at_alter_scrapeddata_data_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scrapeddata',
            old_name='uuid',
            new_name='id',
        ),
    ]
