from graphene_sqlalchemy import SQLAlchemyObjectType
from database.model_artist import ModelArtist
import graphene


class ArtistAttributes:
    name = graphene.String(description="Artist name")
    genre = graphene.String(description="Artist genre")


class Artist(SQLAlchemyObjectType, ArtistAttributes):
    class Meta:
        model = ModelArtist
        interfaces = (graphene.relay.Node,)
