# Define the base save path
$savePath = ".\savedata\0"

# Make sure the folder exists
New-Item -ItemType Directory -Force -Path "$($savePath)\shows"

# Weekly show files
$days = @("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
foreach ($day in $days) {
    $file = Join-Path $savePath "$day.json"
    '{}' | Out-File -FilePath $file -Encoding utf8
}

# Monthly event files
# "$($savePath)\shows"
$months = @("january","february","march","april","may","june",
            "july","august","september","october","november","december")
foreach ($month in $months) {
    $file = Join-Path $savePath "$month.json"
    '{}' | Out-File -FilePath $file -Encoding utf8
}
