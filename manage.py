from app import db, create_app
from flask_migrate import Migrate
from app.models import User
from flask_migrate import Migrate


app = create_app('development')


@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User = User)

if __name__ == '__main__':
    app.run()