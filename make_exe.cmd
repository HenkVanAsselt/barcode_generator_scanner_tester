REM ----- Build the executable

cd src
python bumpversion.py
call version_to_env.cmd

rem pyinstaller --clean -y --noupx --onedir barcode_generator.py
rem pyinstaller --clean -y --noupx --onefile barcode_generator.py

REM ----- Rename the EXE with date and buildnumber.
ren .\dist\barcode_generator.exe barcode_generator_%EXE_date%_V%EXE_version%.exe

REM --- Copy required configuration files to the distribution folder
copy src\buildinfo.txt src\dist

cd ..
goto _end

:_end