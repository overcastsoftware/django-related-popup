try: 
    from setuptools import setup
except ImportError: 
    from distutils.core import setup 

from setuptools import find_packages

setup(
    name='django-related-popup',
    version=__import__('related_popup').__version__,
    description='A set of re-usable widgets and commands for django',
    long_description='',
    author='John Anderson',
    author_email='sontek@gmail.com',
    url='http://github.com/overcastsoftware/django-related-popup',
    download_url='http://github.com/overcastsoftware/django-related-popup',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    classifiers = [
            'Framework :: Django',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
    ],
)
