from app import create_app, db
from flask_migrate import Migrate
from app.models import User, Match, Card

application = create_app()
migrate = Migrate(application, db)

@application.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Match=Match, Card=Card)

@application.cli.command()
def createdb():
    db.create_all()

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000, debug=True, )
    # ssl_context=('cert.pem', 'key.pem')
