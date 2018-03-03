debugger mode (-d)
without -d is static analysis

======================
aaa	          //analyse

s sym.main		//seek
pdf			//disassemble

sym.imp.printf	 //means imported function printf

=========================
//useful debugging commands

db sym.main       //break main
dc                //continue

//do the above before going into Visual mode

ds		  //step
dso		  //step over

pfi @ rbp-0x4	  //print integer of local variable a $rbp-0x4
pfx @ rbp-0x4	  //print hex ...
ps @ rbp-0x4	  //print string
ps @ 0x004006d3   //print string at this addr

px @ address	   //hexdump
pxw @ address		//word hexdump
pxq @ address		//quad hexdump

=======================
//Visual modes

V		  //visual mode
p		  //cycle different visual mode

V -> p -> p     //good for debugging (got register, disassembly)
s                    //step, will highlight current address
:		//enter command
[enter]		//back to visual

shift + r	  //visual mode random color

====================
VV		  //visual graph
