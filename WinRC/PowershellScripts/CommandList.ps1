Get-WmiObject Win32_Computersystem
$dsk = Get-WmiObject Win32_LogicalDisk
foreach ($drive in $dsk ){ "Drive "+$drive.Name, [int]($drive.Size/1073741824)}
Get-Process * | Sort-Object ProcessName
Get-WmiObject win32_service | Sort ProcessId | Group-Object ProcessId