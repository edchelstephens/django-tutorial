from django.contrib import admin

from songs.models import Artist


class ArtistAdmin(admin.ModelAdmin):

    fields = ["name", "image"]
    list_display = ["name", "image"]

admin.site.register(Artist, ArtistAdmin)
