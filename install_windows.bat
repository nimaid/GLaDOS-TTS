@echo off

REM Install Miniconda (if conda is not already installed)
set MINICONDAPATH=%USERPROFILE%\Miniconda3
set CONDAEXE=%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%-condainstall.exe
set "OS="
set "MCLINK="

where conda >nul 2>nul
if %ERRORLEVEL% EQU 0 goto CONDAFOUND

:INSTALLCONDA
reg Query "HKLM\Hardware\Description\System\CentralProcessor\0" | find /i "x86" > NUL && set OS=32BIT || set OS=64BIT
if %OS%==32BIT set MCLINK=https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86.exe
if %OS%==64BIT set MCLINK=https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe

echo Downloading Miniconda3 (This will take while, please wait)...
powershell -Command "(New-Object Net.WebClient).DownloadFile('%MCLINK%', '%CONDAEXE%')" >nul 2>nul
if errorlevel 1 goto CONDAERROR

echo Installing Miniconda3 (This will also take a while, please wait)...
start /wait /min "Installing Miniconda3..." "%CONDAEXE%" /InstallationType=JustMe /S /D="%MINICONDAPATH%"
del "%CONDAEXE%"
if not exist "%MINICONDAPATH%\" (goto CONDAERROR)

"%MINICONDAPATH%\Scripts\conda.exe" init
if errorlevel 1 goto CONDAERROR

echo Miniconda3 has been installed!
set CONDAPATH=%USERPROFILE%\Miniconda3\condabin\conda
goto ENDCONDA

:CONDAERROR
echo Miniconda3 install failed!
goto END

:CONDAFOUND
echo Conda is already installed!
set CONDAPATH=conda
goto ENDCONDA

:ENDCONDA



REM Install the conda environment (if not already installed)
set "ENVNAME=glados"
set "ENVDETECT="

:INSTALLENV
FOR /F "tokens=*" %%g IN ('conda env list ^| findstr /R /C:"%ENVNAME%"') do (set ENVDETECT="%%g")
if defined ENVDETECT goto ALREADYINSTALLED

echo Installing the conda environment...
call %CONDAPATH% env create -f environment_cuda.yml
if errorlevel 1 goto INSTALLENVFAIL

echo Conda environment installed!
goto ENVEND

:INSTALLENVFAIL
rmdir %USERPROFILE%\Miniconda3\envs\%ENVNAME% /s /q 2> nul
echo The conda environment could not be installed!
goto END

:ALREADYINSTALLED
echo The conda environment is already installed!
goto ENVEND

:ENVEND



REM Download and the required models (if not already downloaded)
echo Verifying and downloading required models...

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
                goto MODELERROR
            )
        )
    )
)

echo All models are ready!
goto MODELEND

:MODELERROR
echo Some models failed to download. Please try again later or manually download them.
goto END

:MODELEND



REM End of script
:END
pause