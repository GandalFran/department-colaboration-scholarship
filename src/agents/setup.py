from setuptools import setup

setup(
    name='Beca colaboracion',
    version='1.0',
    description='Proyecto para la beca de colaboaracion',
    author='Francisco Pinto Santos',
    author_email='franpintosantos@usal.es',
    license='see LICENSE.md for details',
    packages=['agents', 'utils'],
    install_requires=[
        'py2neo',
        'pymongo',
        'spacy==2.2.3',
        'confluent-kafka==1.3.0',
        'vaderSentiment==3.2.1',
        'newsapi-python',
        'lxml==4.9.1',
        'cssselect==1.1.0',
        'requests==2.21.0',
        'Flask==1.1.1',
        'werkzeug==0.16.1',
        'flask_cors==3.0.8',
        'flask_restplus==0.13.0'
    ]
)
