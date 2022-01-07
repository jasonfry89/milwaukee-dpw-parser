from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
	name="milwaukee-dpw-parser",
	version="0.1.0",
	description="Milwaukee Wisconsin Department of Public Works Parser",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/jasonfry89/milwaukee-dpw-parser",
	author="Jason Fry",
	py_modules=["mke_dpw_parser"],
	python_requires=">=3",
	setup_requires=[
		"wheel",
	],
	install_requires=[
		"beautifulsoup4>=4.6.1",
		"aiohttp>=3.6.0",
	],
)        
