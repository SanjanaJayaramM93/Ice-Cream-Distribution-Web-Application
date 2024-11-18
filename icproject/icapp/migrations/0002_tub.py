# Generated by Django 3.2.18 on 2023-03-23 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('icapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tub_flavour', models.CharField(max_length=255)),
                ('tub_size', models.IntegerField()),
                ('tub_vegan', models.BooleanField()),
                ('tub_gluten', models.BooleanField()),
                ('tub_image', models.ImageField(upload_to='tubs')),
                ('tub_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='icapp.store')),
            ],
        ),
    ]
