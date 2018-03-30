param(
    [string]$ip,
	[string]$Username,
	[string]$Password,
    [array]$command
)


$commands = "C:/slave.bat "
#Write-Host $commands


#Write-Host $Username,$Password
$pass = ConvertTo-SecureString -AsPlainText $Password -Force
$Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $Username,$pass

$script = {
    param($commands)
    cmd.exe /c $commands 2> $null
}


try{
    $output = Invoke-Command -ComputerName $ip -ScriptBlock $script -ArgumentList $command -credential $Cred
    Write-Output $output
}
catch{
    Write-Host "Error while executing"
}