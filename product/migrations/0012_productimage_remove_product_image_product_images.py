# Generated by Django 5.0.3 on 2024-06-03 07:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_remove_product_image_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField(default='DAC17638-6429-4172-9AB7-35F4313C2394_1_105_c-removebg-preview (2).png', max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(to='product.productimage'),
        ),
    ]
