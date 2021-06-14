from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]

setup(
    name='flask_todo',
    version='0.0',
    description='A To-Do List built with Flask',
    author='Sam Baloyi',
    author_email='sbaloyi@student.wethinkcode.co.za',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)