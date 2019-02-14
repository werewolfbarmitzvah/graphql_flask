from flask import Flask
from flask_graphql import GraphQLView

from database.base import db_session
from query_schema import schema


app = Flask(__name__)
app.debug = True


def create_app(path='/graphql'):
    app = Flask(__name__)
    app.debug = True
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app = create_app()
    app.run(threaded=True, debug=True)
