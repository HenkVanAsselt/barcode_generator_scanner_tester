REM ----- Build the EXE
cd src
rem pyinstaller --clean -y --noupx --onedir barcode_generator.py
pyinstaller --clean -y --noupx --onefile --add-file buildinfo.txt;buildinfo.txt barcode_generator.py

cd ..
goto _end

REM ----- Rename the EXE
REM ----- Entere date and buildnumber. Will be used for renaming the executable
rem set /P datestr="Date in YYYYMMDD: "
rem set /P buildnr="Give new buildnumber: "
rem ren src\dist\barcode_generator.exe barcode_generator_%datestr%_V%buildnr%.exe

:_end