@echo off
echo Setup Automation Environments for Smart on Windows

echo 1.install or update required packages
cd %~dp0

REM pip must be latest version
pip install pip -U
if not errorlevel 0 goto err

pip install -r requirements.txt -U
if not errorlevel 0 goto err

echo 2.copy selenium drivers to python folder, ignore if existed
robocopy \\cns-etnexus\RPS\SeleniumDrivers C:\Python27 /e /xc /xn /xo
if errorlevel 0 goto end

:err
echo ERROR： something wrong during setup, please check!
pause
exit /b -1

:end
echo Done!
exit /b 0