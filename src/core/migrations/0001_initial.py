# Generated by Django 4.0.4 on 2022-05-09 12:31

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
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='City')),
            ],
        ),
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.TextField(verbose_name='Adress')),
                ('car', models.CharField(max_length=40)),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.PositiveIntegerField(help_text='Put amount in hrn', verbose_name='Price')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('service_arrival_time', models.DateTimeField(verbose_name='Arrival')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('status', models.CharField(choices=[('D', 'Done'), ('N', 'Not Done')], default='N', max_length=2)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.city')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
