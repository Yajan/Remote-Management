param(
    [string]$server
)
Test-Connection -ComputerName $server -Count 3 -Delay 2 -TTL 255 -BufferSize 256 -ThrottleLimit 32 