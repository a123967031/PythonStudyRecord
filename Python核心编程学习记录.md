- method for printing dict char
```Python
dict2 = {'name': 'venus', 'port': 6969}
print 'host %(name)s is running on port %(port)d' %dict2
```
**Python核心编程 P167**

- dict中的sorted()方法使用
```Python
dict2 = {'name': 'venus', 'port': 6969}
for eachKey in sorted(dict2):
  print 'dict2 key', eachKey, 'has value', dict2[eachKey]
```
**Python核心编程 P173**

- dict.update() and dict.fromkeys() method
`dicta.update({}.fromkeys(srcstr[len(dststr):]))`

- list.append()分辨错误实例和正确实例
```Python
mylist = mylist.append(mychr) #error
mylist.append(mychr) #correct
```

- ['m', 'n', 'o', None, None, None, 'g', 'h', 'i']中NoneType使用join方法
```Python
mylist = ['m', 'n', 'o', None, None, None, 'g', 'h', 'i']
''.join(mylist)
TypeError: sequence item 3: expected string, NoneType found
```

- 过滤None字符
`mylist = [ch for ch in mylist if ch]`
