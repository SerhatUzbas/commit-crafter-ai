from setuptools import setup, find_packages

setup(
    name="commit-crafter-ai",
    version="0.1.0",
    author="Serhat Uzbas",
    author_email="serhatuzbas@gmail.com",
    description="AI-powered commit message generator",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SerhatUzbas/commit-crafter-ai/",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=[
        "typer[all]",
        "langchain-openai==0.2.12",
        "python-dotenv==1.0.1",
        "aiohappyeyeballs==2.4.4",
        "aiohttp==3.11.10",
        "aiosignal==1.3.2",
        "annotated-types==0.7.0",
        "anyio==4.7.0",
        "attrs==24.3.0",
        "certifi==2024.12.14",
        "charset-normalizer==3.4.0",
        "click==8.1.7",
        "distro==1.9.0",
        "frozenlist==1.5.0",
        "h11==0.14.0",
        "httpcore==1.0.7",
        "httpx==0.28.1",
        "idna==3.10",
        "jiter==0.8.2",
        "jsonpatch==1.33",
        "jsonpointer==3.0.0",
        "langchain==0.3.12",
        "langchain-core==0.3.25",
        "langchain-text-splitters==0.3.3",
        "langsmith==0.2.3",
        "markdown-it-py==3.0.0",
        "mdurl==0.1.2",
        "multidict==6.1.0",
        "numpy==2.2.0",
        "openai==1.57.4",
        "orjson==3.10.12",
        "packaging==24.2",
        "propcache==0.2.1",
        "pydantic==2.10.3",
        "pydantic_core==2.27.1",
        "Pygments==2.18.0",
        "requests==2.32.3",
        "requests-toolbelt==1.0.0",
        "rich==13.9.4",
        "setuptools>=75.6.0",
        "shellingham==1.5.4",
        "sniffio==1.3.1",
        "SQLAlchemy==2.0.36",
        "tenacity==9.0.0",
        "tiktoken==0.8.0",
        "tqdm==4.67.1",
        "typer==0.15.1",
        "typing_extensions==4.12.2",
        "urllib3==2.2.3",
        "yarl==1.18.3",
    ],
    entry_points={
        "console_scripts": [
            "commit-crafter-ai=commit_crafter.commit_crafter:app",
        ],
    },
    python_requires=">=3.7",
)
