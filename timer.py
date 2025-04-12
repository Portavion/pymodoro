import time
import os
import threading
from rich import print

from enum import Enum
from rich.progress import track


class Style(Enum):
    work = "Werk..."
    break_ = "Breakin..."


class TimerSound(Enum):
    start = "Pop"
    end = "Blow"


START_SOUND = f"afplay /System/Library/Sounds/{TimerSound.start.value}.aiff"
END_SOUND = f"afplay /System/Library/Sounds/{TimerSound.end.value}.aiff"


class Timer:
    def __init__(self, duration_sec: int, timer_style: Style):
        self.duration = duration_sec
        self.timer_style = timer_style
        self.is_timer_started = False

    def play_sound(self):
        os.system(START_SOUND) if self.is_timer_started else os.system(END_SOUND)

    def print_progress_timer(self):
        for _ in track(range(self.duration), description=self.timer_style.value):
            time.sleep(1)

    def start_timer(self):
        self.is_timer_started = True
        timer_type = "work" if self.timer_style == Style.work else "break"
        print(
            f":hourglass: [bold red]Starting[/bold red] a [cyan]{self.duration // 60} min [/cyan]{timer_type} timer :hourglass:"
        )
        threading.Thread(target=self.play_sound, args=()).start()
        self.print_progress_timer()
        self.is_timer_started = False
        self.play_sound()
