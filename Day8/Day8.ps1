$lineSplitInput = Get-Content -Path .\input.txt

$specificValues = 0
foreach ($lineInput in $lineSplitInput) {
    $splitLine = $lineInput.Split("|")
    $outputSection = $splitLine[1].Split(' ')
    $count = ($outputSection | Where-Object {$_.length -eq 2 -or $_.length -eq 4 -or $_.length -eq 3 -or $_.length -eq 7} | Measure-Object).Count
    $specificValues += $count
}

echo "Part One Solution: " $specificValues