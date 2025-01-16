import argparse
import sys

import glados

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

    parsed_args = parser.parse_args(args)

    return parsed_args


def main(args):
    parsed_args = parse_args(args)
    
    print("Loading models...")
    tts = glados.TTS()
    
    print("Generating speech...")
    tts.speak_text_aloud(parsed_args.text)


def run():
    main(sys.argv[1:])

run()
