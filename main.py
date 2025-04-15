import typer
import termios
import tty
import sys
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
    old_settings = None
    fd = sys.stdin.fileno()
    try:
        old_settings = termios.tcgetattr(fd)
        tty.setcbreak(sys.stdin.fileno())

        typer.run(timer)
    except termios.error as e:
        print(f"Error: {e}")
        if old_settings:
            try:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            except (termios.error, OSError):
                pass
    finally:
        if old_settings:
            termios.tcflush(fd, termios.TCIFLUSH)
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
