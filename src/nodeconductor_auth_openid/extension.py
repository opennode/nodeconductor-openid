from __future__ import unicode_literals

from django.utils.module_loading import import_string

from nodeconductor.core import NodeConductorExtension


# This function is needed in order to break circular dependency
def login_failed(request, args, **kwargs):
    return import_string('nodeconductor_auth_openid.views.login_failed')(request, args, **kwargs)


class NodeConductorAuthOpenIDExtension(NodeConductorExtension):
    class Settings:

        # the library python-openid does not support a json session serializer
        # <openid.yadis.manager.YadisServiceManager> is not JSON serializable
        # https://github.com/openid/python-openid/issues/17
        SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

        # Should users be created when new OpenIDs are used to log in?
        OPENID_CREATE_USERS = True

        # Generate username from email?
        OPENID_USE_EMAIL_FOR_USERNAME = True

        # When logging in again, should we overwrite user details based on
        # data received via Simple Registration?
        OPENID_UPDATE_DETAILS_FROM_SREG = True

        NODECONDUCTOR_AUTH_OPENID = {
            'LOGIN_URL_TEMPLATE': 'http://example.com/#/login_complete/{token}/',
            'LOGIN_FAILED_URL_TEMPLATE': 'http://example.com/#/login_failed/{token}/',
            # on user registration following name will be used for user's registration_method field
            'NAME': 'openid',
        }

        OPENID_RENDER_FAILURE = login_failed

    @staticmethod
    def update_settings(settings):
        # Enable customer OpenID authentication backend
        settings['AUTHENTICATION_BACKENDS'] += ('nodeconductor_auth_openid.auth.NodeConductorOpenIDBackend',)

        # Enable app in order to connect database models and migrations
        settings['INSTALLED_APPS'] += ('django_openid_auth',)

    @staticmethod
    def django_app():
        return 'nodeconductor_auth_openid'

    @staticmethod
    def django_urls():
        from .urls import urlpatterns
        return urlpatterns
