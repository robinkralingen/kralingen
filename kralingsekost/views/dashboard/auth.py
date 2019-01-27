import logging

import pyramid.httpexceptions as exc
from pyramid.view import view_config
from pyramid.security import remember, forget

from wtforms import Form, StringField, validators, PasswordField

from kralingsekost import models
from kralingsekost.security import hash_password, check_password

log = logging.getLogger(__name__)


class LoginForm(Form):
    email = StringField('email', [
        validators.email(),
        validators.InputRequired()
    ])
    password = PasswordField('password', [
        validators.InputRequired()
    ])


@view_config(
    route_name='dashboard.auth.login',
    request_method=['GET', 'POST'],
    renderer='dashboard/auth.mako'
)
def login(request):
    form = LoginForm(request.POST)

    if request.method == 'POST' and form.validate():
        user = request.dbsession.query(
            models.User).filter_by(email=form.email.data).one_or_none()
        if not user:
            form.errors = {'email': 'no user exists'}
            return {'form': form}

        if not check_password(form.password.data, user.password):
            form.errors = {'password': 'password is incorect'}
            return {'form': form}

        headers = remember(request, user.id)

        return exc.HTTPFound(
            request.route_path('dashboard.recipe.list'),
            headers=headers
        )
        
    return {'form': form}



@view_config(route_name='dashboard.auth.logout')
def logout(request):
    headers = forget(request)
    url = request.route_url('recipe.list')
    return exc.HTTPFound(
        location=url,
        headers=headers
    )
