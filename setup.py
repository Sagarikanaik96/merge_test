from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in serikandi_customizations/__init__.py
from serikandi_customizations import __version__ as version

setup(
	name="serikandi_customizations",
	version=version,
	description="Serikandi Customizations",
	author="Promantia Business Solutions Pvt Ltd",
	author_email="radhika.k@promantia.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
