from django.contrib import admin
from django.db.models import F


# Register your models here.
from announcement.models import Announcement


# Useful for executing bulk operations. # same the default delete
def news_action(modeladmin, request, queryset):
    for announcement in queryset:
        announcement.status = 'published'
        announcement.save()
news_action.short_description = 'Publish selected announcements'  
    

class AnnouncementModelAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "updated", "timestamp", "status")
    list_filter = ["status"]
    search_fields = ["title"]
    ordering = ["status"]
    actions = ['delete_selected', news_action]
    list_per_page = 25

    class Meta:
        model = Announcement
    
admin.site.register(Announcement, AnnouncementModelAdmin)
