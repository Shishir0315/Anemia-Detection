@echo off
SET HF_BIN="C:\Users\student\.local\bin\hf.exe"

ECHO --- Hugging Face Upload Tool ---
ECHO 1. Logging in to Hugging Face...
ECHO (You will need your Access Token from hf.co/settings/tokens)
%HF_BIN% auth login

ECHO.
ECHO 2. Uploading project to Shishir0315/Anemia-Detection...
%HF_BIN% upload Shishir0315/Anemia-Detection . .

PAUSE
