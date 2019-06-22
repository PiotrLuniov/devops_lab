from setuptools import setup, find_packages

setup(
    name="systeminfo",
    packages=find_packages(),
    version="1.0",
    author="Piotr Luniov",
    author_email="piotr_luniov@epam.com",
    description="Small program for retrieving system information",
    license="MIT",
    install_requires=[
        'psutil'
    ],
    include_package_data=True
)
