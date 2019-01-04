"""
django-uric
----------
"""

from setuptools import setup


setup(
    name='uric',
    version='1.0.0',
    url='https://github.com/dongweiming/sanic-mako',
    license='Apache 2',
    author='LiuZhiChao',
    author_email='404042726@qq.com',
    description='ali and wx sdk for django.',
    long_description=__doc__,
    py_modules=['uric-django'],
    zip_safe=False,
    platforms='any',
    install_requires=['requests', 'django', 'xml'],
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