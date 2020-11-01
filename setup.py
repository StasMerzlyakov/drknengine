from setuptools import setup

setup(
    name='drknengine',
    version='1.0',
    description='DRAKON language editor and engine',
    author='Stas Merzlyakov',
    author_email='merzliakov@gmail.com',
    packages=['drknengine'],
    install_requires=['lxml'],
    scripts=[
        'scripts/svgtools/svgshow.py',
    ]
)
