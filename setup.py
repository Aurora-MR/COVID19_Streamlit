from setuptools import setup

setup(name="Data relations", 
    version="0", 
    description="Obtención de datos", 
    author="Aurora Martínez",
    author_email='aurorarivas1606@gmail.com',
    packages=['COVID_data'],
    install_requires=['requests', 'pandas', 'numpy'],
)