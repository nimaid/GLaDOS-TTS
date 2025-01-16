import os
import sys
from typing import Optional, Callable
import threading
import time
import argparse
import tkinter as tk

import glados

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

PLATFORM = None
for plat in [
    {"search_string": "win", "name_string": "windows"},
    {"search_string": "linux", "name_string": "linux"},
    {"search_string": "darwin", "name_string": "macintosh"}
]:
    if sys.platform.startswith(plat["search_string"]):
        PLATFORM = plat["name_string"]
        break
if PLATFORM is None:
    PLATFORM = "other"

if PLATFORM == "windows":
    ICON_FILE = os.path.realpath(os.path.join(SCRIPT_DIR, "icon.ico"))
else:
    ICON_FILE = None

DEFAULT_GREETING = "Hello, and welcome to the Aperture Science Interactive Text-To-Speech Console."


# Parse arguments
def parse_args(args):
    parser = argparse.ArgumentParser(
        description=f"A simple GUI program to speak text in GLaDOS's voice.\n\n",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument("-g", "--greeting", dest="greeting", type=str, required=False, default=DEFAULT_GREETING,
                        help="the greeting message to play when the program starts"
                        )
    parser.add_argument("-ng", "--no-greet", dest="no_greet", action='store_true',
                        help="if a greeting message should be played"
                        )

    parsed_args = parser.parse_args(args)

    return parsed_args


class MessageQueue:
    def __init__(
        self,
        delay: Optional[float] = 0.5,
        print_func: Optional[Callable[[str], None]] = print
    ):
        self.delay = delay
        self.print_func = print_func
        
        self.message_queue = []
        
        self.tts = glados.TTS()
        
        self.thread = None
        self.run = False
        self.running = False
    
    def add(self, message: str):
        message = message.strip().strip("\n").strip("\r").strip()
        if len(message) == 0:
            return
        
        self.message_queue.append(message)
        
        self._print_message_queue()
        
        self.run = True
        if not self.running:
            self.start_loop()
    
    def start_loop(self):
        if self.running:
            raise Exception("Message loop is already running!")
        self.run = True
        
        self.thread = threading.Thread(target=self._message_loop)
        self.thread.start()
    
    def stop_loop(self):
        self.run = False
    
    def stop_audio(self):
        self.tts.stop_audio()
    
    def _process_message(self):
        message = self.message_queue[0]
        
        self.tts.speak_text_aloud(message)
        
        self.message_queue = self.message_queue[1:]
        self._print_message_queue()
    
    def _message_loop(self):
        self.running = True
        while self.run and len(self.message_queue) > 0:
            self._process_message()
            time.sleep(self.delay)
        self.running = False
    
    def _print_message_queue(self):
        all_messages = ""
        for message in self.message_queue:
            all_messages += f">> \"{message}\"\n"
        
        self.print_func(all_messages)


class MainWindow:
    def __init__(self, greeting: Optional[str] = None):
        self.greeting = greeting
        
        self.w = tk.Tk()
        self.title = "GLaDOS TTS Engine"
        if ICON_FILE is not None:
            self.w.iconbitmap(ICON_FILE)
        
        self.w.title(f"{self.title} (loading, please wait...)")
        self.w.resizable(width=False, height=False)
        
        self.text_box = tk.Text(self.w, state="disabled", fg="white", bg="black", wrap=tk.WORD)
        self.text_box.grid(row=0, column=0, columnspan=2, sticky="nsew")
        
        self.entry_box = tk.Entry(self.w, state="disabled")
        self.entry_box.grid(row=1, column=0, sticky="nesw")
        
        self.submit_button = tk.Button(
            self.w,
            text = "Submit",
            command = self._submit_button_func,
            state="disabled"
        )
        self.submit_button.grid(row=1, column=1, sticky="nsew")
        
        self.w.columnconfigure(0, weight=20)
        self.w.columnconfigure(1, weight=1)
        
        self.entry_box.focus_set()

        self.mq = None
        self.w.after(200, self._create_message_queue)
        
        self.w.mainloop()
        
        self._cleanup()
    
    def _create_message_queue(self):
        self.mq = MessageQueue(print_func = self._print_to_box)
        self.w.title(self.title)
        
        self.w.bind("<Return>", lambda event: self._submit_button_func())
        self.submit_button.configure(state="normal")
        self.entry_box.configure(state="normal")
        
        if self.greeting is not None:
            self._add_message(self.greeting)
    
    def _add_message(self, message: str):
        self.mq.add(message)
    
    def _submit_button_func(self):
        message = self.entry_box.get()
        self._add_message(message)
        
        self.entry_box.delete(0, "end")
        self.entry_box.focus_set()
    
    def _print_to_box(self, text: str):
        self.text_box.configure(state="normal")
        self.text_box.delete("1.0", "end")
        self.text_box.insert("end", f"{text}\n")
        self.text_box.see("end")
        self.text_box.configure(state="disabled")
    
    def _cleanup(self):
        self.mq.stop_loop()
        self.mq.stop_audio()


def main(args):
    parsed_args = parse_args(args)
    
    if parsed_args.no_greet:
        greeting = None
    else:
        greeting = parsed_args.greeting
    
    mw = MainWindow(greeting=greeting)
    

def run():
    main(sys.argv[1:])

run()