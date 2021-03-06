# Generated by Django 4.0.3 on 2022-04-17 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('document', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'app_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=4, max_digits=20)),
                ('bill_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'bill',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BillState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_condition', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'db_table': 'bill_state',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'brand',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CartCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 'cart_condition',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=3, unique=True)),
            ],
            options={
                'db_table': 'document_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PayMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_method', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'pay_method',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'db_table': 'phone',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photos', models.BinaryField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=13)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCalification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calification', models.IntegerField()),
            ],
            options={
                'db_table': 'product_calification',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ShippingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'shipping_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
            ],
            options={
                'db_table': 'shopping_cart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ShoppingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'shopping_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'user_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'variant',
                'managed': False,
            },
        ),
    ]
