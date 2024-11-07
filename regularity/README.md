└─$ pwn checksec regularity
[*] '/home/kali/share/htb/challenges/regularity/pwn_regularity/regularity'
    Arch:       amd64-64-little
    RELRO:      No RELRO
    Stack:      No canary found
    NX:         NX unknown - GNU_STACK missing
    PIE:        No PIE (0x400000)
    Stack:      Executable
    RWX:        Has RWX segments
    Stripped:   No

└─$ ldd regularity  
        not a dynamic executable
        
![Screenshot_2024-11-07_17-30-25](https://github.com/user-attachments/assets/a06d0f81-3b05-4808-b0ad-45c1155613fa)
