﻿param(
    [string]$remote
)
Write-Host $remote
$global:Username = $null
$global:Password = $null
$global:hub = $null


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
Write-Host $Username,$Password
$pass = ConvertTo-SecureString -AsPlainText $Password -Force
$Cred = New-Object System.Management.Automation.PSCredential -ArgumentList $Username,$pass

#

$session = New-PSSession -ComputerName $hub -Credential $Cred
Enter-PSSession $session
