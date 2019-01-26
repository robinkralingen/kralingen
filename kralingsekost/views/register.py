import pyramid.httpexceptions as exc
from pyramid.view import view_config

from kralingsekost.security import hash_password

from .. import models


@view_config(
    route_name='register',
    renderer='../templates/dashboard/register.mako'
)
def register(request):
    if request.method == 'GET':
        return {}

    try:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password-confirm']
    except KeyError:
        raise exc.HTTPBadRequest('Missing Key')

    if password != password_confirm:
        raise exc.HTTPBadRequest('Passwords do not match')

    password = hash_password(password)

    user = models.User()
    user.name = name
    user.email = email
    user.password = password

    try:
        request.dbsession.add(user)
    except:
        raise exc.HTTPBadRequest('User already exists')

    return exc.HTTPFound(request.route_url('dashboard.auth.login'))
