from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import MenTop, LadiesClothing, MenSneakers

class MenTopAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'quantity', 'price', 'display_image', 'time']  # Add 'display_image' to the list display

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')  # Use 'mark_safe' to render HTML
    display_image.short_description = 'Image'  # Custom column name

admin.site.register(MenTop, MenTopAdmin)

class MenSneakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'quantity', 'price', 'display_image', 'time']  # Add 'display_image' to the list display

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')  # Use 'mark_safe' to render HTML
    display_image.short_description = 'Image'  # Custom column name

admin.site.register(MenSneakers, MenSneakerAdmin)

class LadiesClothingsAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'quantity', 'price', 'display_image', 'time']  # Add 'display_image' to the list display

    def display_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')  # Use 'mark_safe' to render HTML
    display_image.short_description = 'Image'  # Custom column name

admin.site.register(LadiesClothing, LadiesClothingsAdmin)

