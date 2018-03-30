param(
    [string]$remote,
    [string]$Username,
    [string]$Password,
    [string]$fromfile,
    [string]$topath
)

Write-Host $fromfile
Write-Host $topath
$fromdir =  Get-Item $fromfile
$todir = Get-Item $topath


#Write-Host $Username,$Password
$pass = ConvertTo-SecureString -AsPlainText $Password -Force
$Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $Username,$pass

try{  
$session = New-PSSession –ComputerName $hub -Credential $Cred
Copy-Item –Path $fromdir –Destination $todir -ToSession $session
$session | Remove-PSSession
}
catch{
    Write-Host "Error while executing"
}