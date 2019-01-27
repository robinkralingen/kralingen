from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from pyramid.csrf import SessionCSRFStoragePolicy


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    from pyramid.settings import asbool
    if asbool(settings.get('env.use_env_variables', False)):
        from os import getenv
        settings['sqlalchemy.url'] = getenv(settings['sqlalchemy.url'])

    with Configurator(settings=settings) as config:
        config.include('.models')
        config.include('pyramid_mako')
        config.include('.routes')
        config.include('.security')
        config.set_csrf_storage_policy(SessionCSRFStoragePolicy)

        config.set_default_permission('public')

        config.set_session_factory(
            SignedCookieSessionFactory(settings.get('secret'))
        )

        config.scan()
    return config.make_wsgi_app()
