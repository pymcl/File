text = '''\
A problem has been detected and windows has been shut down to prevent damaqe to your computer. 

Attempt to reset the display driver and recover from timeout failed.If this is the first time you've seen this stop error screen,restart your computer. If this screen appears again,followthese steps:

Check to make sure any new hardware or software is properly installed.If this is a new installation, ask your hardware or software manufacturer for any windows updates you might need.

If problems continue, disable or remove any newly installed hardware or software. Disable BIOS memory options such as caching or shadowing. If you need to use Safe Mode to remove or disable components, restart your computer, press F8 to select Advanced Startup Options, and then select Safe Mode.

Technical information:

***** STOP: 0X00000116 (OXFFFFFA8OO9C644EO, OXFFXXF88OO7O73404,0x0000054000000000, 0 XOOOOOOOOOOOOOO12)
**** nvlddmkm.sys - Address FFFFF88007013404 base at FFFFF88006EDE000, Datestamp 513e93218

Collecting data for crash dump ...
Initializing disk for crash dump ...
Beginning dump of physical memory...

'''
'''
pop_text = [
'Technical information:',
'***** STOP: 0X00000116 (OXFFFFFA8OO9C644EO, OXFFXXF88OO7O73404,0x0000054000000000, 0 XOOOOOOOOOOOOOO12)',
'**** nvlddmkm.sys - Address FFFFF88007013404 base at FFFFF88006EDE000, Datestamp 513e93218',
'Collecting data for crash dump ...',
'Initializing disk for crash dump ...',
'Beginning dump of physical memory...',
'Dumping physical memory to disk: {0}']
'''
pop_text = 'Dumping physical memory to disk: {0}'
