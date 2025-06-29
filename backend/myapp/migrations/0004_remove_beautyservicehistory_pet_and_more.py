# Generated by Django 5.2.1 on 2025-06-10 12:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_rename_doctor_id_appointment_doctor_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="beautyservicehistory",
            name="pet",
        ),
        migrations.RemoveField(
            model_name="beautyservicehistory",
            name="staff",
        ),
        migrations.RemoveField(
            model_name="hotelservicehistory",
            name="pet",
        ),
        migrations.RemoveField(
            model_name="hotelservicehistory",
            name="staff",
        ),
        migrations.RemoveField(
            model_name="medicalhistory",
            name="pet",
        ),
        migrations.RemoveField(
            model_name="medicalhistory",
            name="vet",
        ),
        migrations.RemoveField(
            model_name="nutritionplan",
            name="pet",
        ),
        migrations.RemoveField(
            model_name="pet",
            name="owner",
        ),
        migrations.RemoveField(
            model_name="vaccinationhistory",
            name="pet",
        ),
        migrations.RemoveField(
            model_name="vaccinationhistory",
            name="vet",
        ),
        migrations.DeleteModel(
            name="Appointment",
        ),
        migrations.DeleteModel(
            name="BeautyServiceHistory",
        ),
        migrations.DeleteModel(
            name="HotelServiceHistory",
        ),
        migrations.DeleteModel(
            name="MedicalHistory",
        ),
        migrations.DeleteModel(
            name="NutritionPlan",
        ),
        migrations.DeleteModel(
            name="Pet",
        ),
        migrations.DeleteModel(
            name="User",
        ),
        migrations.DeleteModel(
            name="VaccinationHistory",
        ),
    ]
