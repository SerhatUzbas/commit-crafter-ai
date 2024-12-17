from setuptools import setup, find_packages

setup(
    name="commit-crafter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer[all]",
        "langchain-openai",
        "python-dotenv",
        # Add any other dependencies your project requires
    ],
    entry_points={
        "console_scripts": [
            "commit-crafter=commit_crafter:app",  # This links the command to your Typer app
        ],
    },
    python_requires=">=3.7",
)
