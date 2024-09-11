# Generated by Django 5.0.4 on 2024-09-11 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('documentos', '0001_initial'),
        ('logos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.documento')),
                ('logo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logos.logo')),
            ],
        ),
    ]
