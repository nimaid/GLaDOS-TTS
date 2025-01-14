from datetime import datetime
import time

import schedule

import glados

tts = glados.TTS()

def say_time():
    time = datetime.now()
    
    print(f"READING TIME ALOUD -> {time.strftime('%I:%M %p')}")
    tts.speak_text_aloud_async(f"The current time is {time.strftime('%I %M %p')}.")

schedule.every().minute.at(":00").do(say_time)

say_time()
while True:
    schedule.run_pending()
    time.sleep(1)
