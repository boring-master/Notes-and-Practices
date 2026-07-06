

# 算法分析
## 什么是算法分析
### 程序和算法的区别
算法是对问题解决的分步描述  
程序则是采用某种编程语言实现的算法，同一个算法通过不同的程序员采用不同的编程语言，能产生很多程序
### 计算资源指标
一种是算法解决问题过程中需要的存储空间或内存，另一种是算法的执行时间
### 运行时间检测
利用Python的time模块，在算法开始前和结束后分别记录系统时间，即可得到运行时间
```Python
import time
def sumf(n):
    start = time.time()
    Sum = 0
    for i in range(1,n+1):
        Sum += i
    end = time.time()
    return Sum, end-start
```
## 大O表示法
### 算法时间度量指标
一个算法所实施的操作数量或步骤数可作为独立于具体程序/机器的度量指标，赋值语句是一个合适的选择

一条赋值语句同时包含了（表达式）计算和（变量）存储两个基本资源。    
仔细观察程序设计语言特性，除了与计算资源无关的定义语句外，主要就是三种控制流语句和赋值语句，而控制流仅仅起了组织语句的作用，并不实施处理。
### 赋值语句执行次数
对于sumf的问题规模$n$，赋值语句数量$T(n)=n+1$
### 问题规模影响算法执行时间
***问题规模***：影响算法执行时间的主要因素

在前n个整数累计求和的算法中，需要累计的整数个数合适作为问题规模的指标  
算法分析的目标是要找出***问题规模***会怎么影响一个算法的执行时间
### 数量级函数 Order of Magnitude
基本操作数量函数$T(n)$的精确值并不是特别重要，重要的是$T(n)$中起决定性因素的主导部分
> 用动态的眼光看，就是当问题规模增大的时候，$T(n)$中的一些部分会盖过其它部分的贡献

数量级函数描述了$T(n)$中随着n增加而增加速度最快的主导部分，称作“大O”表示法，记作$O(f(n))$，其中$f(n)$表示$T(n)$中的主导部分
### 确定运行时间数量级大O的方法
#### 例1：
$T(n)=1+n$

当$n$增大时，常数$1$在最终结果中显得越来越无足轻重  
所以可以去掉$1$，保留$n$作为主要部分，运行时间数量级就是$O(n)$
#### 例2：
$T(n)=5n^2+27n+1005$

当$n$很小时，常数$1005$其决定性作用  
但当$n$越来越大，$n^2$项就越来越重要，其它两项对结果的影响则越来越小  
同样，$n^2$项中的系数$5$，对于$n^2$的增长速度来说也影响不大  
所以可以在数量级中去掉$27n+1005$，以及系数$5$的部分，确定为$O(n^2)$
### 影响算法运行时间的其它因素
有时决定运行时间的不仅是问题规模，某些具体数据也会影响算法运行时间，分为*最好*、*最差*和*平均*情况，***平均***状况体现了算法的主流性能  
对算法的分析要看主流，而不被某几种特定的运行状况所迷惑
### 常见的大O数量级函数
通常当$n$较小时，难以确定其数量级  
当$n$增长到较大时，容易看出其主要变化量级
$f(n)$|名称
---|---
$1$|常数
$log(n)$|对数
$n$|线性
$n*log(n)$|对数线性
$n^2$|平方
$n^3$|立方
$2^n$|指数
### 从代码分析确定执行时间数量级函数
代码赋值语句可以分为4个部分  
$T(n) = 3+3n^2+2n+1 = 3n^2+2n+4$
<img src="./images/从代码分析数量级函数.png" style="max-width: 50%; height: auto;"  alt="从代码分析数量级函数"/>

仅保留最高阶项$n^2$，去掉所有系数数量级为$O(n^2)$
### 其它算法复杂度表示法
#### 大O表示法
表示了所有上限中最小的那个上限
#### 大𝛀表示法
表示了所有下限中最大的那个下限  
$f(n)=\Omega(g(n))$当且仅当$g(n)=O(f(n))$
#### 大𝚹表示法
如果上下限相同，那么就可以用大$\Theta$表示  
$f(n)=\Theta(g(n))$当且仅当$f(n)=O(g(n))$且$f(n)=\Omega(g(n))$
## “变位词”判断问题
### 问题描述
所谓“变位词”是指两个词之间存在组成字母的重新排列关系，如：heart和earth，python和typhon

为了简单起见，假设参与判断的两个词仅由小写字母构成，而且长度相等
### 解题目标
写一个bool函数，以两个词作为参数，返回这两个词是否变位词
### 解法1-逐字检查
#### 解法思路
将词1中的字符逐个到词2中检查是否存在，存在就“打勾”标记（防止重复检查）  
如果每个字符都能找到，则两个词是变位词只要有1个字符找不到，就不是变位词
#### 程序技巧
实现“打勾”标记：将词2对应字符设为None。由于字符串是不可变类型，需要先复制到列表中
#### 具体程序
```Python
def anagramSolution1(s1,s2):
    alist = list(s2)
    pos1 = 0
    stillOK = True
    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            alist[pos2] = None
        else:
            stillOK = False
        pos1 += 1
    return stillOK
```
#### 算法分析
**问题规模**：词中包含的字符个数n  
主要部分在于两重循环：外层循环遍历s1每个字符，将内层循环执行n次，而内层循环在s2中查找字符，每个字符的对比次数，分别是1、2…n中的一个，而且各不相同  
所以总执行次数是1+2+3+……+n  
可知其数量级为$O(n^2)$
### 解法2-排序比较
#### 解题思路
将两个字符串都按照字母顺序排好序，再逐个字符对比是否相同  
如果相同则是变位词，有任何不同就不是变位词
#### 具体程序
```Python
def anagramSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()
    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False
    return matches
```
#### 算法分析
粗看上去，本算法只有一个循环，最多执行n次，数量级是$O(n)$  
但循环前面的两个sort并不是无代价的  
如果查询下后面的章节，会发现排序算法采用不同的解决方案，其运行时间数量级差不多是$O(n^2)$或者$O(nlog(n))$，大过循环的$O(n)$  
所以本算法时间主导的步骤是排序步骤  
本算法的运行时间数量级就等于排序过程的数量级$O(nlog(n))$
### 解法3-暴力法
#### 解题思路
穷尽所有可能组合  
将s1中出现的字符进行全排列，再查看s2是否出现在全排列列表中  
这里最大困难是产生s1所有字符的全排列  
根据组合数学的结论，如果n个字符进行全排列，其所有可能的字符串个数为$n!$  
已知$n!$的增长速度甚至超过$2^n$

结论：暴力法恐怕不能算是个好算法
### 解法4-计数比较
#### 解题思路
对比两个词中每个字母出现的次数，如果26个字母出现的次数都相同的话，这两个字符串就一定是变位词
#### 具体做法
为每个词设置一个26位的计数器，先检查每个词，在计数器中设定好每个字母出现的次数  
计数完成后，进入比较阶段，看两个字符串的计数器是否相同，如果相同则输出是变位词的结论
#### 具体程序
```Python
def anagramSolution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1
    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j += 1
        else:
            stillOK = False
    return stillOK
```
#### 算法分析
计数比较算法中有3个循环迭代，但不像解法1那样存在嵌套循坏

前两个循环用于对字符串进行计数，操作次数等于字符串长度n  
第3个循环用于计数器比较，操作次数总是26次  
所以总操作次数$T(n)=2n+26$，其数量级为$O(n)$

这是一个线性数量级的算法，是4个变位词判断算法中性能最优的

> 注意：本算法依赖于两个长度为26的计数器列表，来保存字符计数，这相比前3个算法需要更多的存储空间  
> 如果考虑由大字符集构成的词（如中文具有上万不同字符），还会需要更多存储空间。
> 牺牲存储空间来换取运行时间，或者相反，这种在时间空间之间的取舍和权衡，在选择问题解法的过程中经常会出现。
## Python数据类型的性能
### 对比list和dict的操作

类型|list|dict
---|---|---
索引|自然数i|不可变类型值key
添加|append、extend、insert|b[k]=v
删除|pop、remove*|pop
更新|a[i]=v|b[k]=v
正查|a[i]、a[i:j]|b[k]、copy
反查|index(v)、count(v)|无
其他|reverse、sort|has_key、update

### list数据类型
让最常用的操作性能最好，牺牲不太常用的操作
> 80/20准则：80%的功能其使用率只有20%
#### 常用操作性能
最常用的是：按索引取值和赋值（v=a[i]，a[i]=v）

> 由于列表的随机访问特性，这两个操作执行时间与列表大小无关，均为$O(1)$

另一个是列表增长，可以选择append()和__add__()“+”

> `lst.append(v)`，执行时间是$O(1)$
> `lst= lst+ [v]`，执行时间是$O(n+k)$，其中k是被加的列表长度

#### 4种生成前n个整数列表的方法
首先是循环连接列表（+）方式生成
```Python
def test1():
    l = []
    for i in range(1000):
        l += [i]
```
然后是用append方法添加元素生成
```Python
def test2():
    l = []
    for i in range(1000):
        l.append(i)
```
接着用列表推导式来做
```Python
def test3():
    l = [i for i in range(1000)]
```
最后是range函数调用转成列表
```Python
def test4():
    l = list(range(1000))
```
#### 使用timeit模块对函数计时
创建一个Timer对象，指定需要反复运行的语句和只需要运行一次的“安装语句”  
然后调用这个对象的timeit方法，其中可以指定反复运行多少次
```Python
from timeit import Timer
t1 = Timer('test1()', 'from __main__ import test1')
print(f'contact {t1.timeit(number=1000)} seconds\n')   

t2 = Timer('test2()', 'from __main__ import test2')
print(f'append {t2.timeit(number=1000)} seconds\n')

t3 = Timer('test3()', 'from __main__ import test3')
print(f'comprehension {t3.timeit(number=1000)} seconds\n')

t4 = Timer('test4()', 'from __main__ import test4')
print(f'list range {t4.timeit(number=1000)} seconds\n')
```
```
contact 0.043239699909463525 seconds

append 0.018909000093117356 seconds

comprehension 0.013164800126105547 seconds

list range 0.008927199989557266 seconds
```
可以看到，4种方法运行时间差别很大。列表连接（contact）最慢，list range最快，
#### List基本操作的大O数量级

<img src="./images/List基本操作的大O数量级.png" style="max-width: 50%; height: auto;"  alt="List基本操作的大O数量级"/>

#### list.pop的计时试验
注意到pop这个操作
- `pop()`从列表末尾移除元素，$O(1)$
- `pop(i)`从列表中部移除元素，$O(n)$

**原因在于Python所选择的实现方法**  
从中部移除元素的话，要把移除元素后面的元素全部向前挪位复制一遍，这个看起来有点笨拙，但这种实现方法能够保证列表按索引取值和赋值的操作很快，达到$O(1)$ 

**为了验证表中的大O数量级，我们把两种情况下的pop操作来实际计时对比**  
相对同一个大小的list，分别调用`pop()`和`pop(0)`

**对不同大小的list做计时，期望的结果是**  
`pop()`的时间不随list大小变化，`pop(0)`的时间随着list变大而变长

我们通过改变列表的大小来测试两个操作的增长趋势
```Python
import timeit
popzero = timeit.Timer('x.pop(0)', 'from __main__ import x')
popend = timeit.Timer('x.pop()', 'from __main__ import x')
print('pop(0)    pop()')
for i in range(1000000,100000001,1000000):
    x = list(range(i))
    pt = popend.timeit(number=1000)
    pz = popzero.timeit(number=1000)
    print(f'{pz:7.5f}   {pt:7.5f}')
```
```
pop(0)    pop()
0.35184   0.00002
0.71082   0.00002
1.04331   0.00002
1.39212   0.00003
1.74167   0.00002
2.22155   0.00002
···
```
### dict数据类型
**字典与列表不同，根据关键码（key）找到数据项，而列表是根据位置（index）**  
最常用的取值get和赋值set，其性能为$O(1)$  
另一个重要操作contains(in)是判断字典中是否存在某个关键码（key），这个性能也是$O(1)$
#### list和dict的in操作对比
**设计一个性能试验来验证list中检索一个值，以及dict中检索一个值的计时对比**  
生成包含连续值的list和包含连续关键码key的dict，用随机数来检验操作符in的耗时
```Python
import timeit
import random
for i in range(10000,1000001,20000):
    t = timeit.Timer(f'random.randrange({i}) in x', 'from __main__ import random, x')
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print(f'{i},{lst_time:11.5f},{d_time:11.5f}')
```
```
···
510000,    1.16319,    0.00045
530000,    1.18504,    0.00045
550000,    1.24642,    0.00050
570000,    1.27892,    0.00051
590000,    1.30099,    0.00050
610000,    1.35568,    0.00052
630000,    1.42419,    0.00051
···
```
可见字典的执行时间与规模无关，是常数（在 0.0001x 秒级别）  
而列表的执行时间则随着列表的规模加大而线性上升
# 基本结构
## 什么是线性结构
**线性结构是一种有序数据项的集合，其中每个数据项都有*唯一*的前驱和后继**  
除了第一个没有前驱，最后一个没有后继  
新的数据项加入到数据集中时，只会加入到原有某个数据项之前或之后具有这种性质的数据集，就称为***线性结构***

线性结构总有两端，在不同的情况下，两端的称呼也不同，有时候称为“左”“右”端、“前”“后”端、“顶”“底”端

![](./images/线性结构.png)

**两端的称呼并不是关键，不同线性结构的关键区别在于数据项增减的方式**  
有的结构只允许数据项从一端添加，而有的结构则允许数据项从两端移除

**我们从4个最简单但功能强大的结构入手，开始研究数据结构**  

***栈Stack，队列Queue，双端队列Deque和列表List***

这些数据集的共同点在于，数据项之间只存在先后的次序关系，都是线性结构
## 栈抽象数据类型及Python实现
### 什么是栈Stack
**一种有次序的数据项集合，在栈中，数据项的加入和移除都仅发生在同一端**  
这一端叫栈“顶top”，另一端叫栈“底base”

日常生活中有很多栈的应用，包括盘子、托盘、书堆等等

**距离栈底越近的数据项，留在栈中的时间就越长**  
而最新加入栈的数据项会被最先移除

**这种次序通常称为“后进先出LIFO”：Last in First out**  
这是一种基于数据项保存时间的次序，时间越短的离栈顶越近，而时间越长的离栈底越近
### 抽象数据类型Stack
抽象数据类型“栈”是一个有次序的数据集，每个数据项仅从“栈顶”一端加入到数据集中、从数据集中移除，栈具有后进先出LIFO的特性

**抽象数据类型“栈”定义为如下的操作**
- `Stack()`：创建一个空栈，不包含任何数据项
- `push(item)`：将item加入栈顶，无返回值
- `pop()`：将栈顶数据项移除，并返回，栈被修改
- `peek()`：“窥视”栈顶数据项，返回栈顶的数据项但不移除，栈不被修改
- `isEmpty()`：返回栈是否为空栈
- `size()`：返回栈中有多少个数据项

#### 操作样例
Stack Operation|Stack Contents|Return Value
---|---|---
s = Stack()|[]|Stack object
s.isEmpty|[]|True
s.push(4)|[4]|
s.push('dog')|[4, 'dog']|
s.peek()|[4, 'dog']|'dog'
s.push(True)|[4, 'dog', True]|
s.size()|[4, 'dog', True]|3
s.isEmpty()|[4, 'dog', True]|False
s.push(8.4)|[4, 'dog', True, 8.4]|
s.pop()|[4, 'dog', True]|8.4
s.pop()|[4, 'dog']|True
s.size()|[4, 'dog']|2

### 用Python实现ADT(Abstract Data Type) Stack
**Python的面向对象机制，可以用来实现用户自定义类型**  
将ADT Stack的操作实现为Class的方法  
由于Stack是一个数据集，所以可以采用Python的原生数据集来实现，我们选用最常用的数据集list来实现
```Python
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
```
见[Stack.py](./code/栈/Stack.py)
## 栈的应用：简单括号匹配
**括号的使用必须遵循 “平衡”规则**
首先，每个开括号要恰好对应一个闭括号；其次，每对开闭括号要正确的嵌套
- 正确的括号：(()()()())，(((())))，(()((())()))
- 错误的括号：((((((())，()))，(()()(()

对括号是否正确匹配的识别，是很多语言编译器的基础算法
### 构造括号匹配识别算法
从左到右扫描括号串，最新打开的左括号，应该匹配最先遇到的右括号。这样，第一个左括号（最早打开），就应该匹配最后一个右括号（最后遇到）  
这种次序反转的识别，正好符合栈的特性
### 具体程序
```Python
from Stack import Stack
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False
print(parChecker('((()))'))     # True
print(parChecker('((()()()'))   # False
```
### 更多种括号的匹配
下面这些是匹配的
{ { ( [ ] [ ] ) } ( ) }，  
[ [ { { ( ( ) ) } } ] ]，  
[ ] [ ] [ ] ( ) { }

下面这些是不匹配的
( [ ) ]，   
( ( ( ) ] ) )，  
[ { ( ) ]
### 程序修改
```Python
from Stack import Stack
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False
def matches(open,close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)
print(parChecker('{{([][])}()}'))   # True
print(parChecker('[{(}]'))          # False
```
## 栈的应用：十进制转换为二进制
**所谓的“进制”，就是用多少个字符来表示整数**  
十进制是0～9这十个数字字符，二进制是0、1两个字符

**我们经常需要将整数在二进制和十进制之间转换**  
如：$(233)_{10}$的对应二进制数为$(11101001)_2$，具体是这样：  
$(233)_{10}=2×10^2+3×10^1+3×10^0$  
$(11101001)_2=1×2^7+1×2^6+1×2^5+0×2^4+1×2^3+0×2^2+0×2^1+1×2^0$

**十进制转换为二进制，采用的是“除以2求余数”的算法**  
将整数不断除以2，每次得到的余数就是由低到高的二进制位

![](./images/除以2求余数.png)

“除以2”的过程，得到的余数是从低到高的次序，而输出则是从高到低，所以需要一个栈来反转次序
### 具体程序
```Python
from Stack import Stack
def divideBy2(decNumber):
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2
    binString = ''
    while not remstack.isEmpty():
        binString += str(remstack.pop())
    return binString
print(divideBy2(42))    # 101010
```
### 扩展到更多进制转换
**十进制转换为二进制的算法，很容易可以扩展为转换到任意N进制**  
只需要将“除以2求余数”算法改为“除以N求余数”算法就可以

**计算机中另外两种常用的进制是八进制和十六进制**  
$(233)_{10}$等于$(351)_8$和$(E9)_{16}$  
$(351)_8=3×8^2+5×8^1+1×8^0$  
$(E9)_{16}=14×16^1+9×16^0$  

**主要的问题是如何表示八进制及十六进制**  
二进制有两个不同数字0、1  
十进制有十个不同数字0、1、2、3、4、5、6、7、8、9  
八进制可用八个不同数字0、1、2、3、4、5、6、7  
十六进制的十六个不同数字则是0、1、2、3、4、5、6、7、8、9、A、B、C、D、E、F
### 程序修改
```Python
from Stack import Stack
def baseConverter(decNumber,base):
    digits = '0123456789ABCDEF'
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base
    newString = ''
    while not remstack.isEmpty():
        newString += digits[remstack.pop()]
    return newString
print(baseConverter(25,2))  # 11001
print(baseConverter(25,16)) # 19
```
## 表达式转换
### 中缀表达式
我们通常看到的表达式象这样：B*C，很容易知道这是B乘以C  
这种操作符（operator）介于操作数（operand）中间的表示法，称为“中缀”表示法

**但有时候中缀表示法会引起混淆，如“A+B\*C”**  
是A+B然后再乘以C
还是B\*C然后再去加A？
### 中缀表达式中的优先级
**人们引入了操作符“优先级”的概念来消除混淆**  
规定高优先级的操作符先计算  
相同优先级的操作符从左到右依次计算  
这样A+B*C就没有疑义是A加上B与C的乘积

**同时引入了括号来表示强制优先级，括号的优先级最高，而且在嵌套的括号中，内层的优先级更高**  
这样(A+B)*C就是A与B的和再乘以C
### 全括号中缀表达式
**虽然人们已经习惯了这种表示法，但计算机处理最好是能明确规定所有的计算顺序，这样无需处理复杂的优先规则**

**引入全括号表达式：在所有的表达式项两边都加上括号**  
A+B\*C+D，应表示为((A+(B\*C))+D)
### 前缀和后缀表达式
**如果将表达式中操作符的位置稍移动一下，例如中缀表达式A+B**  
将操作符移到前面，变为“+AB”  
或者将操作符移到最后，变为“AB+”

**我们就得到了表达式的另外两种表示法：“*前缀*”和“*后缀*”表示法**

这样A+B\*C将变为前缀的“+A\*BC”，后缀的“ABC\*+”
### 前缀、中缀和后缀表达式
再来看中缀表达式“(A+B)\*C”，按照转换的规则，前缀表达式是“\*+ABC”，而后缀表达式是“AB+C\*”

神奇的事情发生了，在中缀表达式里必须的括号，在前缀和后缀表达式中消失了？

在前缀和后缀表达式中，操作符的次序完全决定了运算的次序，不再有混淆

所以在很多情况下，表达式的计算机表示都避免用复杂的中缀形式

**下面看更多的例子**
中缀表达式|前缀表达式|后缀表达式
---|---|---
A + B * C + D|++ A * B C D|A B C * + D +
(A + B) * (C + D)|* + A B + C D|A B + C D + *
A * B + C * D|+ * A B * C D|A B * C D * +
A + B + C + D|+ + + A B C D|A B + C + D +

### 中缀表达式转换为前缀和后缀形式
无论表达式多复杂，需要转换成前缀或者后缀，只需要两个步骤
1. 将中缀表达式转换为全括号形式
2. 将所有的操作符移动到子表达式所在的左括号（前缀）或者右括号（后缀）处，替代之，再删除所有的括号
### 通用的中缀转后缀算法
**来看中缀表达式A+B\*C，其对应的后缀表达式是ABC\*+**  
操作数ABC的顺序没有改变  
操作符的出现顺序，在后缀表达式中反转了  
由于*的优先级比+高，所以后缀表达式中操作符的出现顺序与运算次序一致

**在中缀表达式转换为后缀形式的处理过程中，操作符比操作数要晚输出**  
所以在扫描到对应的第二个操作数之前，需要把操作符先保存起来  

**而这些暂存的操作符，由于优先级的规则，还有可能要反转次序输出**
在A+B\*C中，+虽然先出现，但优先级比后面这个\*要低，所以它要等\*处理完后，才能再处理  

**这种反转特性，使得我们考虑用*栈*来保存暂时未处理的操作符**

**再看看(A+B)\*C，对应的后缀形式是AB+C\***  
这里+的输出比\*要早，主要是因为括号使得+的优先级提升，高于括号之外的\*

**回顾“全括号”表达式，后缀表达式中操作符应该出现在左括号对应的右括号位置**  
所以遇到左括号，要标记下，其后出现的操作符优先级提升了，一旦扫描到对应的右括号，就可以马上输出这个操作符

**总结下，在从左到右扫描逐个字符扫描中缀表达式的过程中，采用一个栈来暂存未处理的操作符**  
**这样，栈顶的操作符就是最近暂存进去的，当遇到一个新的操作符，就需要跟栈顶的操作符比较下优先级，再行处理**
#### 流程
后面的算法描述中，约定中缀表达式是由空格隔开的一系列单词（token）构成，操作符单词包括*/+-()而操作数单词则是单字母标识符A、B、C等

**首先，创建空栈opstack用于暂存操作符，空表postfixList用于保存后缀表达式**  
**将中缀表达式转换为单词（token）列表**
> A+B\*C =split=> ['A', '+', 'B', '*', 'C']

**从左到右扫描中缀表达式单词列表**
- 如果单词是操作数，则直接添加到后缀表达式列表的末尾
- 如果单词是左括号“(”，则压入opstack栈顶
- 如果单词是右括号“)”，则反复弹出opstack栈顶操作符，加入到输出列表末尾，直到碰到左括号
- 如果单词是操作符“*/+-”，则压入opstack栈顶

但在压入之前，要比较其与栈顶操作符的优先级
> 如果栈顶的高于或等于它，就要反复弹出栈顶操作符，加入到输出列表末尾，直到栈顶的操作符优先级低于它

**中缀表达式单词列表扫描结束后，把opstack栈中的所有剩余操作符依次弹出，添加到输出列表末尾**  
**把输出列表再用join方法合并成后缀表达式字符串，算法结束**
### 具体程序
```Python
from Stack import Stack
def infixToPostfix(infixexpr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.pop()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return ' '.join(postfixList)
```
## 后缀表达式求值
跟中缀转换为后缀问题不同，在对后缀表达式从左到右扫描的过程中，由于操作符在操作数的后面，所以要暂存操作数，在碰到操作符的时候，再将暂存的两个操作数进行实际的计算
> 仍然是栈的特性：操作符只作用于离它最近的两个操作数
### 流程
- 创建空栈operandStack用于暂存操作数
- 将后缀表达式用split方法解析为单词（token）的列表
- 从左到右扫描单词列表
  - 如果单词是一个操作数，将单词转换为整数int，压入operandStack栈顶
  - 如果单词是一个操作符（*/+-），就开始求值，从栈顶弹出2个操作数，先弹出的是右操作数，后弹出的是左操作数，计算后将值重新压入栈顶
- 单词列表扫描结束后，表达式的值就在栈顶
- 弹出栈顶的值，返回
### 具体程序
```Python
from Stack import Stack
def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in '0123456789':
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()
def doMath(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2
```
## 队列抽象数据类型及Python实现
### 什么是队列Queue
**队列是一种有次序的数据集合，其特征是**
- 新数据项的添加总发生在一端（通常称为“尾rear”端）
- 而现存数据项的移除总发生在另一端（通常称为“首front”端）

**当数据项加入队列，首先出现在队尾，随着队首数据项的移除，它逐渐接近队首**  
**新加入的数据项必须在数据集末尾等待，而等待时间最长的数据项则是队首**

这种次序安排的原则称为（FIFO:First-in first-out）先进先出，或“先到先服务first-come first-served”

队列的例子包括排队

**队列仅有一个入口和一个出口**  
不允许数据项直接插入队中，也不允许从中间移除数据项
### 计算机科学中队列的例子
#### 打印队列
一台打印机面向多个用户/程序提供服务

打印速度比打印请求提交的速度要慢得多

有任务正在打印时，后来的打印请求就要排成队列，以FIFO的形式等待被处理
#### 进程调度
操作系统核心采用多个队列来对系统中同时运行的进程进行调度

进程数远多于CPU核心数

有些进程还要等待不同类型I/O事件

调度原则综合了“先到先服务”及“资源充分利用”两个出发点
#### 键盘缓冲
键盘敲击并不马上显示在屏幕上

需要有个队列性质的缓冲区，将尚未显示的敲击字符暂存其中

队列的先进先出性质则保证了字符的输入和显示次序一致性
### 抽象数据类型Queue
**抽象数据类型Queue是一个有次序的数据集合**  
数据项仅添加到“尾rear”端，而且仅从“首front”端移除  
Queue具有FIFO的操作次序

**抽象数据类型Queue定义为如下操作**
- `Queue()`：创建一个空队列对象，返回值为Queue对象
- `enqueue(item)`：将数据项item添加到队尾，无返回值
- `dequeue()`：从队首移除数据项，返回值为队首数据项，队列被修改
- `isEmpty()`：测试是否空队列，返回值为布尔值
- `size()`：返回队列中数据项的个数
#### 操作样例
Queue Operation|Queue Contents|Return Value
---|---|---
q = Queue()|[]|Queue object
q.isEmpty()|[]|True
q.enqueue(4)|[4]|
q.enqueue('dog')|['dog', 4]|
q.enqueue(True)|[True, 'dog', 4]|
q.size()|[True, 'dog', 4]|3
q.isEmpty()|[True, 'dog', 4]|False
q.enqueue(8.4)|[8.4, True, 'dog', 4]|
q.dequeue()|[8.4, True, 'dog']|4
q.dequeue()|[8.4, True]|'dog'
q.size()|[8.4, True]|2

### 用Python实现ADT Queue
**采 用 List 来容纳Queue的数据项**
- 将List首端作为队列尾端
- List的末端作为队列首端
- enqueue()复杂度为O(n)
- dequeue()复杂度为O(1)

**首尾倒过来的实现，复杂度也倒过来**
```Python
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
```
见[Queue.py](./code/队列/Queue.py)
## 队列的应用：热土豆
### 热土豆问题（约瑟夫问题）
“击鼓传花”的土豆版本  
传烫手的热土豆，鼓声停的时候，手里有土豆的小孩就要出列

如果去掉鼓，改为传过固定人数，就成了“现代版”的约瑟夫问题
> 传说犹太人反叛罗马人，落到困境，约瑟夫和39人决定殉难，坐成一圈儿，报数1～7，报到7的人由旁边杀死，结果约瑟夫给自己安排了个位置，最后活了下来……
### 算法
用队列来实现热土豆问题的算法，参加游戏的人名列表，以及传土豆次数num，算法返回最后剩下的人名

模拟程序采用队列来存放所有参加游戏的人名，按照传递土豆方向从队首排到队尾

游戏时，队首始终是持有土豆的人  
模拟游戏开始，只需要将队首的人出队，随即再到队尾入队，算是土豆的一次传递  
传递了num次后，将队首的人移除，不再入队  

如此反复，直到队列中剩余1人
### 具体程序
```Python
from Queue import Queue
def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()
print(hotPotato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'],7)) # Susan
```
## 队列的应用：打印任务
多人共享一台打印机，采取“先到先服务”的队列策略来执行打印任务  
在这种设定下，首要的问题就是
- 这种打印作业系统的容量有多大？
- 在能够接受的等待时间内，系统能容纳多少用户以多高频率提交多少打印任务？

**一个具体的实例配置如下：**  
一个实验室，在任意的一个小时内，大约有10名学生在场，这一小时中，每人会发起2次左右的打印，每次120页

**打印机的性能是：**
- 以草稿模式打印的话，每分钟10页
- 以正常模式打印的话，打印质量好，但速度下降为每分钟5页

**问题是：怎么设定打印机的模式，让大家都不会等太久的前提下尽量提高打印质量？**

这是一个典型的决策支持问题，但无法通过规则直接计算

我们要用一段程序来模拟这种打印任务场景，然后对程序运行结果进行分析，以支持对打印机模式设定的决策
### 问题建模
**对象：打印任务、打印队列、打印机**
- 打印任务的属性：提交时间、打印页数
- 打印队列的属性：具有FIFO性质的打印任务队列
- 打印机的属性：打印速度、是否忙

**过程：生成和提交打印任务**
- 确定生成概率：实例为每小时会有10个学生提交的20个作业，这样，概率是每180秒会有1个作业生成并提交，概率为每秒1/180
- 确定打印页数：实例是1~20页，那么就是1~20页之间概率相同

**过程：实施打印**
- 当前的打印作业：正在打印的作业
- 打印结束倒计时：新作业开始打印时开始倒计时，回0表示打印完毕，可以处理下一个作业

**模拟时间：**
- 统一的时间框架：以最小单位（秒）均匀流逝的时间，设定结束时间
- 同步所有过程：在一个时间单位里，对生成打印任务和实施打印两个过程各处理一次
### 模拟流程
**创建打印队列对象**

**时间按照秒的单位流逝**  
按照概率生成打印作业，加入打印队列
- 如果打印机空闲，且队列不空，则取出队首作业打印，记录此作业等待时间
- 如果打印机忙，则按照打印速度进行1秒打印
- 如果当前作业打印完成，则打印机进入空闲

**时间用尽，开始统计平均等待时间**

**作业的等待时间**  
- 生成作业时，记录生成的时间戳
- 开始打印时，当前时间减去生成时间即可

**作业的打印时间**  
生成作业时，记录作业的页数开始打印时，页数除以打印速度即可
### 具体程序
见[打印任务.py](./code/队列/打印任务.py)
## 双端队列抽象数据类型及Python实现
### 什么是双端队列Deque
**双端队列Deque是一种有次序的数据集**，跟队列相似，其两端可以称作“首”“尾”端，但deque中数据项既可以从队首加入，也可以从队尾加入；数据项也可以从两端移除    
某种意义上说，双端队列集成了栈和队列的能力

**但双端队列并不具有内在的LIFO或者FIFO特性**  
如果用双端队列来模拟栈或队列，需要由使用者自行维护操作的一致性

### 抽象数据类型Deque
**抽象数据类型“双端队列”定义为如下的操作**
- `Deque()`：创建一个空双端队列
- `addFront(item)`：将item加入队首
- `addRear(item)`：将item加入队尾
- `removeFront()`：从队首移除数据项，返回值为移除的数据项
- `removeRear()`：从队尾移除数据项，返回值为移除的数据项
- `isEmpty()`：返回deque是否为空
- `size()`：返回deque中有包含数据项的个数
### 操作样例
Deque Operation|Deque Contents|Return Value
---|---|---
d = Deque()|[]|Deque object
d.isEmpty()|[]|True
d.addRear(4)|[4]|
d.addRear('dog')|['dog', 4]|
d.addFront('cat')|['dog', 4, 'cat']|
d.addFront(True)|['dog', 4, 'cat', True]|
d.size()|['dog', 4, 'cat', True]|4
d.isEmpty()|['dog', 4, 'cat', True]|False
d.addRear(8.4)|[8.4, 'dog', 4, 'cat', True]|
d.removeRear()|['dog', 4, 'cat', True]|8.4
d.removeFront()|['dog', 4, 'cat']|True
### Python实现ADT Deque
**采用List实现**
- List下标0作为deque的尾端
- List下标-1作为deque的首端

**操作复杂度**
- addFront/removeFront O(1)
- addRear/removeRear O(n)
```Python
class Deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0, item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
```
### “回文词”判定
**“回文词”指正读和反读都一样的词**  
如radar、madam、toot  
中文“上海自来水来自海上”“山东落花生花落东山”

**用双端队列很容易解决“回文词”问题**  
- 先将需要判定的词从队尾加入deque
- 再从两端同时移除字符判定是否相同，直到deque中剩下0个或1个字符
```Python
from Deque import Deque
def palchecker(aString):
    chardeque = Deque()
    for ch in aString:
        chardeque.addRear(ch)
    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual
```
见[“回文词”判定.py](./code/双端队列/“回文词”判定.py)
## 无序表抽象数据类型及Python实现
### 什么是列表List
**列表List是一种简单强大的数据集结构，提供了丰富的操作接口**  
> 但并不是所有的编程语言都提供了List数据类型，有时候需要程序员自己实现

**一种数据项按照相对位置存放的数据集**  
特别的，被称为“无序表unordered list”，其中数据项只按照存放位置来索引，如第1个、第2个……、最后一个等
>为了简单起见，假设表中不存在重复数据项

如一个考试分数的集合“54, 26, 93, 17,77和31”  
如果用无序表来表示，就是[54, 26, 93,17, 77, 31]
### 抽象数据类型无序表UnorderedList
**抽象数据类型“无序表”定义为如下的操作**
- `UnorderedList()`：创建一个空无序表
- `add(item)`：添加一个数据项到列表中，假设item原先不存在于列表中
- `remove(item)`：从列表中移除item，列表被修改，item原先应存在于表中
- `search(item)`：在列表中查找item，返回布尔类型值
- `isEmpty()`：返回列表是否为空
- `size()`：返回列表包含了多少数据项
- `append(item)`：添加一个数据项到表末尾，假设item原先不存在于列表中
- `index(item)`：返回数据项在表中的位置
- `insert(pos, item)`：将数据项插入到位置pos，假设item原先不存在与列表中，同时原列表具有足够多个数据项，能让item占据位置pos
- `pop()`：从列表末尾移除数据项，假设原列表至少有1个数据项
- `pop(pos)`：移除位置为pos的数据项，假设原列表存在位置pos
### 采用链表实现无序表
**为了实现无序表数据结构，可以采用链接表的方案**

**虽然列表数据结构要求保持数据项的前后相对位置，但这种前后位置的保持，并不要求数据项依次存放在连续的存储空间**

**如下图，数据项存放位置并没有规则，但如果在数据项之间建立链接指向，就可以保持其前后相对位置**

![](./images/采用链表实现无序表.png)

第一个和最后一个数据项需要显式标记出来，一个是队首，一个是队尾，后面再无数据了
### 链表实现：节点Node
**链表实现的最基本元素是节点Node**  
每个节点至少要包含2个信息：数据项本身，以及指向下一个节点的引用信息
> 注意next为None的意义是没有下一个节点了，这个很重要

#### 具体程序
```Python
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self, newdata):
        self.data = newdata
    def setNext(self, newnext):
        self.next = newnext
```
### 链表实现：无序表UnorderedList
**可以采用链接节点的方式构建数据集来实现无序表**

**链表的第一个和最后一个节点最重要**  
如果想访问到链表中的所有节点，就必须从第一个节点开始沿着链接遍历下去  

**所以无序表必须要有对第一个节点的引用信息**  
设立一个属性head，保存对第一个节点的引用空表的head为None
```Python
class UnorderedList:
    def __init__(self):
        self.head = None
```
随着数据项的加入，无序表的head始终指向链条中的第一个节点
> 注意：无序表mylist对象本身并不包含数据项（数据项在节点中）

其中包含的head只是对首个节点Node的引用  
判断空表的isEmpty()很容易实现  
## 无序表的链表实现
### add
**接下来，考虑如何实现向无序表中添加数据项，实现add方法**  
由于无序表并没有限定数据项之间的顺序，新数据项可以加入到原表的任何位置  
按照实现的性能考虑，应添加到最容易加入的位置上 

**由链表结构我们知道，要访问到整条链上的所有数据项，都必须从表头head开始沿着next链接逐个向后查找**  
**所以添加新数据项最快捷的位置是表头，整个链表的首位置**
```Python
def add(self, item):
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp
```
### size
**size：从链条头head开始遍历到表尾同时用变量累加经过的节点个数**
```Python
def size(self):
    current = self.head
    count = 0
    while current != None:
        count += 1
        current = current.getNext()
    return count
```
### search
**从链表头head开始遍历到表尾，同时判断当前节点的数据项是否目标**
```Python
def search(self, item):
    current = self.head
    found = False
    while current != None and not found:
        if current.getData() == item:
            found = True
        else:
            current = current.getNext()
    return found
```
### remove(item)
**首先要找到item，这个过程跟search一样，但在删除节点时，需要特别的技巧**  
current指向的是当前匹配数据项的节点，而删除需要把前一个节点的next指向current的下一个节点，所以我们在search current的同时，还要维护前一个(previous)节点的引用

找到item之后，current指向item节点，previous指向前一个节点，开始执行删除，需要区分两种情况：
- current是首个节点
- 或者是位于链条中间的节点
```Python
def remove(self, item):
    current = self.head
    previous = None
    found = False
    while not found:
        if current.getData() == item:
            found = True
        else:
            previous = current
            current = current.getNext()
    if previous == None:
        self.head = current.getNext()
    else:
        previous.setNext(current.getNext()) 
```
### 具体程序
见[UnorderedList.py](./code/无序表/UnorderedList.py)
## 有序表抽象数据类型及Python实现
### 什么是有序表OrderedList
**有序表是一种数据项依照其某可比性质（如整数大小、字母表先后）来决定在列表中的位置**  
越“小”的数据项越靠近列表的头，越靠“前”
### 抽象数据类型：有序表OrderedList
**抽象数据类型“有序表”定义为如下的操作**
- `OrderedList()`：创建一个空的有序表
- `add(item)`：在表中添加一个数据项，并保持整体顺序，此项原不存在
- `remove(item)`：从有序表中移除一个数据项，此项应存在，有序表被修改
- `search(item)`：在有序表中查找数据项，返回是否存在
- `isEmpty()`：是否空表
- `size()`：返回表中数据项的个数
- `index(item)`：返回数据项在表中的位置，此项应存在
- `pop()`：移除并返回有序表中最后一项，表中应至少存在一项
- `pop(pos)`：移除并返回有序表中指定位置的数据项，此位置应存在
### 有序表OrderedList实现
**在实现有序表的时候，需要记住的是，数据项的相对位置，取决于它们之间的“大小”比较**  
由于Python的扩展性，下面对数据项的讨论并不仅适用于整数，可适用于所有定义了__gt__方法（即'>'操作符）的数据类型

- 同样采用链表方法实现
- Node定义相同
- OrderedList也设置一个head来保存链表表头的引用
```Python
class OrderedList:
    def __init__(self):
        self.head = None
```
对于isEmpty/size/remove这些方法，与节点的次序无关 ， 所以其实现跟UnorderedList是一样的  
search/add方法则需要有修改
#### search(item)
**在*无序表*的search中，如果需要查找的数据项不存在，则会搜遍整个链表，直到表尾**  

**对于*有序表*来说，可以利用链表节点有序排列的特性，来为search节省不存在数据项的查找时间**  
一旦当前节点的数据项大于所要查找的数据项，则说明链表后面已经不可能再有要查找的数据项，可以直接返回False
```Python
def search(self, item):
    current = self.head
    found = False
    stop = False
    while current != None and not found and not stop:
        if current.getData() == item:
            found = True
        else:
            if current.getData() > item:
                stop = True
            else:
                current = current.getNext()
    return found
```
#### add(item)
**相比无序表，改变最大的方法是add，因为add方法必须保证加入的数据项添加在合适的位置，以维护整个链表的有序性**

由于涉及到的插入位置是当前节点之前，而链表无法得到“前驱”节点的引用  
所以要跟remove方法类似，引入一个previous的引用，跟随当前节点current
```Python
def add(self, item):
    current = self.head
    previous = None
    stop = False
    while current != None and not stop:
        if current.getData() > item:
            stop = True
        else:
            previous = current
            current = current.getNext()
    temp = Node(item)
    if previous == None:
        temp.setNext(self.head)
        self.head = temp
    else:
        temp.setNext(current)
        previous.setNext(temp)
```
### 链表实现的算法分析
**对于链表复杂度的分析，主要是看相应的方法是否涉及到链表的遍历**  
对于一个包含节点数为n的链表  
- isEmpty是O(1)，因为仅需要检查head是否为None
- size是O(n)，因为除了遍历到表尾，没有其它办法得知节点的数量
- search/remove以及有序表的add方法，则是O(n)，因为涉及到链表的遍历，按照概率其平均操作的次数是n/2
- 无序表的add方法是O(1)，因为仅需要插入到表头

链表实现的List，跟Python内置的列表数据类型，在有些相同方法的实现上的时间复杂度不同  
主要是因为Python内置的列表数据类型是基于*顺序存储*来实现的，并进行了优化
# 递归动规
## 什么是递归
### 什么是递归Recursion
**递归是一种解决问题的方法，其精髓在于**  
将问题分解为规模更小的相同问题，持续分解，直到问题规模小到可以用非常简单直接的方式来解决  
递归的问题分解方式非常独特，其算法方面的明显特征就是：*在算法流程中调用自身*
### 初识递归：数列求和
**求和实际上最终是由一次次的加法实现的，而加法恰有2个操作数，这个是确定的**

看看怎么想办法，将问题规模较大的列表求和，分解为规模较小而且固定的2个数求和（加法）

**换个方式来表达数列求和：全括号表达式(1+(3+(5+(7+9))))**  
上面这个式子，最内层的括号(7+9)，这是无需循环即可计算的，实际上整个求和的过程是这样：  
$total = (1 + (3 + (5 + (7 + 9))))$  
$total = (1 + (3 + (5 + 16)))$  
$total = (1 + (3 + 21))$  
$total = (1 + 24)$  
$total = 25$

**观察上述过程中所包含的重复模式，可以把求和问题归纳成这样：**  
数列的和=“首个数”+“余下数列”的和
#### 具体程序
```Python
def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])
```
**上面程序的要点：**
1. 问题分解为更小规模的相同问题，并表现为“调用自身”
2. 对“最小规模”问题的解决：简单直接
### 递归“三定律”
1. 递归算法必须有一个基本结束条件（最小规模问题的直接解决）
2. 递归算法必须能改变状态向基本结束条件演进（减小问题规模）
3. 递归算法必须调用自身（解决减小了规模的相同问题）

数列求和问题首先具备了基本结束条件：  
**当列表长度为1的时候，直接输出所包含的唯一数**

数列求和处理的数据对象是一个列表，而基本结束条件是长度为1的列表，那递归算法就要改变列表并向长度为1的状态演进
## 递归的应用：任意进制转换
**用最熟悉的十进制分析下这个问题**

十进制有十个不同符号：convString = "0123456789"  
比十小的整数，转换成十进制，直接查表就可以了：convString[n]  
想办法把比十大的整数，拆成一系列比十小的整数，逐个查表  
比如七百六十九，拆成七、六、九，查表得到769就可以了

**所以，在递归三定律里，我们找到了“基本结束条件”，就是小于十的整数**  
拆解整数的过程就是向“基本结束条件”演进的过程

**我们用整数除，和求余数两个计算来将整数一步步拆开**  
除以“进制基base”（// base）  
对“进制基”求余数（% base）  

**问题就分解为：**
- 余数总小于“进制基base”，是“基本结束条件”，可直接进行查表转换
- 整数商成为“更小规模”问题，通过递归调用自身解决
### 具体代码
```Python
def toStr(n, base):
    convertString = '0123456789ABCDEF'
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base,base) + convertString[n%base]
```
见[任意进制转换.py](./code/递归/任意进制转换.py)
## 递归调用的实现
**当一个函数被调用的时候，系统会把调用时的现场数据压入到系统调用栈**  
每次调用，压入栈的现场数据称为栈帧  
当函数返回时，要从调用栈的栈顶取得返回地址，恢复现场，弹出栈帧，按地址返回
### Python中的递归深度限制
在调试递归算法程序的时候经常会碰到这样的错误：RecursionError
> 递归的层数太多，系统调用栈容量有限

这时候要检查程序中是否忘记设置基本结束条件，导致无限递归，或者向基本结束条件演进太慢，导致递归层数太多，调用栈溢出

在Python内置的sys模块可以获取和调整最大递归深度

<img src="./images/Python中的递归深度限制.png" style="max-width: 50%; height: auto;" alt="Python中的递归深度限制">

## 递归可视化：分形树
