import argparse
import sys

import glados

# Parse arguments
def parse_args(args):
    parser = argparse.ArgumentParser(
        description=f"A simple program to speak text in GLaDOS's voice.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("-t", "--text", dest="text", type=str, required=True,
                        help="the text to speak"
                        )
    parser.add_argument("-o", "--output", dest="output_file", type=str, required=False, default=None,
                        help="output a wave file"
                        )
    parser.add_argument("-q", "--quiet", dest="speak", action="store_false",
                        help="do not speak the audio aloud"
                        )                  

    parsed_args = parser.parse_args(args)

    return parsed_args


def main(args):
    parsed_args = parse_args(args)
    
    print("Loading models...")
    tts = glados.TTS()
    
    print(f"Generating speech: \"{parsed_args.text}\"")
    audio = tts.generate_speech_audio(parsed_args.text)
    
    if parsed_args.speak:
        print("Speaking aloud...")
        tts.play_audio(audio)
    
    if parsed_args.output_file != None:
        print(f"Saving wave file: \"{parsed_args.output_file}\"")
        tts.save_wav(audio, parsed_args.output_file)

def run():
    main(sys.argv[1:])

run()
