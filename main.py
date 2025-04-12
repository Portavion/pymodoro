import typer
from timer import Timer, Style

app = typer.Typer()


@app.command()
def timer(timer_length_min: int, is_break: bool = typer.Option(False, "--break")):
    """
    Starts a TIMER_LENGTH_MIN minutes work timer, optionally starts it as a break timer with --break.
    """
    timer_total_seconds = timer_length_min  # multiply by 60 to get minutes
    timer_style = Style.break_ if is_break else Style.work

    timer = Timer(timer_total_seconds, timer_style)

    timer.start_timer()


if __name__ == "__main__":
    typer.run(timer)
