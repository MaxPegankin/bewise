from setuptools import setup

setup(
    name='rest_app',
    packages=['rest_app'],
    include_package_data=True,
    install_requires=[
        'flask', 
        'flask-bootstrap',
        'flask-wtf',
        'Flask-SQLAlchemy',
        'psycopg2',
        'python-dotenv',
        'requests'
    ],
)