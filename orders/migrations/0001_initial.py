# Generated by Django 2.0.3 on 2018-12-10 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Regular Pizza', 'Regular Pizza'), ('Sicilian Pizza', 'Sicilian Pizza'), ('Sub', 'Sub'), ('Pasta', 'Pasta'), ('Salad', 'Salad'), ('Dinner Platter', 'Dinner Platter')], max_length=64)),
                ('name', models.CharField(blank=True, max_length=64)),
                ('takesExtras', models.BooleanField()),
                ('isOneSize', models.BooleanField()),
                ('singleSizeCost', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('smallCost', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('largeCost', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='open', max_length=64)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('menuitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.MenuItem')),
                ('numberToppings', models.IntegerField()),
            ],
            bases=('orders.menuitem',),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.MenuItem'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order'),
        ),
        migrations.AddField(
            model_name='extra',
            name='forItems',
            field=models.ManyToManyField(limit_choices_to={'takesExtras': True}, related_name='extras', to='orders.MenuItem'),
        ),
    ]
