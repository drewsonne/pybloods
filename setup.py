from setuptools import setup

requirements = []
with open('requirements.txt') as fp:
    line = fp.readline()
    while line:
        requirements.append(line)
        line = fp.readline()

setup(
    name='pybloods',
    version='0.1.0',
    packages=[
        'pybloods.api',
        'pybloods.cli',
        'pybloods.model'
    ],
    url='https://github.com/drewsonne/pybloods',
    license='LGPLv2',
    author='Drew J. Sonne',
    author_email='drew.sonne@gmail.com',
    description='',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'pybloods-api=pybloods.api:run',
            'pybloods=pybloods.cli:cli'
        ]
    }
)
