import argparse
import sys
from typing import Optional

import time

import glados
from llamacheck import LlamaChecker

# Parse arguments
def parse_args(args):
    parser = argparse.ArgumentParser(
        description=f"A simple program to speak text in GLaDOS's voice.\n\n"
                    f"Valid parameters are shown in {{braces}}\n"
                    f"Default parameters are shown in [brackets].",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("-t", "--text", dest="text", type=str, required=True,
                        help="the text to speak aloud"
                        )
    
    parser.add_argument("-c", "--correct", dest="correct", action='store_true',
                        help="if the text should be run through a Llama3.2-based spellchecker"
                        )

    parsed_args = parser.parse_args(args)

    return parsed_args

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


def main(args):
    parsed_args = parse_args(args)
    
    tts = TTS()
    
    tts.speak(parsed_args.text, correct=parsed_args.correct)


def run():
    main(sys.argv[1:])

run()