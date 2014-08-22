try: 
    from setuptools import setup
except ImportError: 
    from distutils.core import setup 

setup(
    name='django-related-popup',
    version=__import__('related_popup').__version__,
    description='A set of re-usable widgets and commands for django',
    long_description='',
    author='Overcast Software',
    author_email='team@overcast.io',
    url='http://github.com/overcastsoftware/django-related-popup',
    download_url='http://github.com/overcastsoftware/django-related-popup',
    license='MIT',
    packages=['related_popup', 'related_popup.templates'],
    include_package_data=True,
    classifiers = [
            'Framework :: Django',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
    ],
)
