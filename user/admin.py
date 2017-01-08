from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = (
		'email', 
		'first_name', 
		'last_name', 
		'is_active', 
		'is_staff'
	)

	
