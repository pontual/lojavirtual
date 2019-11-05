# Generated by Django 2.2.7 on 2019-11-05 15:26

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=64)),
                ('ean', models.CharField(blank=True, max_length=40)),
                ('caixa_grande', models.IntegerField(blank=True, null=True)),
                ('caixa_pequena', models.IntegerField(blank=True, null=True)),
                ('ncm', models.CharField(blank=True, max_length=20)),
                ('ii', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=6)),
                ('ativo', models.BooleanField(default=True)),
                ('origem', models.CharField(blank=True, max_length=78)),
                ('cest', models.CharField(blank=True, max_length=40)),
                ('icms', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=6)),
                ('ipi', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=6)),
                ('preco_padrao', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('observacoes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['codigo'],
            },
        ),
    ]
