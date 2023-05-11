$FullRoster = Import-Csv -Path ".\Roster.csv"
$Angles     = Import-Csv -Path ".\Angles.csv"


#$Roster.psobject.properties.where({!$_.Value}).foreach{$_.Value = $null}
$TagTeams = $FullRoster | Where-Object -filterscript {($_.BRAND -ne 'Retired') -and ($_.BRAND -ne 'Inactive') -and ($_.BRAND -ne $null) -and ($_.TAGTEAM -ne '')}
$Superstars = $FullRoster | Where-Object -filterscript {($_.BRAND -ne 'Retired') -and ($_.BRAND -ne 'Inactive') -and ($_.BRAND -ne $null) -and ($_.TAGTEAM -eq '')}
$Brands = $FullRoster | Where-Object -FilterScript {($_.BRAND -ne '')} | Select-Object -Property BRAND -Unique
#Separate tag teams
ForEach ( $Wrestler in $TagTeams ) { $Wrestler.SUPERSTAR = $Wrestler.TAGTEAM }
$TagDivision = $TagTeams | Select-Object -Property * -Unique

#Separate tag teams
ForEach ( $Wrestler in $TagTeams ) { $Wrestler.SUPERSTAR = $Wrestler.TAGTEAM }
$TagTeams = $TagTeams | Select-Object -Property * -Unique


# Select roster division...
# HAS TO BE OUTSIDE of selection
$Gender = Get-Random ("M","F")
$Division = Get-Random ("Singles","Tag")
if ($Gender -eq 'M') { Write-Host "Men's $Division Divison" }
if ($Gender -eq 'F') { Write-Host "Women's $Division Divison" }


function Book-Angle {
	[CmdletBinding()]
    param(
        [Parameter()]
		$Participants = 2
	)

    # Obey roster boundary for gender
    $FilteredRoster = $FilteredRoster | Where-Object -FilterScript {( $_.SEX -eq "$Gender" )}
    
    # Obey roster boundary for division
    if ( $Division -eq 'Tag' ) { 
        $FilteredRoster = $FilteredRoster | Where-Object -FilterScript {( $_.TAGTEAM -ne '' )}
     } else {  
        $FilteredRoster = $FilteredRoster | Where-Object -FilterScript {( $_.TAGTEAM -eq '' )}
     }


    #Pick an angle at random
    $Angle = $Angles | Where-Object -FilterScript {( $Angles.PARTICIPANTS -eq $Participants)} | Get-Random
    
    #Start count
    $count = $Participants - $Participants

    #Select wrestlers for the angle based on count
    $Role = @()
    While ($Role.length -lt $Participants) {
        #Increment Count
        $Count = $Count + 1

        #Pull Role command from CSV and set it up
        $RoleNumber = "Role$count"
        $RoleCMD = $Angle.$rolenumber

        $SelectRole = IF ( $RoleCMD -eq '' ) { Invoke-Expression 'Wrestler' } else { Invoke-Expression "$RoleCMD" }
        $Role += $SelectRole
    }

    #build output here
    Invoke-Expression $Angle.Description
}


# BETTER FILTERING WITH SWITCHES

function Wrestler {
    [CmdletBinding()]
    param(
    [switch]$Face,
    [switch]$Heel,
    [switch]$MainEvent,
    [switch]$UpperMidCard,
    [switch]$MidCard,
    [switch]$Jobber,
    [switch]$FanFavorite,
    [switch]$Legend,
    [switch]$Manager,
    [switch]$Authority,
    [switch]$Partner
    )
 
    # Import roster for processing
    $FilteredRoster = $FullRoster

    # Obey roster boundary for gender
    $FilteredRoster = $FilteredRoster | Where-Object -FilterScript {( $_.SEX -eq "$Gender" )}
    
    # Obey roster boundary for division
    if ( $Division -eq 'Tag' ) { 
        $FilteredRoster = $FilteredRoster | Where-Object -FilterScript {( $_.TAGTEAM -ne '' )}
     } else {  
        $FilteredRoster = $FilteredRoster | Where-Object -FilterScript {( $_.TAGTEAM -eq '' )}
     }

    # Modify the roster by switches
    # By alignments...
    if ($Face.IsPresent) { $FilteredRoster = $FilteredRoster | Where-Object -FilterScript {($_.ALIGNMENT -eq 'Face')}}
    if ($Heel.IsPresent) { $FilteredRoster = $FilteredRoster | Where-Object -FilterScript {($_.ALIGNMENT -eq 'Heel')}}
    #By roles...
    if ($MainEvent.IsPresent) { $FilteredRoster = $FilteredRoster | Where-Object -FilterScript {($_.ROLE -eq 'MainEvent')}}
    if ($UpperMidCard.IsPresent) { $FilteredRoster = $FilteredRoster | Where-Object -FilterScript {($_.ROLE -eq 'UpperMidCard')}}
    if ($MidCard.IsPresent) { $FilteredRoster = $FilteredRoster | Where-Object -FilterScript {($_.ROLE -eq 'MidCard')}}
    if ($Jobber.IsPresent) { $FilteredRoster = $FilteredRoster | Where-Object -FilterScript {($_.ROLE -eq 'Jobber')}}
    if ($Manager.IsPresent) { $FilteredRoster = $FilteredRoster | Where-Object -FilterScript {($_.ROLE -eq 'Manager')}}
    if ($Legend.IsPresent) { $FilteredRoster = $FilteredRoster | Where-Object -FilterScript {($_.ROLE -eq 'Legend')}}
    if ($Authority.IsPresent) { $FilteredRoster = $FilteredRoster | Where-Object -FilterScript {($_.ROLE -eq 'Authority')}}
    if ($FanFavorite.IsPresent) { $FilteredRoster = $FilteredRoster | Where-Object -FilterScript {($_.ROLE -eq 'FanFavorite')}}
    if ($Partner.IsPresent) { $FilteredRoster = $FilteredRoster | Where-Object -FilterScript {($_.ROLE -eq 'FanFavorite')}}


    # Get an item from the array and convert from a generic object to a string
    if ( $Division -ne 'Tag' ) {
        $Selection = $FilteredRoster | Select-Object -ExpandProperty SUPERSTAR | Get-Random 
    }
    if ( $Division -eq 'Tag' ) {
        $Selection = $FilteredRoster | Select-Object -ExpandProperty TAGTEAM | Get-Random
    }
    
    return $selection
    }

 }
}