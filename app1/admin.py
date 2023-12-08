from django.contrib import admin
from .models import Region, TypeOfUser, UserTG, VeteransAssistant, Question


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)
    search_fields = ('id', 'title',)


@admin.register(TypeOfUser)
class TypeOfUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)
    search_fields = ('id', 'title',)


@admin.register(UserTG)
class UserTGAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'date_of_birth',
                    'time_create', 'time_update',
                    'region', 'type_of_user',)
    list_display_links = ('full_name', 'phone_number',)
    search_fields = ('id', 'full_name', 'phone_number', 'date_of_birth', 'region', 'type_of_user',)
    list_per_page = 10


@admin.register(VeteransAssistant)
class VeteransAssistantAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'patronymic', 'phone_number', 'date_of_birth',
                    'time_create', 'time_update',
                    'region', 'type_of_user',)
    list_display_links = ('surname', 'name', 'patronymic', 'phone_number',)
    search_fields = ('id', 'surname', 'name', 'patronymic', 'phone_number',)
    list_per_page = 10


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_create', 'time_update', 'veterans_assistant', 'user_gt', 'text_question',)
    list_display_links = ('veterans_assistant', 'user_gt', 'text_question',)
    search_fields = ('id', 'veterans_assistant', 'user_gt', 'text_question',)
    ordering = ['-time_create', 'text_question']
    list_per_page = 40
