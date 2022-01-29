from django.contrib import admin

from .models import User, Agent, Lead, UserProfile, Category

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Agent)
admin.site.register(Lead)
admin.site.register(Category)


class LeadAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'category', 'agent')

