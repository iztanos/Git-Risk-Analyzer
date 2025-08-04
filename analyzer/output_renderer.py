from rich.console import Console

console = Console()

def render_report(report: dict):
    level = report.get("risk_level", "Low")
    issues = report.get("issues", [])

    color = {
        "Low": "green",
        "Medium": "yellow",
        "High": "red"
    }.get(level, "green")

    console.print(f"\n[bold {color}]Risk Level: {level}[/bold {color}]")
    for issue in issues:
        console.print(f"- [bold]{issue}[/bold]")
