# Generated by Django 4.0.1 on 2022-01-29 16:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverInfo',
            fields=[
                ('type', models.CharField(choices=[('FULLSIZE', 'Fullsize'), ('SUV', 'SUV'), ('MPV', 'MPV'), ('VAN', 'VAN')], default='FULLSIZE', max_length=10)),
                ('license_number', models.CharField(max_length=15, unique=True)),
                ('max_passengers', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)])),
                ('driver_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='driver', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('special_info', models.CharField(blank=True, max_length=200)),
                ('driver_status', models.CharField(choices=[('AVAILABLE', 'available'), ('CONFIRM', 'confirm'), ('START', 'start'), ('COMPLETE', 'complete')], default='AVAILABLE', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RideRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_passengers', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)])),
                ('required_time_arrival', models.DateTimeField()),
                ('departure_address', models.CharField(max_length=50)),
                ('destination_address', models.CharField(max_length=50)),
                ('canShare', models.BooleanField(default=False)),
                ('number_of_ride_owner_party', models.IntegerField()),
                ('vehicle_type', models.CharField(blank=True, choices=[('FULLSIZE', 'Fullsize'), ('SUV', 'SUV'), ('MPV', 'MPV'), ('VAN', 'VAN')], max_length=10)),
                ('special_rider_info', models.CharField(blank=True, max_length=200, null=True)),
                ('ride_status', models.CharField(choices=[('OPEN', 'open'), ('CONFIRMED', 'confirmed'), ('START', 'start'), ('COMPLETE', 'complete')], default='OPEN', max_length=20)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ride', to='rideShare.driverinfo')),
                ('ride_owner_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('search_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('destination_address', models.CharField(max_length=50)),
                ('earliest_acceptable_arrival_time', models.DateTimeField()),
                ('latest_acceptable_arrival_time', models.DateTimeField()),
                ('num_of_passengers_in_party', models.IntegerField()),
                ('search_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RideInfo',
            fields=[
                ('ride_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='rideShare.riderequest')),
                ('total_number_of_passengers', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RideSharer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ride_sharer_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RideOwner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ride_owner_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShareInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_ride_sharer_party', models.IntegerField(default=1)),
                ('ride_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rideShare.riderequest')),
                ('ride_sharer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ride_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rideShare.rideinfo')),
            ],
        ),
        migrations.CreateModel(
            name='RideConfirmed',
            fields=[
                ('ride_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='rideShare.riderequest')),
                ('driver_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rideShare.driverinfo')),
            ],
        ),
    ]
