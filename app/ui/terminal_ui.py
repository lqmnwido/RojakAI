from rich.console import Console
from rich.panel import Panel

class TerminalUI:
    def __init__(self) -> None:
        self.console = Console()

    def show_header(self) -> None:
        self.console.print(
            Panel.fit(
                "Coding Agent\nModel: gemma3:1b",
                title="Agent",
                border_style="cyan",
            )
        )

    def show_thinking(self) -> None:
        self.console.print("[yellow]Thinking...[/yellow]")

    def show_answer(self, answer: str) -> None:
        self.console.print(
            Panel(
                answer,
                title="Answer",
                border_style="green",
            )
        )