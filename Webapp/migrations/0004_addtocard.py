# Generated by Django 2.2.16 on 2020-10-31 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0003_products_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddtoCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
