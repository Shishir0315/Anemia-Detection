@echo off
REM Inject Anaconda paths into PATH environment variable
SET PATH=C:\ProgramData\Anaconda3;C:\ProgramData\Anaconda3\Library\mingw-w64\bin;C:\ProgramData\Anaconda3\Library\usr\bin;C:\ProgramData\Anaconda3\Library\bin;C:\ProgramData\Anaconda3\Scripts;C:\ProgramData\Anaconda3\bin;%PATH%

ECHO Running Random Forest Training (Alternative to CNN due to missing Tensorflow)...
"C:\ProgramData\Anaconda3\python.exe" src\train_ml.py

PAUSE
