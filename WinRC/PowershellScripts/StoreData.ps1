param(
[object]$data,
[string]$action
)

If ($action -eq "store"){
foo $data stored
Write-Host $stored
}
If ($action -eq "fetch"){
return $stored
} 

function foo ($data, $varName)
{  
   $global:stored = $null
   Set-Variable -Name $varName -Value ($data) -Scope Global
}



