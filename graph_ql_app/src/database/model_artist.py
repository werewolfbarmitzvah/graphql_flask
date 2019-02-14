from graph_ql_app.database import Base
from sqlalchemy import Column, Integer, String


class ModelArtist(Base):

    __tablename__ = 'artist'

    id = Column('id', Integer, primary_key=True, doc='Id for the artist')
    name = Column('name', String, doc='Artist name')
    genre = Column('genre', String, doc='Artist genre')
