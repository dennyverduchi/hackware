La challenge metteva a disposizione un binario da analizzare.
```
$ pwn checksec regularity
[*] '/home/kali/share/htb/challenges/regularity/pwn_regularity/regularity'
    Arch:       amd64-64-little
    RELRO:      No RELRO
    Stack:      No canary found
    NX:         NX unknown - GNU_STACK missing
    PIE:        No PIE (0x400000)
    Stack:      Executable
    RWX:        Has RWX segments
    Stripped:   No
```
```
$ ldd regularity  
        not a dynamic executable
```
Analizzo il binario su Binary Ninja:
![bin_start](https://github.com/user-attachments/assets/7dd2aec3-02ed-4ffc-ae8d-f8025f8a39de)

Il flusso sembra essere chiaro, dentro _start ci sono 3 chiamate a funzione: write, read e ancora write.
Analizzo le funzioni chiamate:
![bin_read_write](https://github.com/user-attachments/assets/95e54092-b44e-47aa-8f80-04dcf098d7bb)

Nella funzione read sembra che vengano liberati 0x100 bytes per far spazio al buffer. Quando la syscall viene chiamata per leggere il buffer tuttavia, vengono passati 0x110 bytes!
Per sfruttare questo overflow e aggirare il problema ASLR è necessario sapre quale sarà l'indirizzo dove viene locato il buffer:
```
$ gdb -q regularity
Reading symbols from regularity...
(No debugging symbols found in regularity)
(gdb) b *0x40106e
Breakpoint 1 at 0x40106e
(gdb) r
Starting program: /home/kali/htb/challenges/regularity/pwn_regularity/regularity 
Hello, Survivor. Anything new these days?
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

Breakpoint 1, 0x000000000040106e in read ()
(gdb)  x/8gx $rsp-0x100
0x7fffffffdd78: 0x4141414141414141      0x4141414141414141
0x7fffffffdd88: 0x4141414141414141      0x4141414141414141
0x7fffffffdd98: 0x4141414141414141      0x4141414141414141
0x7fffffffdda8: 0x4141414141414141      0x0000000a41414141
```
Quindi 0x7fffffffdd78 è l'indirizzo dove è locato il buffer. Controllo i registri:
```
(gdb) info reg
...
rsi            0x7fffffffdd78      140737488346488
...
```
rsi punta proprio all'indirizzo del buffer! Come abbiamo visto in _start rsi viene utilizzato per uscire con l'istruzione:

mov rsi, exit
jmp rsi {exit}

A questo punto posso sovrascrivere il puntatore di uscita della funzione 'read' (0x40106e) con l'indirizzo di 'jmp rsi' per saltare alla mia shellcode.
![Screenshot_2024-11-07_17-30-25](https://github.com/user-attachments/assets/a06d0f81-3b05-4808-b0ad-45c1155613fa)
