# GLaDOS Text-To-Speech Module

TODO

# Installation Instruction
Try this simplified process, but be aware it's still in the experimental stage!  For all operating systems, you'll first need to install Ollama to run the LLM.

## Install Drivers in necessary
If you are an Nvidia system with CUDA, make sure you install the necessary drivers and CUDA, info here:
https://onnxruntime.ai/docs/install/

If you are using another accelerator (ROCm, DirectML etc), after following the instructions below for you platform, follow up with installing the  [best onnxruntime version](https://onnxruntime.ai/docs/install/) for your system.

## Set up a local LLM server:
1. Download and install [Ollama](https://github.com/ollama/ollama) for your operating system.
2. Once installed, download a small 2B model for testing, at a terminal or command prompt use: `ollama pull llama3.2`



## Windows Installation Process
1. Open the Microsoft Store, search for `python` and install Python 3.12
2. Download this repository, either:
   1. Download and unzip this repository somewhere in your home folder, or
   2. If you have Git set up, `git clone` this repository using `git clone github.com/dnhkng/glados.git`
3. In the repository folder, run the `download_models_windows.bat`, and wait until the installation in complete.
4. Install the required dependencies through `pip`
   - For CPU: `pip install -r requirements_cuda.txt`
   - For GPU/CUDA: `pip install -r requirements_cuda.txt`
   

## macOS Installation Process
This is still experimental. Any issues can be addressed in the Discord server. If you create an issue related to this, you will be referred to the Discord server.  Note: I was getting Segfaults!  Please leave feedback!


1. Download this repository, either:
   1. Download and unzip this repository somewhere in your home folder, or
   2. In a terminal, `git clone` this repository using `git clone github.com/dnhkng/glados.git`
2. In a terminal, go to the repository folder and run these commands:

         chmod +x install_mac.command
         chmod +x start_mac.command

3. In the Finder, double click `download_models_mac.command`, and wait until the installation in complete.
4. Install the required dependencies through `pip`
   - For CPU: `pip install -r requirements_cuda.txt`
   - For GPU/CUDA: `pip install -r requirements_cuda.txt`

## Linux Installation Process
This is still experimental. Any issues can be addressed in the Discord server. If you create an issue related to this, you will be referred to the Discord server.  This has been tested on Ubuntu 24.04.1 LTS


1. Download this repository, either:
   1. Download and unzip this repository somewhere in your home folder, or
   2. In a terminal, `git clone` this repository using `git clone github.com/dnhkng/glados.git`
2. In a terminal, go to the repository folder and run these commands:
   
         chmod +x install_ubuntu.sh
         chmod +x start_ubuntu.sh

3. In the a terminal in the GLaODS folder, run `./download_models_ubuntu.sh`, and wait until the installation in complete.
4. Install the required dependencies through `pip`
   - For CPU: `pip install -r requirements_cuda.txt`
   - For GPU/CUDA: `pip install -r requirements_cuda.txt`