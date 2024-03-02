from setuptools import setup, find_packages

setup(
    name="<vad_lib>",
    version="0.0.1",
    author="<author>",
    author_email="<author_email>",
    url="",
    description="Description of lib",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    entry_points={"console_scripts": ["<vad_lib> = <vad_lib>.main:download"]},
)