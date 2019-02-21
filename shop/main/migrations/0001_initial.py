# Generated by Django 2.1.1 on 2019-02-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(blank=True, upload_to='product_images')),
                ('cost', models.IntegerField()),
            ],
        ),
    ]
