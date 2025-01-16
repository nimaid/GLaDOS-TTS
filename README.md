# GLaDOS Text-To-Speech Module
[Adapted from dnhkng's GLaDOS repository.](https://github.com/dnhkng/GlaDOS)

Add the evil robot to your Python project as easy as:
```python
import glados

tts = glados.TTS()
tts.speak_text_aloud("Hello, World!")
```
Find more usage options [here](https://github.com/nimaid/GLaDOS-TTS#Usage)!

# Installation

## Windows
1. Install with `install_windows.bat`. This should automatically:
   1. Install Miniconda if you don't already have a `conda` binary
   2.  Install the Conda environment (with CUDA and CuDNN!)
   3.  Download the required model files if not already present
2. Run the interactive console demo with `run_console_windows.bat`

## Linux
1. Install [Miniconda](https://www.anaconda.com/download/success) if you do not have `conda` already installed.
   - [64-Bit x86](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)
   - [64-Bit ARM64](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh)
2. Install the Conda environment with one of the following commands:
   - GPU accelerated: `conda env create -f environment_cuda.yaml`
   - CPU only: `conda env create -f environment.yaml`
3. Download the required models with `download_models_ubuntu.bash`
4. Run the interactive console demo with `conda run -n glados python speak_console.py`

## Mac
1. Install [Miniconda](https://www.anaconda.com/download/success) if you do not have `conda` already installed.
   - [64-Bit x86 (Intel)](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg)
   - [64-Bit ARM64 (Apple)](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.pkg)
2. Install the Conda environment with one of the following commands:
   - GPU accelerated: `conda env create -f environment_cuda.yaml`
   - CPU only: `conda env create -f environment.yaml`
3. Download the required models with `download_models_mac.command`
4. Run the interactive console demo with `conda run -n glados python speak_console.py`

## Generic Conda
1. Install [Miniconda](https://www.anaconda.com/download/success) for your operating system if you do not have `conda` already installed.
2. Install the Conda environment with one of the following commands:
   - GPU accelerated: `conda env create -f environment_cuda.yaml`
   - CPU only: `conda env create -f environment.yaml`
3. Download the required models and place them in `glados/models/`
   - [glados.onnx](https://github.com/dnhkng/GlaDOS/releases/download/0.1/glados.onnx)
   - [phomenizer_en.onnx](https://github.com/dnhkng/GlaDOS/releases/download/0.1/phomenizer_en.onnx)
4. Run the interactive console demo with `conda run -n glados python speak_console.py`

# Usage

## From An Interactive Console
This is the suggested way to quickly generate messages. After it loads the models, it is actually very fast. It usually takes less than a quarter of a second to generate a message.
`conda run -n glados python speak_console.py`

## From The Command Line
This has to load the models every single time it runs, so it can be a bit slow.
`conda run -n glados python speak.py -t "I am reading a message directly from the command line."`

## In Custom Code
```python
import time  # For making delays
import glados  # Import the local module

# Create a reusable text-to-speech object (this will take some time to load the AI models)
tts = glados.TTS()

# Say some text, wait 1 second, and then move on to the next line of code
# If the speech is longer than 1 second, it will continue in the background
tts.speak_text_aloud_async("Calcium is a soft, silvery-white metal and one of the most abundant elements on Earth. It is essential for living organisms, playing a critical role in building strong bones and teeth, as well as aiding muscle function and nerve signaling. Calcium is commonly found in compounds like limestone and is extracted for use in construction materials, such as cement and plaster. It also has industrial applications, including acting as a reducing agent in metal production. In everyday life, dietary calcium is obtained from foods like milk, cheese, leafy greens, and fortified products to support overall health.")
time.sleep(1)

# Say some text and wait until it is done being spoken
# If the previous speech isn't over yet, this will interrupt it
tts.speak_text_aloud("Hello, and thank you, world.")

# Manually stop the speech playback
tts.stop_audio()

# Generate audio to a Numpy array
speech_audio = tts.generate_speech_audio("Wow, my voice is now stored directly in your random access memory.")
```