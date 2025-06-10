# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Appointments(models.Model):
    appointment_id = models.UUIDField(primary_key=True)
    pet = models.ForeignKey('Pets', models.DO_NOTHING)
    doctor = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    appointment_type = models.TextField()
    notes = models.TextField(blank=True, null=True)
    status = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointments'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BeautyServiceHistory(models.Model):
    service_id = models.UUIDField(primary_key=True)
    service_type = models.CharField(max_length=100)
    service_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    pet = models.ForeignKey('Pets', models.DO_NOTHING)
    staff = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beauty_service_history'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HotelServiceHistory(models.Model):
    stay_id = models.UUIDField(primary_key=True)
    check_in = models.DateField()
    check_out = models.DateField()
    room_number = models.CharField(max_length=10)
    special_care = models.TextField(blank=True, null=True)
    pet = models.ForeignKey('Pets', models.DO_NOTHING)
    staff = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel_service_history'


class MedicalHistory(models.Model):
    record_id = models.UUIDField(primary_key=True)
    diagnosis = models.TextField()
    treatment = models.TextField()
    notes = models.TextField(blank=True, null=True)
    date_of_visit = models.DateField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    pet = models.ForeignKey('Pets', models.DO_NOTHING)
    vet = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_history'


class NutritionPlan(models.Model):
    plan_id = models.UUIDField(primary_key=True)
    food_type = models.TextField()
    portion = models.TextField()
    special_notes = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)
    pet = models.ForeignKey('Pets', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'nutrition_plan'


class Pets(models.Model):
    pet_id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50)
    birthdate = models.DateField()
    color = models.CharField(max_length=30, blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    owner = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pets'


class Users(models.Model):
    user_id = models.UUIDField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.TextField()
    role = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class VaccinationHistory(models.Model):
    vaccination_id = models.UUIDField(primary_key=True)
    vaccine_name = models.CharField(max_length=100)
    date_given = models.DateField()
    next_due = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    pet = models.ForeignKey(Pets, models.DO_NOTHING)
    vet = models.ForeignKey(Users, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vaccination_history'
