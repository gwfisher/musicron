from setuptools import setup,find_packages,find_namespace_packages

setup(
    name="musicron",
    version="0.1.6",
    author="Wesley Fisher",
    author_email="wfisher@praetor.tel",
    description="A cron for music!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gwfisher/musicron",
    packages=["musicron", "musicron.core", "musicron.plugins"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "pyyaml",
        "dbus-python",
        "pathlib",
        "importlib2",
        "psutil",
        "python-dateutil"
    ],
)
