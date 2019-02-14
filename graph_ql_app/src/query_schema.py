import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from graph_ql_app import artist_schema, song_schema


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    artist = graphene.relay.Node.Field(artist_schema.Artist)
    artistList = SQLAlchemyConnectionField(artist_schema.Artist)
    song = graphene.relay.Node.Field(song_schema.Song)
    songList = SQLAlchemyConnectionField(song_schema.Song)

schema = graphene.Schema(query=Query)
