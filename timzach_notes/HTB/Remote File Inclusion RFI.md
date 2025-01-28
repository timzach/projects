Aus HTB Starting Point Responder2_4

RFI or Remote File Inclusion is similar to LFI but in this case it is possible for an attacker to load a remote
file on the host using protocols like HTTP, FTP etc.
We test the page parameter to see if we can include files on the target system in the server response. We
will test with some commonly known files that will have the same name across networks, Windows
domains, and systems which can be found here. One of the most common files that a penetration tester
might attempt to access on a Windows machine to verify LFI is the hosts file,
WINDOWS\System32\drivers\etc\hosts (this file aids in the local translation of host names to IP
addresses). The ../ string is used to traverse back a directory, one at a time. Thus multiple ../ strings are
included in the URL so that the file handler on the server traverses back to the base directory i.e. C:\ .
http://unika.htb/index.php?page=../../../../../../../../windows/system32/drivers/etc/hosts

New technology lan manager ntlm
