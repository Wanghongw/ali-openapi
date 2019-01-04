"""
django-uric
----------
"""

from setuptools import setup


setup(
    name='uric',
    version='1.1.4',
    url='https://github.com/csrftoken/uric.git',
    license='Apache 2',
    author='LiuZhiChao',
    author_email='404042726@qq.com',
    description='ali and wx sdk for django.',
    long_description=__doc__,
    zip_safe=False,
    platforms=['all', ],
    install_requires=['requests', ],
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