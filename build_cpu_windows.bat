@echo off

set ORIG_DIR=%CD%

set ENV_NAME=glados-cpu
set MAIN_FILE_NAME=speak_console

set DIST_DIR=%ORIG_DIR%\dist
set BUILD_DIR=%ORIG_DIR%\build

set PY=%ORIG_DIR%\%MAIN_FILE_NAME%.py
set SPEC=%ORIG_DIR%\%MAIN_FILE_NAME%.spec
set EXE=%DIST_DIR%\%MAIN_FILE_NAME%.exe
set TARGET_EXE=%ORIG_DIR%\%MAIN_FILE_NAME%.exe

set ICON_ICO=%ORIG_DIR%\icon.ico
set SPLASH_IMG=%ORIG_DIR%\tts_console.png


echo Building portable EXE...
del /f /s /q "%TARGET_EXE%" 1>nul 2>&1
call conda run -n %ENV_NAME% pyinstaller ^
    --clean ^
    --noconfirm ^
    --windowed ^
    --add-data %ICON_ICO%;. ^
	--add-data %ORIG_DIR%\glados;.\glados ^
    --onefile ^
    --splash=%SPLASH_IMG% ^
    --icon=%ICON_ICO% ^
    "%PY%"
if errorlevel 1 goto ERROR

echo Cleaning up...
move "%EXE%" "%TARGET_EXE%"
del /f /s /q "%DIST_DIR%" 1>nul 2>&1
rmdir /s /q "%DIST_DIR%" 1>nul 2>&1
del /f /s /q "%BUILD_DIR%" 1>nul 2>&1
rmdir /s /q "%BUILD_DIR%" 1>nul 2>&1
del /f /q "%SPEC%" 1>nul 2>&1

goto DONE


:ERROR
cd %ORIGDIR%
echo Portable EXE build failed!
exit /B 1

:DONE
cd %ORIGDIR%
echo Portable EXE build done!
exit /B 0