# Generated by Django 5.0.6 on 2024-05-14 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_remove_event_staus_event_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='evaluated',
            field=models.ManyToManyField(related_name='evaluated_events', to='database.colaborator'),
        ),
    ]
