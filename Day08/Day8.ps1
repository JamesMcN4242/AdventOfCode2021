$lineSplitInput = Get-Content -Path .\input.txt

$specificValues = 0
foreach ($lineInput in $lineSplitInput) {
    $splitLine = $lineInput.Split("|")
    $outputSection = $splitLine[1].Split(' ')
    $count = ($outputSection | Where-Object {$_.length -eq 2 -or $_.length -eq 4 -or $_.length -eq 3 -or $_.length -eq 7} | Measure-Object).Count
    $specificValues += $count
}

Write-Output "Part One Solution: $specificValues"

$combinedOutput = 0
foreach($lineInput in $lineSplitInput) {
    $splitLine = $lineInput.Split("|")    
    $valueSection = $splitLine[0].Split(' ')    
    $expected = @{}

    # Safe to assume all of these numbers are represented in each line. Assumption has been tested against all numbers. 
    $easyNumbers = $valueSection | Where-Object {$_.length -eq 2 -or $_.length -eq 4 -or $_.length -eq 3 -or $_.length -eq 7}
    foreach($easyVal in $easyNumbers) {
        switch ($easyVal.length) {
            2 { $expected[1] = $easyVal }
            4 { $expected[4] = $easyVal }
            3 { $expected[7] = $easyVal }
            7 { $expected[8] = $easyVal }
        }
    }
    
    $fiveSections = $valueSection | Where-Object {$_.length -eq 5}
    $sixSections = $valueSection | Where-Object {$_.length -eq 6}

    # Process the easy win of '3' as it is the only 5 char with both chars of 1 in it. Similar for 6 being the only 6 char *without* both chars of 1 in it
    $expected[3] = $fiveSections | Where-Object {$_.Contains($expected[1][0]) -and $_.Contains($expected[1][1])} | Select-Object -First 1
    $expected[6] = $sixSections | Where-Object {$_.Contains($expected[1][0]) -xor $_.Contains($expected[1][1])} | Select-Object -First 1

    # Now that we have 3, we can also get 9 by result, as it is the only outstanding 6 char identifier which also holds all characters in 3. 
    # By doing this we also get 0 implictly, since it will be the last remaining 6 char identifier.
    $expected[9] = $sixSections | Where-Object {$_.Contains($expected[3][0]) -and $_.Contains($expected[3][1]) -and $_.Contains($expected[3][2]) -and $_.Contains($expected[3][3]) -and $_.Contains($expected[3][4])} | Select-Object -First 1
    $expected[0] = $sixSections | Where-Object {$_ -ne $expected[6] -and $_ -ne $expected[9]} | Select-Object -First 1
    
    # Now let's get the 5 from the fact it's the only number with 1 char different from 6. And 2 will be the last possible 5 length digit.
    foreach ($charSegment in $fiveSections) {
        $distinct = ($charSegment + $expected[6]).ToCharArray() | Sort-Object | Get-Unique
        if ($distinct.Length -eq 6) {
            $expected[5] = $charSegment
            break
        }
    }
    $expected[2] = $fiveSections | Where-Object {$_ -ne $expected[5] -and $_ -ne $expected[3]} | Select-Object -First 1
    
    $outputSection = $splitLine[1].Split(' ')
    $outputValue = 0
    foreach ($digit in $outputSection) {
        $outputValue *= 10
        switch ($digit.length) {
            2 { $outputValue += 1 }
            3 { $outputValue += 7 }
            4 { $outputValue += 4 }
            7 { $outputValue += 8 }

            5 {
                $twoValid = $true
                $threeValid = $true
                foreach($char in $digit.ToCharArray()) {
                    $twoValid = $twoValid -and $expected[2].Contains($char)
                    $threeValid = $threeValid -and $expected[3].Contains($char)
                }
                
                if ($twoValid) { $outputValue += 2 }
                elseif ($threeValid) { $outputValue += 3 }
                else { $outputValue += 5 }  #Only other valid entry
            }

            6 {
                $sixValid = $true
                $nineValid = $true
                foreach($char in $digit.ToCharArray()) {
                    $sixValid = $sixValid -and $expected[6].Contains($char)
                    $nineValid = $nineValid -and $expected[9].Contains($char)
                }
                
                if ($sixValid) { $outputValue += 6 }
                elseif ($nineValid) { $outputValue += 9 }
                #Only other valid entry would be 0, so ignore it.
            }
        }
    }
    $combinedOutput += $outputValue
}

Write-Output "Part Two Solution: $combinedOutput"