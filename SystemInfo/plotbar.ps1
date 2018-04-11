param(
    [int]$x
)

function plot ($x) {
    for ($i = 0; $i -lt $x; $i++) {
        if ($i -le 10){
            Write-Host "|" -NoNewline -BackgroundColor Gray -ForegroundColor Black
        }
        elseif ($i -le 20 -and $i -gt 10){
            Write-Host "|"  -NoNewline -BackgroundColor White -ForegroundColor Black
        }
        elseif ($i -le 30 -and $i -gt 20){
            Write-Host "|" -NoNewline  -BackgroundColor DarkGray -ForegroundColor Black
        }
        elseif ($i -le 40 -and $i -gt 30){
            Write-Host "|" -NoNewline  -BackgroundColor DarkCyan -ForegroundColor Black
        }
        elseif ($i -le 50 -and $i -gt 40){
            Write-Host "|" -NoNewline -BackgroundColor Blue -ForegroundColor White
        }
        elseif ($i -le 60 -and $i -gt 50){
            Write-Host "|" -NoNewline -BackgroundColor Green -ForegroundColor White
        }
        elseif ($i -le 70 -and $i -gt 60) {
            Write-Host "|" -NoNewline -BackgroundColor Yellow -ForegroundColor Black
        }
        elseif ($i -le 80 -and $i -gt 70){
            Write-Host "|" -NoNewline -BackgroundColor DarkYellow -ForegroundColor Black
        }
        elseif ($i -le 90 -and $i -gt 80){
            Write-Host "|" -NoNewline -BackgroundColor Red -ForegroundColor White
        }
        elseif ($i -le 100 -and $i -gt 90){
            Write-Host "|" -NoNewline -BackgroundColor DarkRed -ForegroundColor White
        }
    }
  Write-Host " $i %"
}
plot $x