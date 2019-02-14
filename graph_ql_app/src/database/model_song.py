from graph_ql_app.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class ModelSong(Base):

    __tablename__ = 'song'

    id = Column('id', Integer, primary_key=True, doc='Id for the song')
    name = Column('name', String, doc='Song name')
    length = Column('length', String, doc='Song length')
    album = Column('album', String, doc='Album name')
    year = Column('year', String, doc='Year album released')
    artist_id = Column('artist_id', Integer, ForeignKey('artist.id'), doc='Id associated with the artist of the song')
