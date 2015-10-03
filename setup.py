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
    description='Automagically provide APIs for your Django admin',
    long_description=__doc__,
    author='Pradip Caulagi',
    author_email='caulagi@gmail.com',
    url='http://github.com/caulagi/django-adminapi/',
    packages=['adminapi'],
    include_package_data=False,
    install_requires=[
        'Django>=1.7',
    ],
    license='BSD',
    zip_safe=False,
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
