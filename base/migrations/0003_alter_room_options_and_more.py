# Generated by Django 4.0.2 on 2022-08-19 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.RenameField(
            model_name='room',
            old_name='desctription',
            new_name='description',
        ),
    ]