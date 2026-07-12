@echo off
setlocal
set "HERE=%~dp0"
set "PATCH=%HERE%tricolore_crise_english_patch_v1.0.1.json"
set "SCRIPT=%HERE%apply_json_patch.py"

if not exist "%PATCH%" (
  echo Missing %PATCH%
  echo Download the JSON patch from the v1.0.1 GitHub release and put it here.
  pause
  exit /b 1
)

echo Drag your clean track03.bin onto this window, then press Enter.
set /p "SOURCE=track03.bin: "
set "SOURCE=%SOURCE:"=%"
if not exist "%SOURCE%" (
  echo File not found.
  pause
  exit /b 1
)

py -3 "%SCRIPT%" --patch "%PATCH%" --source "%SOURCE%" --out "%HERE%track03_english_v1.0.1.bin"
if errorlevel 1 (
  echo.
  echo Patching failed. Make sure this is the clean, matching track03.bin.
) else (
  echo.
  echo Success. Copy track03_english_v1.0.1.bin into a COPY of your GDI folder
  echo and rename it to track03.bin.
)
pause
