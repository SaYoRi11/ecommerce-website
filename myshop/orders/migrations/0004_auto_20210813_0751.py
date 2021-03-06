# Generated by Django 3.2.6 on 2021-08-13 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='braintree_id',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='order',
            name='size',
            field=models.CharField(choices=[('M', 'Medium (M)'), ('L', 'Large (L)'), ('XL', 'Extra Large (XL)'), ('XXL', 'Extra Extra Large (XXL)')], default='XL', max_length=20),
        ),
    ]
