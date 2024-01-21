from setuptools import setup, find_packages
import re

VERSIONFILE="adiskreader_secretsdump/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
	# Application name:
	name="adiskreader_secretsdump",

	# Version number (initial):
	version=verstr,

	# Application author details:
	author="Tamas Jos",
	author_email="info@skelsecprojects.com",

	# Packages
	packages=find_packages(exclude=["tests*"]),

	# Include additional files into the package
	include_package_data=True,


	# Details
	url="https://github.com/skelsec/adiskreader-secretsdump",

	zip_safe=True,
	description="Secretsdump module for adiskreader",

	# long_description=open("README.txt").read(),
	python_requires='>=3.6',
	classifiers=[
		"Programming Language :: Python :: 3.6",
		"Operating System :: OS Independent",
	],
	
	## these are only necessary for the command line tool
	## lib can work without additional deps
	install_requires=[
		'adiskreader>=0.0.3',
		'pypykatz>=0.0.7',
        'aesedb>=0.1.6',
		'tqdm',
		'colorama',
	],

	entry_points={
		'console_scripts': [
			'adiskreader-secretsdump = adiskreader_secretsdump.examples.console:main',
		],
	}
)