from setuptools import setup, find_packages

setup(
    name="budget_tracker_v1",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer",
        "SQLAlchemy",
    ],
    entry_points={
        "console_scripts": [
            "bt=budget_tracker.main:app",  # "bt" is the command, and app is the Typer app in main.py
        ],
    },
    author="techie4coffee",
    description="A CLI Budget Tracker built with Typer",
)
