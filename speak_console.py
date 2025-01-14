import sys
from typing import Optional
import threading
import time

import glados


class MessageQueue:
    def __init__(self, delay: Optional[float] = 1.0):
        self.delay = delay
        
        self.message_queue = []
        
        self.tts = glados.TTS()
        
        self.thread = None
        self.run = False
        self.running = False
    
    def add(self, message: str):
        message = message.strip().strip("\n").strip("\r").strip()
        if len(message) == 0:
            return
        
        self._print(f"Adding message: \"{message}\"")
        
        self.message_queue.append(message)
        
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
        message = self.message_queue[0]
        self.message_queue = self.message_queue[1:]
        
        self._print(f"GLaDOS: \"{message}\"")
        self.tts.speak_text_aloud(message)
    
    def _message_loop(self):
        self.running = True
        while self.run and len(self.message_queue) > 0:
            self._process_message()
            time.sleep(self.delay)
        self.running = False
    
    def _print(self, text: str):
        print(text)


def main():
    mq = MessageQueue()
    
    while True:
        message = input(">> ")
        mq.add(message)

main()

