# Generated by Django 2.1.1 on 2019-02-21 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_programm'),
    ]

    operations = [
        migrations.AddField(
            model_name='programm',
            name='category',
            field=models.CharField(choices=[('Стандартная', 'Стандартная'), ('Для похудения', 'Для похудения'), ('Для здорового образа жизни', 'Для здорового образа жизни'), ('Для вегетрианцев', 'Для вегетрианцев'), ('Detox программа', 'Detox программа')], default='Стандартная', max_length=100),
        ),
    ]
