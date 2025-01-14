@echo off
REM Download and the required models for the project on Windows

echo Downloading Models...

:: Enable delayed expansion for working with variables inside loops
setlocal enabledelayedexpansion

:: Define the list of files with their URLs and local paths
:: Removed quotes around the entire string and fixed paths
set "files[0]=https://github.com/dnhkng/GlaDOS/releases/download/0.1/glados.onnx;glados/models/glados.onnx"
set "files[1]=https://github.com/dnhkng/GlaDOS/releases/download/0.1/phomenizer_en.onnx;glados/models/phomenizer_en.onnx"

:: Loop through the list
for /l %%i in (0,1,1) do (
    for /f "tokens=1,2 delims=;" %%a in ("!files[%%i]!") do (
        set "url=%%a"
        set "file=%%b"
        
        echo Checking file: !file!
        
        if exist "!file!" (
            echo File "!file!" already exists.
        ) else (
            echo Downloading !file!...
            curl -L "!url!" --create-dirs -o "!file!"
            
            if exist "!file!" (
                echo Download successful.
            ) else (
                echo Download failed for !file!
                echo URL: !url!
            )
        )
    )
)

echo Downloads Complete!
pause