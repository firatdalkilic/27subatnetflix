# Generated by Django 4.1.1 on 2023-08-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kullanici',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
                ('soyisim', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100, null=True)),
                ('resim', models.FileField(upload_to='kullanicilar/', verbose_name='Profil Resmi')),
                ('tel', models.IntegerField(default=0)),
                ('dogum', models.DateField()),
                ('olusturulma_tarih', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
