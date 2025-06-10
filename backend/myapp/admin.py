from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Users, Pets, Appointments, BeautyServiceHistory, HotelServiceHistory, MedicalHistory, NutritionPlan, VaccinationHistory

admin.site.register(Users)
admin.site.register(Pets)
admin.site.register(Appointments)
admin.site.register(BeautyServiceHistory)
admin.site.register(HotelServiceHistory)
admin.site.register(MedicalHistory)
admin.site.register(NutritionPlan)
admin.site.register(VaccinationHistory)
