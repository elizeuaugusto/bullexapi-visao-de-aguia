
from setuptools import setup, find_namespace_packages

setup(
    name="bullexapi",
    version="0.1.0",
    description="Wrapper Python para Bullex API",
    author="L0k1",
    author_email="cassioms764@gmail.com",
    url="https://github.com/elizeuaugusto/bullexapi-visao-de-aguia",
    packages=find_namespace_packages(include=["bullexapi*"]),
    install_requires=[
        "requests",
        "websocket-client==1.8.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)
