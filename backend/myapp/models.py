from django.db import models
import uuid
from django.db import models

# trả về dạng bảng
class BaseModel(models.Model):
    class Meta:
        abstract = True

    def to_string(self):
        fields = [f"{field.name}={getattr(self, field.name)}" for field in self._meta.fields]
        return ', '.join(fields)

    def __str__(self):
        return self.to_string()

# Enum choices
class PetGender(models.TextChoices):
    MALE = 'M', 'Male'
    FEMALE = 'F', 'Female'
    


class AppointmentType(models.TextChoices):
    MEDICAL = 'medical', 'Medical'
    BEAUTY = 'beauty', 'Beauty'
    HOTEL = 'hotel', 'Hotel'



class AppointmentStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    COMPLETED = 'completed', 'Completed'
    CANCELLED = 'cancelled', 'Cancelled'
    CONFIRMED = 'confirmed', 'Confirmed'


class RoleChoices(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    STAFF = 'staff', 'Staff'
    OWNER = 'owner', 'Owner'
    VET = 'vet', 'Vet'


# Models
class User(BaseModel):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50)
    password = models.TextField()
    role = models.CharField(max_length=20, choices=RoleChoices.choices)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'users'
    
    


class Pet(BaseModel):
    pet_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=PetGender.choices)
    birthdate = models.DateField()
    color = models.CharField(max_length=30, blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'pets'

    


class Appointment(BaseModel):
    appointment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time = models.DateTimeField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    appointment_type = models.CharField(max_length=20, choices=AppointmentType.choices)
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('Chưa xác nhận', 'Chưa xác nhận'), ('Đã xác nhận', 'Đã xác nhận'), ('Đã khám', 'Đã khám'), ('Đã hủy', 'Đã hủy')],
        default='Chưa xác nhận'
    )
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'appointments'



class BeautyServiceHistory(BaseModel):
    service_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=100)
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    service_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'beauty_service_history'




class HotelServiceHistory(BaseModel):
    stay_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    room_number = models.CharField(max_length=10)
    special_care = models.TextField(blank=True, null=True)
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'hotel_service_history'
        


class MedicalHistory(BaseModel):
    record_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vet = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    diagnosis = models.TextField()
    treatment = models.TextField()
    notes = models.TextField(blank=True, null=True)
    date_of_visit = models.DateField()
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'medical_history'
        


class NutritionPlan(BaseModel):
    plan_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    food_type = models.TextField()
    portion = models.TextField()
    special_notes = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'nutrition_plan'
        



class VaccinationHistory(BaseModel):
    vaccination_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=100)
    date_given = models.DateField()
    next_due = models.DateField(blank=True, null=True)
    vet = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'vaccination_history'
        
