from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Pet, Appointment, BeautyServiceHistory, HotelServiceHistory, MedicalHistory, NutritionPlan, VaccinationHistory

admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Appointment)
admin.site.register(BeautyServiceHistory)
admin.site.register(HotelServiceHistory)
admin.site.register(MedicalHistory)
admin.site.register(NutritionPlan)
admin.site.register(VaccinationHistory)
