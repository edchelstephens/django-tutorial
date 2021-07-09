import uuid

from django.db import models
from django.db.models.deletion import DO_NOTHING, SET_DEFAULT

class Artist(models.Model):

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="artist/", blank=True)

    def __repr__(self) -> str:
        return "Artist(name={})".format(self.name)

    def __str__(self) -> str:
        return self.name

def get_unkown_artist():
    unknown_artist, created =  Artist.objects.get_or_create(name="unkown")
    return unknown_artist

class Album(models.Model):

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return "Album(artist={})".format(repr(self.artist))

class Song(models.Model):

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT) 
    feat = models.ForeignKey(
        Artist, 
        on_delete=models.SET(get_unkown_artist), 
        related_name="songs_featured", 
        null=True, 
        blank=True
    )   

    def __repr__(self) -> str:
        return "Song(artist={}, album={}, feat={})".format(
            repr(self.artist), 
            repr(self.album), 
            repr(self.feat)
    )


class Musician(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return "Musician(name={}, groups={})".format(
            self.name,
            self.get_groups()
    )

    def get_groups(self):
        return [ g.name for g in self.groups.all() ]

class Group(models.Model):

    name = models.CharField(max_length=50)
    members = models.ManyToManyField(
        Musician, 
        through="Membership",
        related_name="groups"
    )

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return "Group(name={}, members={})".format(
            self.name,
            self.get_members()
        )

    def get_members(self):
        return [ m.name for m in self.members.all() ]


class Membership(models.Model):

    musician = models.ForeignKey(
        Musician,
        on_delete=models.CASCADE,
        related_name="memberships"
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="group_memberships"
    )
    
    date_joined = models.DateTimeField()
    invite_reason = models.CharField(max_length=120)


    def __str__(self) -> str:
        return "{} - {}".format(self.group, self.musician)

    def __repr__(self) -> str:
        return "Membership(musician={}, group={})".format(
            self.musician,
            self.group
        )