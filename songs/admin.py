from django.contrib import admin

from songs.models import Artist, Album


class ArtistAdmin(admin.ModelAdmin):

    fields = ["name", "image"]
    list_display = ["name", "image"]

class AlbumAdmin(admin.ModelAdmin):

    list_display = ["id", "artist"]

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
