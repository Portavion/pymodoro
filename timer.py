import time
import readchar
import os
import threading
from rich import print

from enum import Enum
from rich.progress import (
    BarColumn,
    TaskProgressColumn,
    TextColumn,
    Progress,
    TimeRemainingColumn,
)


class Style(Enum):
    work = "Werk..."
    break_ = "Breakin..."


class TimerSound(Enum):
    start = "Pop"
    end = "Blow"


START_SOUND = f"afplay /System/Library/Sounds/{TimerSound.start.value}.aiff"
END_SOUND = f"afplay /System/Library/Sounds/{TimerSound.end.value}.aiff"
END_NOTIFICATION = (
    """osascript -e 'display dialog "Timer finished!" with title "Pymodoro"'"""
)


class Timer:
    def __init__(self, duration_sec: int, timer_style: Style):
        self.duration = duration_sec
        self.timer_style = timer_style
        self.is_timer_started = False
        self.is_timer_paused = False

    def play_sound(self):
        os.system(START_SOUND) if self.is_timer_started else os.system(END_SOUND)

    def print_notification(self):
        os.system(END_NOTIFICATION)

    def print_progress_timer(self):
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(bar_width=None, pulse_style="bar.pulse"),
            TaskProgressColumn(),
            TimeRemainingColumn(compact=True, elapsed_when_finished=True),
        ) as progress:
            timer = progress.add_task(self.timer_style.value, True, self.duration)

            while not progress.finished:
                progress.update(timer, advance=1)
                time.sleep(1)

    def start_timer(self):
        self.is_timer_started = True
        timer_type = "work" if self.timer_style == Style.work else "break"
        print(
            f":hourglass: [bold red]Starting[/bold red] a [cyan]{self.duration // 60} min [/cyan]{timer_type} timer :hourglass:"
        )
        threading.Thread(target=self.play_sound, args=()).start()
        self.print_progress_timer()
        self.stop_timer()

    def stop_timer(self):
        self.is_timer_started = False
        self.play_sound()
        self.print_notification()
