from setuptools import setup

setup(
    name="xiao-ming",
    packages=["project"],
    include_package_data=True,
    install_requires=[
        "flask",
        "sqlalchemy"
    ]
)