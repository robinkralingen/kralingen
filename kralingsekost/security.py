import bcrypt

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import ALL_PERMISSIONS, Allow, Authenticated

from kralingsekost.models import User


def hash_password(password):
    password_hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    return password_hash.decode('utf8')


def check_password(password, hashed_password):
    expected_hash = hashed_password.encode('utf8')
    return bcrypt.checkpw(password.encode('utf8'), expected_hash)


def get_user(request):
    user_id = request.unauthenticated_userid
    if user_id is not None:
        user = request.dbsession.query(User).get(user_id)
        return user


class LabelAuthenticationPolicy(AuthTktAuthenticationPolicy):
    def authenticated_userid(self, request):
        user = request.user
        if user is not None:
            return user.id


class Root:
    __acl__ = (
        (Allow, Authenticated, ALL_PERMISSIONS),
    )


def includeme(config):
    settings = config.get_settings()
    authn_policy = LabelAuthenticationPolicy(
        settings['secret'],
        hashalg='sha512',
    )
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.add_request_method(get_user, 'user', reify=True)
    config.set_root_factory(lambda request: Root())
