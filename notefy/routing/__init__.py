from notefy.models import User
from notefy import login_manager


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)


from .signup import *
from .home import *
from .notes import *
from .misc import *