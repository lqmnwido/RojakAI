import typer

from app.core.agent import CodingAgent
from app.rag.indexer import Indexer
from app.ui.terminal_ui import TerminalUI

app = typer.Typer(help="Local Coding Agent")
ui = TerminalUI()

@app.command()
def index(path: str):
    ui.show_header()
    ui.show_thinking()

    Indexer().index_project(path)

    ui.show_answer("Project indexed successfully.")

@app.command()
def ask(question: str):
    ui.show_header()
    ui.show_thinking()

    answer = CodingAgent().ask(question)

    ui.show_answer(answer)

@app.command()
def chat():
    ui.show_header()

    agent = CodingAgent()

    while True:
        question = input("\nYou > ")

        if question.lower() in ["exit", "quit"]:
            break

        ui.show_thinking()

        answer = agent.ask(question)

        ui.show_answer(answer)