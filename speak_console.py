import sys
from typing import Optional
import threading
import time

import glados
from llamacheck import LlamaChecker


PROMPT_ENTRY = ">> "

class TTS:
    def __init__(self):
        self.tts = glados.TTS()
        self.lc = LlamaChecker()

    def speak(self, text: str, correct: Optional[bool] = False):
        if correct:
            text = self.lc.correct_text(text)
            print(f"GLaDOS (text corrected): \"{text}\"")
        else:
            print(f"GLaDOS: \"{text}\"")
        
        self.tts.speak_text_aloud(text)


class MessageQueue:
    def __init__(self, delay: Optional[float] = 1.0, correction_command: Optional[str] = "/"):
        self.delay = delay
        self.correction_command = correction_command
        
        self.message_queue = []
        
        self.tts = TTS()
        
        self.thread = None
        self.run = False
        self.running = False
    
    def add(self, message: str):
        message = message.strip().strip("\n").strip("\r").strip()
        if len(message) == 0:
            return
        
        correct = False
        if message[:len(self.correction_command)] == self.correction_command:
            correct = True
            message = message[1:]
        
        if correct:
            print(f"Adding (w/ correction): \"{message}\"")
        else:
            print(f"Adding message: \"{message}\"")
        
        self.message_queue.append(
            {
                "message": message,
                "correct": correct
            }
        )
        
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
    
    def _process_message(self):
        msg = self.message_queue[0]
        self.message_queue = self.message_queue[1:]
            
        self.tts.speak(msg["message"], correct=msg["correct"])
    
    def _message_loop(self):
        self.running = True
        while self.run and len(self.message_queue) > 0:
            self._process_message()
            time.sleep(self.delay)
        self.running = False

def main(args):
    mq = MessageQueue()
    
    while True:
        message = input(PROMPT_ENTRY)
        mq.add(message)


def run():
    main(sys.argv[1:])

run()