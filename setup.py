import os
import sys

from setuptools import setup, find_packages

# pylint: disable=invalid-name
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, *('doc', 'DESCRIPTION.rst'))) as f:
    DESCRIPTION = f.read()
with open(os.path.join(here, 'CHANGELOG')) as f:
    CHANGELOG = f.read()

requires = [
    'boto3',
    'Paste',
    'PasteScript',
    'peewee',
    'peewee_migrate',
    'psycopg2',
    'python-dotenv',
    'pyramid',
    'pyramid_assetviews',
    'pyramid_mako',
    'pyramid_services',
]

if sys.version_info[0] < 3:  # python 2.7
    requires.extend([
        'ipaddress',
        'typing',
    ])

development_requires = [
    'colorlog',
    'PyYAML',
    'waitress',

    'flake8',
    'flake8_docstrings',
    'pydocstyle',
    'pycodestyle',
    'pyflakes',
    'pylint',
]

testing_requires = [
    'colorlog',
    'pytest',
    'pytest-cov',
    'pytest-mock',
    'PyYAML',
    'WebTest',
]

production_requires = [
    'CherryPy',
]

setup(
    name='winterthur',
    version='0.1',
    description='',
    long_description=DESCRIPTION + '\n\n' + CHANGELOG,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='',
    author_email='',
    url='',
    keywords='web wsgi pylons pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'development': development_requires,
        'testing': testing_requires,
        'production': production_requires,
    },
    install_requires=requires,
    entry_points="""\
    [paste.app_factory]
    main = winterthur:main
    [console_scripts]
    winterthur_pserve = winterthur.scripts.pserve:main
    winterthur_pstart = winterthur.scripts.pstart:main
    winterthur_manage = winterthur.scripts.manage:main
    """,
)
