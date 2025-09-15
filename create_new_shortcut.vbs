Set WshShell = CreateObject("WScript.Shell")
strDesktop = WshShell.SpecialFolders("Desktop")

' Create shortcut to the batch file
Set oShellLink = WshShell.CreateShortcut(strDesktop & "\Plant Bacteria Database.lnk")
oShellLink.TargetPath = "C:\Users\Lenovo\OneDrive\Desktop\project_v1\build\Run_Database_Server.bat"
oShellLink.IconLocation = "C:\Windows\System32\shell32.dll,145"
oShellLink.Description = "Launch Plant Bacteria Database"
oShellLink.WindowStyle = 1  ' Normal window
oShellLink.Save
