Set WshShell = CreateObject("WScript.Shell")
Set FSO = CreateObject("Scripting.FileSystemObject")

' Get Desktop path
strDesktop = WshShell.SpecialFolders("Desktop")

' Get the current script directory
currentDir = FSO.GetParentFolderName(WScript.ScriptFullName)

' Create shortcut
Set oShortcut = WshShell.CreateShortcut(strDesktop & "\Plant Bacteria Database.lnk")

' Set the target to be PowerShell running the batch file
oShortcut.TargetPath = "powershell.exe"
oShortcut.Arguments = "-NoProfile -ExecutionPolicy Bypass -Command ""& '" & currentDir & "\run_database.bat'"""
oShortcut.WorkingDirectory = currentDir
oShortcut.IconLocation = "C:\Windows\System32\shell32.dll,139"
oShortcut.Description = "Plant Bacteria Database"
oShortcut.Save

WScript.Echo "Shortcut created successfully on your desktop! You can now use it to start the database."
