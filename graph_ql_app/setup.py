from distutils.core import setup
from ast import literal_eval
from database.model_artist import ModelArtist
from database.model_song import ModelSong
from database import base
import logging
import sys


setup(
    name='graph_ql_app',
    packages=['graph_ql_app',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
)


# Load logging configuration
log = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    log.info('Create database {}'.format(base.db_name))
    base.Base.metadata.create_all(base.engine)

    log.info('Insert artist data in database')
    with open('database/data/artist.json', 'r') as file:
        data = literal_eval(file.read())
        for record in data:
            artist = ModelArtist(**record)
            base.db_session.add(artist)
        base.db_session.commit()

    log.info('Insert song data in database')
    with open('database/data/song.json', 'r') as file:
        data = literal_eval(file.read())
        for record in data:
            song = ModelSong(**record)
            base.db_session.add(song)
        base.db_session.commit()
