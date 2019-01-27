import pyramid.httpexceptions as exc
from pyramid.view import view_config
from wtforms import Form, PasswordField, StringField, validators

from kralingsekost.security import hash_password

from .. import models


class RegisterForm(Form):
    name = StringField('name', [
        validators.InputRequired()
    ])
    email = StringField('email', [
        validators.email(),
        validators.InputRequired()
    ])
    password = PasswordField('password', [
        validators.InputRequired()
    ])
    password_confirm = PasswordField('password_confirm', [
        validators.InputRequired(),
        validators.EqualTo('password')
    ])



@view_config(
    route_name='register',
    renderer='dashboard/register.mako'
)
def register(request):
    form = RegisterForm(request.POST)

    if request.method == 'POST' and form.validate():
        user = request.dbsession.query(
            models.User).filter_by(email=form.email.data).one_or_none()
        if user:
            form.errors = {'email': 'User already exists'}
            return {'form': form}
        
        user = models.User()
        user.name = form.name.data
        user.email = form.email.data
        user.password = hash_password(form.password.data)

        request.dbsession.add(user)
        
        return exc.HTTPFound(request.route_url('dashboard.auth.login'))

    return {'form': form}
