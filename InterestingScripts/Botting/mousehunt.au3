#cs ----------------------------------------------------------------------------

 AutoIt Version: 3.3.14.2
 Author:         myName

 Script Function:
	Template AutoIt script.

#ce ----------------------------------------------------------------------------

; Script Start - Add your code below here

Global $numCheese=10, $count=0
Global $currentWin

Sleep(3000)

For $x = 0 To $numCheese Step 1
   $currentWin = WinGetTitle("[ACTIVE]")
   WinActivate("MouseHunt on Facebook - Google Chrome")
   Sleep(500)
   Send("{HOME}")
   Sleep(250)
   MouseClick("left", 636, 230)		;no banner
   ;MouseClick("left", 638, 309)	;got banner
   WinActivate($currentWin)
   $count+=1
   ConsoleWrite($count)
   Sleep(15*60 * 1000 + 250)
Next
MsgBox(0, "finished", "task completed")