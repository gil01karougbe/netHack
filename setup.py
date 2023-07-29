"""
Lab setup 
"""
from setuptools import setup

setup(
    name="netHack",
    version="1.0.0",
    description="Automated netHack",
    packages=['netHack'],
    
    install_requires=[
        "click",
        "questionary"
    		],
    
    entry_points={
        'console_scripts': ['netHack=netHack.__main__:main']
                },

)

