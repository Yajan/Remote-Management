param(
    [string]$remote,
    [array]$command
)
Write-Host $remote
$global:Username = $null
$global:Password = $null
$global:hub = $null

$commands = $null

foreach($cmd in $command){
#Write-Host $cmd
    if ($command -ne $null){
        $commands = $commands+" "+$cmd
    }
    else{
        $command = $cmd
    }
}
#Write-Host $commands

function Credencial($var)
{ 

    foreach($line in Get-Content $env:UserProfile/.host/host) {
        #Write-Host $line
        if( $line -like "*$var*"){
            #Write-Host $line
            $a,$b,$c = $line.Split(' ')
            #Write-Host $a,$b,$c
            $tmp, $hub = $a.Split('=')
            #Write-Host $hub
            SetGlobal $hub hub

            $tmp, $Username = $b.Split('=')
            #Write-Host $Username
            SetGlobal $Username Username

            $tmp, $Password = $c.Split('=')
            #Write-Host $Password
            SetGlobal $Password Password
        }
    }
}

function SetGlobal ($tmp, $varName)
{
   Set-Variable -Name $varName -Value ($tmp) -Scope Global
}

Credencial $remote
#Write-Host $Username,$Password
$pass = ConvertTo-SecureString -AsPlainText $Password -Force
$Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $Username,$pass

$script = {
    param($commands)
    cmd.exe /c $commands
}


try{
    $output = Invoke-Command -ComputerName $hub -ScriptBlock $script -ArgumentList $command -credential $Cred
    Write-Output $output
}
catch{
    Write-Host "Error while executing"
}