param(
    [string]$remote,
    [string]$fromfile,
    [string]$topath
)
Write-Host $remote
$global:Username = $null
$global:Password = $null
$global:hub = $null

Write-Host $fromfile
Write-Host $topath
$fromdir =  Get-Item $fromfile
$todir = Get-Item $topath

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

#try{  
$session = New-PSSession –ComputerName $hub -Credential $Cred
Copy-Item –Path $fromdir –Destination $todir -FromSession $session
$session | Remove-PSSession
#}
#catch{
#    Write-Host "Error while executing"
#}