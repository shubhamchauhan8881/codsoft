# Generated by Django 4.2.4 on 2023-09-29 09:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('showroom', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_amount', models.IntegerField()),
                ('payment_status', models.CharField(default='not-initialized', max_length=100)),
                ('razorpay_payment_id', models.CharField(max_length=500)),
                ('razorpay_order_id', models.CharField(max_length=500)),
                ('razorpay_signature', models.CharField(max_length=600)),
                ('order_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
