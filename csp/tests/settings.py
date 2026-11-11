import django


CSP_REPORT_ONLY = False

CSP_INCLUDE_NONCE_IN = ['default-src']

# This fork makes the header opt-in per URL prefix (see CSPMiddleware
# .process_response): with no prefix listed, nothing is ever sent. Upstream's
# tests all assume a header is produced for '/', so the suite has to opt in --
# otherwise 14 of them fail for a reason that has nothing to do with what they
# are testing. test_middleware covers the setting itself.
CSP_INCLUDE_URL_PREFIXES = ('/',)

DATABASES = {
    'default': {
        'NAME': 'test.db',
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'csp',
)

SECRET_KEY = 'csp-test-key'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'csp.tests.environment.environment',
            'extensions': ['csp.extensions.NoncedScript']
            },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {},
    },
]


# Django >1.6 requires `setup` call to initialise apps framework
if hasattr(django, 'setup'):
    django.setup()
