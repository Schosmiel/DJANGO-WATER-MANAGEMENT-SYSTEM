# Generated by Django 2.2.13 on 2023-03-31 08:00

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mapbox_location_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(max_length=6, unique=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('disabled', 'Disabled'), ('active', 'Active'), ('deleted', 'Deleted'), ('blocked', 'Blocked'), ('completed', 'Completed')], max_length=10)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_user', to=settings.AUTH_USER_MODEL)),
                ('updated_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=132)),
                ('address', models.CharField(max_length=64)),
                ('sexe', models.CharField(choices=[('M', 'Male'), ('F', 'Feminin')], max_length=1)),
                ('city', models.CharField(max_length=32)),
                ('zip_code', models.CharField(max_length=16)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('disabled', 'Disabled'), ('active', 'Active'), ('deleted', 'Deleted'), ('blocked', 'Blocked'), ('completed', 'Completed')], max_length=10)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by_client_related', to=settings.AUTH_USER_MODEL)),
                ('updated_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_by_client_related', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Livreur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=132)),
                ('addresse', models.CharField(max_length=64)),
                ('sexe', models.CharField(choices=[('M', 'Male'), ('F', 'Feminin')], max_length=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('disabled', 'Disabled'), ('active', 'Active'), ('deleted', 'Deleted'), ('blocked', 'Blocked'), ('completed', 'Completed')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserCoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gain_type', models.CharField(choices=[('event', 'Event'), ('others', 'Others')], max_length=6)),
                ('gain_coin', models.PositiveIntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('disabled', 'Disabled'), ('active', 'Active'), ('deleted', 'Deleted'), ('blocked', 'Blocked'), ('completed', 'Completed')], max_length=10)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usercoin_created_user', to=settings.AUTH_USER_MODEL)),
                ('updated_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usercoin_updated_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='event_category/')),
                ('stock', models.PositiveIntegerField()),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('volume', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('disponible', 'Disponible'), ('rupture', 'Rupture de stock'), ('endommagé', 'Endomagé')], max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Categorie')),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_created_user', to=settings.AUTH_USER_MODEL)),
                ('updated_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_updated_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Livraison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='event_category/')),
                ('price', models.PositiveIntegerField()),
                ('quantite', models.PositiveIntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('venue', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('heure', models.TimeField(auto_now_add=True)),
                ('location', mapbox_location_field.models.LocationField(map_attrs={})),
                ('volume', models.DecimalField(decimal_places=1, max_digits=10000)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('disabled', 'Disabled'), ('active', 'Active'), ('deleted', 'Deleted'), ('time out', 'Time Out'), ('completed', 'Completed'), ('cancel', 'Cancel')], max_length=10)),
                ('produit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.Produit')),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=132)),
                ('ville', models.CharField(max_length=32)),
                ('pays', models.CharField(max_length=32)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('disabled', 'Disabled'), ('active', 'Active'), ('deleted', 'Deleted'), ('blocked', 'Blocked'), ('completed', 'Completed')], max_length=10)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventwishlist_created_user', to=settings.AUTH_USER_MODEL)),
                ('produit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.Produit')),
                ('updated_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventwishlist_updated_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventJobCategoryLinking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('disabled', 'Disabled'), ('active', 'Active'), ('deleted', 'Deleted'), ('blocked', 'Blocked'), ('completed', 'Completed')], max_length=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Client')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Produit')),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='event_image/')),
                ('produit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.Produit')),
            ],
        ),
        migrations.CreateModel(
            name='EventAgenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_name', models.CharField(max_length=120)),
                ('speaker_name', models.CharField(max_length=120)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('venue_name', models.CharField(max_length=255)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Produit')),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbre_cmd', models.PositiveIntegerField()),
                ('prix', models.PositiveIntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('date_cmd', models.DateField(auto_now_add=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('livrée', 'Livrée'), ('en cours', 'En cours'), ('annulée', 'Annulée')], max_length=10)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.Client')),
                ('produit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.Produit')),
            ],
        ),
        migrations.CreateModel(
            name='EventMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attend_status', models.CharField(choices=[('waiting', 'Waiting'), ('attending', 'Attending'), ('completed', 'Completed'), ('absent', 'Absent'), ('cancelled', 'Cancelled')], max_length=10)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('disabled', 'Disabled'), ('active', 'Active'), ('deleted', 'Deleted'), ('blocked', 'Blocked'), ('completed', 'Completed')], max_length=10)),
                ('created_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventmember_created_user', to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Produit')),
                ('updated_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventmember_updated_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('event', 'user')},
            },
        ),
    ]
