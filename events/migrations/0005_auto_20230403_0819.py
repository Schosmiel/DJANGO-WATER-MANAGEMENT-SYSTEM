# Generated by Django 2.2.13 on 2023-04-03 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20230401_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='status',
            field=models.CharField(choices=[('disponible', 'Disponible'), ('rupture de stock', 'Rupture de stock'), ('emdommagé', 'Endommagé')], max_length=10),
        ),
        migrations.AlterField(
            model_name='client',
            name='status',
            field=models.CharField(choices=[('actif', 'actif'), ('perdu', 'perdu'), ('bloqué', 'bloqué')], max_length=10),
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='status',
            field=models.CharField(choices=[('actif', 'Actif'), ('perdu', 'perdu'), ('bloqué', 'Bloqué')], max_length=10),
        ),
        migrations.AlterField(
            model_name='livraison',
            name='start_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='livreur',
            name='status',
            field=models.CharField(choices=[('actif', 'Actif'), ('perdu', 'perdu'), ('bloqué', 'Bloqué')], max_length=10),
        ),
    ]
