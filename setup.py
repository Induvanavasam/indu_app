from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in indu_app/__init__.py
from indu_app import __version__ as version

setup(
	name="indu_app",
	version=version,
	description="dev",
	author="indu",
	author_email="indusrivanavasam@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
