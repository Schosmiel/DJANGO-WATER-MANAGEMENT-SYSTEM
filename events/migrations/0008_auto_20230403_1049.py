# Generated by Django 2.2.13 on 2023-04-03 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20230403_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='status',
            field=models.CharField(choices=[('actif', 'actif'), ('inactif', 'Inactif'), ('bloqué', 'bloqué')], max_length=10),
        ),
        migrations.AlterField(
            model_name='livraison',
            name='status',
            field=models.CharField(choices=[('en cours', 'En cours'), ('terminé', 'Terminé'), ('annuler', 'Annuler')], default='en cours', max_length=10),
        ),
        migrations.AlterField(
            model_name='livreur',
            name='status',
            field=models.CharField(choices=[('actif', 'Actif'), ('inactif', 'Inactif'), ('bloqué', 'Bloqué')], max_length=10),
        ),
    ]
