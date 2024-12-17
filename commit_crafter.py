#!/usr/bin/env python3

import os
import subprocess
import sys
import typer
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from envloader import OPENAI_API_KEY


app = typer.Typer()


def get_git_diff() -> str:
    """Get the git diff output for staged changes"""
    try:
        diff_output = subprocess.check_output(
            ["git", "diff", "--staged"], stderr=subprocess.STDOUT
        ).decode("utf-8")

        if not diff_output:
            # If no staged changes, get unstaged changes
            diff_output = subprocess.check_output(
                ["git", "diff"], stderr=subprocess.STDOUT
            ).decode("utf-8")

        return diff_output
    except subprocess.CalledProcessError as e:
        print(f"Error getting git diff: {e}")
        sys.exit(1)


def generate_commit_message(diff: str) -> str:
    """Generate a commit message using LangChain and OpenAI"""
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, api_key=OPENAI_API_KEY)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a helpful assistant that generates clear and concise git commit messages.
        Follow these rules:
        1. Use the conventional commits format (type: description)
        2. Keep the message under 72 characters
        3. Use present tense
        4. Be specific but concise
        5. Focus on the "what" and "why" rather than "how"
        """,
            ),
            ("user", "Generate a commit message for the following git diff:\n{diff}"),
        ]
    )

    chain = prompt | llm

    response = chain.invoke({"diff": diff})
    return response.content


def create_commit(message: str):
    """Create a git commit with the generated message"""
    try:
        # Add all changes if nothing is staged
        diff_staged = subprocess.check_output(
            ["git", "diff", "--staged"], stderr=subprocess.STDOUT
        ).decode("utf-8")

        if not diff_staged:
            subprocess.run(["git", "add", "."], check=True)

        subprocess.run(["git", "commit", "-m", message], check=True)
        print(f"Successfully committed with message: {message}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating commit: {e}")
        sys.exit(1)


@app.command()
def craft():
    """Craft a commit message and create a commit"""
    diff = get_git_diff()

    if not diff:
        print("No changes to commit!")
        sys.exit(0)

    commit_message = generate_commit_message(diff)
    create_commit(commit_message)


if __name__ == "__main__":
    # load_dotenv()  # Load environment variables from .env file
    app()
