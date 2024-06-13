from setuptools import setup, find_packages

setup(
    name='home_inventory_system',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click',  # if using Click for CLI
        'SQLAlchemy',  # if using SQLAlchemy for ORM
    ],
    entry_points={
        'console_scripts': [
            'inventory-cli=inventory.cli:main',
        ],
    },
)
