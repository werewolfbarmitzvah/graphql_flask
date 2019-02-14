from graphene_sqlalchemy import SQLAlchemyObjectType
from database.model_song import ModelSong
import graphene


class SongAttributes:
    name = graphene.String(description="Song name")
    length = graphene.String(description="Song length")
    album = graphene.String(description="Album name")
    year = graphene.String(description="Year album released")
    artist_id = graphene.ID(description="Global ID for the artist of the song")


class Song(SQLAlchemyObjectType, SongAttributes):
    class Meta:
        model = ModelSong
        interfaces = (graphene.relay.Node,)
