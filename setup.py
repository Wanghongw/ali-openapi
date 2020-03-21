"""
django-uric
----------
"""

from setuptools import setup
from setuptools import find_packages


setup(
    name='ali-openapi',
    version='0.0.1',
    url='https://github.com/csrftoken/ali-openapi.git',
    license='Apache 2',
    author='liuzhichao',
    author_email='404042726@qq.com',
    description='ali-openapi',
    long_description=__doc__,
    zip_safe=False,
    packages=find_packages(),
    platforms=['all', ],
    install_requires=['requests', 'pycryptodome', ],
    classifiers=[
        'Framework :: AsyncIO',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)