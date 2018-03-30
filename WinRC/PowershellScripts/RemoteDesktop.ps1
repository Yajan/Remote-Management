param(
    [string]$server
)
Write-Host $server
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
Credencial $server
#Write-Host $Username,$Password,$hub
cmdkey /generic:$hub /user:$hub\$Username /pass:$Password
mstsc /v: $hub
#to bypass the security alerts or certificate errors that has to be done manually
sleep 5
cmdkey /delete:$hub 
