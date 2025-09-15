
@echo off
title Plant Bacteria Database
cls
echo ================================================================
echo                Plant Bacteria Database
echo ================================================================
echo.
echo The database is now running!
echo.
echo * The website should open automatically in your browser
echo * If it doesn't load, wait a few seconds and refresh
echo * Keep this window open while using the database
echo.
echo To close the database:
echo   1. Close this window
echo   2. Close your browser tab
echo ================================================================
echo.
REM Start Django server in a new window
start "" /B python manage.py runserver
REM Wait for server to start
ping 127.0.0.1 -n 6 >nul
REM Open the browser
start "" http://127.0.0.1:8000/
pause
