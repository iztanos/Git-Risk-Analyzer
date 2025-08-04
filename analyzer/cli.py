import typer
from analyzer.diff_extractor import get_git_diff
from analyzer.risk_scoring import score_diff
from analyzer.output_renderer import render_report
from analyzer.ai_model import explain_diff

app = typer.Typer()

@app.command()
def main(commit: str = typer.Argument(..., help="Git commit hash to analyze")):
    """Analyze a git commit for security risks."""
    diff = get_git_diff(commit)
    if not diff:
        typer.echo("No diff found or error occurred.")
        return
    
    report = score_diff(diff)
    render_report(report)
    
    # Add AI explanation if available
    explanation = explain_diff(diff)
    if explanation and "error" not in explanation.lower():
        typer.echo("\n AI Analysis:")
        typer.echo(explanation)

if __name__ == "__main__":
    app()
