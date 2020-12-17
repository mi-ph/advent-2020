@ECHO OFF
SETLOCAL

SET year=%1
SET day=%2

IF NOT DEFINED year GOTO USAGE
IF NOT DEFINED day GOTO USAGE

IF NOT DEFINED AOC_SESSION GOTO COOKIE

curl "https://adventofcode.com/%year%/day/%day%/input" -s -o input.txt --cookie session=%AOC_SESSION%

ECHO input.txt:

:: HEAD command from linux emulator
setlocal EnableDelayedExpansion
set /a counter=0
set linesToShow=10

for /f ^"usebackq^ eol^=^

^ delims^=^" %%a in (input.txt) do (
        if "!counter!"=="!linesToShow!" goto ENDHEAD
        echo %%a
        set /a counter+=1
)
GOTO END

:ENDHEAD
ECHO ... (first 10 lines shown)
GOTO END

:USAGE
ECHO Usage: download.bat YEAR DAY

IF NOT DEFINED AOC_SESSION GOTO COOKIE

GOTO END

:COOKIE
ECHO Set environment variable to log in to AoC: SET AOC_SESSION=session_key

:END
ENDLOCAL
ECHO ON
@EXIT /B 0
