# BrainFuDGE code examples
## Uses of loops and their logic:
**NEED TO KNOW:**
- Loops run until the memory index you were addressing when the loop was initialised is equal to zero.
- You can change your memory pointer during the loop which does not effect the address the loop checks when it reaches its end (where it decides whether to return to the start of the loop or continue).
- Yes you can have infinately running loops lol.

**Brain FuDGE Example:**
```
+++++[.>+++++[.-]<-]
```

**Same Code In Python:**
```python
Mem[0] = 5
while Mem[0] != 0:
  print(Mem[0])
  Mem[1] = 5
  while Mem[1] != 0:
    print(Mem[1])
    Mem[1] -= 1
  Mem[0] -= 1
```
