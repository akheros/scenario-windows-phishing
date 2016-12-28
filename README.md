This scenario showcases a workstation user opening a file containing a malware.


## Installation

This scenario requires a Windows XP VM with WinRM installed. See 
[here](https://github.com/akheros/moirai/wiki/How-to-get-a-Windows-XP-box-in-Vagrant) 
on how to do that. This VM should also have Adobe Acrobat 9 installed. The 
install file is in the `install` directory.

The second VM should have metasploit and pupy installed. Pupy must be patched in 
order to execute more than one module with the `run_module` directive. Copy the 
`install/PupyTriggers.py` to where pupy is installed, typically 
`/usr/share/pupy/pupy/pupylib/PupyTriggers.py`.


## Running the scenario

This scenario actually involves user interaction at the beginning because 
opening the file `infected.pdf` displays dialogs. The file should be opened 
about 10 seconds after the task `msfconsole/msfconsole -r ~/record.rc` starts. 
Msfconsole will actually wait for 30 seconds so there is a bit of leeway. When 
the file opens, the first dialog asks `Specify a file to extract to`, click 
`Save`. In the second dialog, `Launch File`, click `Open`. And then, you're good 
to go.

