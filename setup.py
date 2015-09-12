"""
django-adminapi

"""
import re
from setuptools import setup

version = ''
with open('adminapi/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(), re.MULTILINE).group(1)

setup(
    name='django-adminapi',
    version=version,
    url='http://github.com/caulagi/django-adminapi/',
    license='BSD',
    author='Pradip Caulagi',
    author_email='caulagi@gmail.com',
    description='Automagically provide APIs for your Django admin',
    long_description=__doc__,
    packages=['adminapi'],
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Django>=1.7',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
