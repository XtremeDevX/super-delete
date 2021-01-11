@echo off
set FOLDER=%CD%
cd /
del /F/Q/S "%FOLDER%" > NUL
rmdir /Q/S "%FOLDER%"
exit