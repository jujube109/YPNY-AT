ControlFocus("打开","","Edit1")
WinWait("[CLASS:#32770]","",10)
ControlSetText("打开","","Edit1", @ScriptDir &  "\Images\1.jpg")
Sleep(2000)
ControlClick("打开","","Button1");
