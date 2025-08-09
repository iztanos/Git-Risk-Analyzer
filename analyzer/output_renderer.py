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
    # Display issues
    for issue in issues:
        if "AI explanation" in issue:
            console.print(f"\n[bold blue]AI Explanation:[/bold blue]\n{issue}")
        else:
            console.print(f"- [bold]{issue}[/bold]")
