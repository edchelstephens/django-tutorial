from django.db import models
from django.db.models.deletion import DO_NOTHING, SET_DEFAULT

class Artist(models.Model):

    name = models.CharField(max_length=100)

    def __repr__(self) -> str:
        return "Artist(name={})".format(self.name)

def get_unkown_artist():
    return Artist.objects.get_or_create(name="unkown")

class Album(models.Model):

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return "Album(artist={})".format(repr(self.artist))

class Song(models.Model):

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)    

    def __repr__(self) -> str:
        return "Song(artist={}, album={})".format(repr(self.artist), repr(self.album))

