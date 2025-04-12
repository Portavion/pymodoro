import typer
from timer import Timer, Style

app = typer.Typer()


@app.command()
def timer(timer_length_min: int, is_break: bool = typer.Option(False, "--break")):
    """
    Starts a TIMER_LENGTH_MIN minutes work timer, optionally starts it as a break timer with --break.
    """
    timer_total_seconds = timer_length_min  # multiply by 60 to get minutes
    if is_break:
        timer_style = Style.break_
    else:
        timer_style = Style.work

    timer = Timer(timer_total_seconds, timer_style)

    timer.start_timer()


if __name__ == "__main__":
    typer.run(timer)
