
# 目录
## [1)match...case](#match-case)
## [2)next()](#next)
## [3)@property](#property)
## [4)enumerate()](#enumerate)
## [5)sort()和sorted()](#sort-sorted)

# 1)match...case<a id="match-case"></a>
`match...case` 是 Python 3.10 引入的一个非常强大的新特性，官方称之为**结构化模式匹配（Structural Pattern Matching）**。

虽然它在表面上看起来很像 C、Java 或 JavaScript 中的 `switch-case` 语句，但它的功能要强大得多，更接近于 Rust 或 Haskell 中的模式匹配。它不仅能进行简单的值匹配，还能对复杂的数据结构（如列表、字典、类实例）进行解构，并提取其中的数据。

## 1. 基础语法结构
基本结构非常直观，`match` 后面跟上要匹配的对象，然后依次尝试 `case` 分支。只有第一个匹配成功的模式会被执行，如果都不匹配，则执行 `case _:`（通配符，类似其他语言的 `default`）。

```
match 被匹配对象:
    case 模式1:
        执行代码块1
    case 模式2:
        执行代码块2
    case _:
        默认执行代码块
```

## 2. 核心应用场景与示例

### 场景一：替代冗长的 if-elif 链（字面值与多值匹配）
处理 HTTP 状态码或枚举类型时，代码会变得非常简洁。同时支持使用 `|` 进行多条件匹配。

```python
def handle_status(status_code):
    match status_code:
        case 200:
            return "OK"
        case 401 | 403:  # 匹配多个值
            return "Not allowed"
        case 404:
            return "Not found"
        case _:          # 兜底默认处理
            return "Unknown status"
```

### 场景二：序列（列表/元组）解构与变量捕获
这是 `match` 最强大的功能之一。它可以直接从列表或元组中提取特定位置的数据，并赋值给变量。

```python
point = (1, 2)
match point:
    case (0, 0):
        print("原点")
    case (0, y):         # 捕获 y 的值
        print(f"在Y轴上，Y坐标为 {y}")
    case (x, 0):         # 捕获 x 的值
        print(f"在X轴上，X坐标为 {x}")
    case (x, y):         # 同时捕获 x 和 y
        print(f"坐标为 ({x}, {y})")
```

对于列表，还支持使用 `*` 捕获剩余元素：
```python
match [1, 2, 3, 4]:
    case [1, *rest]:     # rest 将捕获 [2, 3, 4]
        print(f"剩余元素: {rest}")
```

### 场景三：字典匹配
可以精确匹配字典中的某些键，并提取对应的值。

```python
user = {"name": "Alice", "age": 25}
match user:
    case {"name": name, "age": age}:
        print(f"姓名: {name}, 年龄: {age}")
    case {"name": name}:
        print(f"只有姓名: {name}")
```

### 场景四：类实例匹配
可以直接匹配自定义类的对象，并提取其属性。

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
match person:
    case Person(name="Alice", age=25):
        print("匹配到 Alice，25 岁")
    case Person(name=name, age=age):
        print(f"匹配到 {name}, {age} 岁")
```

## 3. 高级技巧：守卫语句（Guard）
你可以在 `case` 后面加上 `if` 条件（称为守卫），只有当模式匹配成功 **且** `if` 条件为真时，才会执行该分支。

```python
match point:
    case (x, y) if x > 0 and y > 0:
        print("在第一象限")
    case (x, y):
        print("不在第一象限")
```

##  注意事项
1. **版本要求**：必须使用 Python 3.10 或更高版本。
2. **软关键字**：`match` 和 `case` 是“软关键字”，这意味着如果你把变量命名为 `match` 或 `case`，在旧代码中依然可以正常运行，只有在特定语法上下文中它们才会被识别为关键字。
3. **执行逻辑**：匹配是**自上而下**进行的，一旦匹配成功就会跳出，不会像某些语言的 `switch` 那样发生“穿透（fall-through）”。

## match-case 速查表

| 功能分类             | 语法示例                           | 说明与注意事项                                   |
|:-----------------|:-------------------------------|:------------------------------------------|
| **精确值匹配**        | `case 404:`                    | 匹配具体的数字、字符串等字面值。                          |
| **多值匹配 (OR)**    | `case "yes" \| "y":`           | 使用竖线 `                                    |` 连接多个值，满足其一即匹配。 |
| **变量绑定**         | `case x:`                      | 匹配任何值，并将其赋值给变量 `x`。（️注意：会覆盖同名外部变量）        |
| **通配符 (默认)**     | `case _:`                      | 匹配所有未命中情况，类似 `default`。（️必须放在所有 case 的最后） |
| **序列解构**         | `case [first, *rest]:`         | 匹配列表或元组，提取首元素，`*rest` 捕获剩余所有元素。           |
| **字典匹配**         | `case {"name": name, **rest}:` | 匹配包含指定键的字典，提取值，`**rest` 捕获剩余的键值对。         |
| **类实例匹配**        | `case Point(x=0, y=0):`        | 匹配类的实例，并提取其属性值。支持位置参数和关键字参数。              |
| **守卫条件 (Guard)** | `case (x, y) if x > 0:`        | 在模式匹配成功后，追加 `if` 条件判断。条件为假则尝试下一个 case。    |
| **类型匹配**         | `case str() as username:`      | 匹配特定数据类型，并使用 `as` 将匹配到的值绑定给变量。            |
| **嵌套匹配**         | `case {"data": [p1, *_]}:`     | 支持列表、字典、类的任意深度嵌套解构。                       |
| **常量匹配**         | `case HttpStatus.OK:`          | 匹配模块级或类级别的常量。（️注意：直接写变量名会被视为变量绑定）         |

##  核心避坑指南
1. **顺序敏感**：匹配是**自上而下**进行的，一旦匹配成功就会跳出，不会发生“穿透（fall-through）”。
2. **变量陷阱**：在 `case` 中直接写一个变量名（如 `case x:`），Python 会认为你在声明一个新变量并捕获当前值，而不是去匹配外部已有的变量 `x`。如果要匹配外部变量，应使用点号表示法（如 `case Colors.RED:`）或守卫条件。
3. **不支持的结构**：`match` 只能用于可解构的结构体（列表、元组、字典、类），**不支持**集合（set）和生成器（generator），因为它们是无序或一次性的。
Python 的 `match case` 是在 **Python 3.10**（PEP 634）中引入的结构化模式匹配（Structural Pattern Matching）。**千万别把它只当成其他语言中的 `switch` 语句**，它的核心能力是**解构数据**（拆包），而不仅仅是匹配值。

## 什么时候用？什么时候不用？
| 适用场景                | 不适用场景                                 |
|:--------------------|:--------------------------------------|
| 解析复杂的 JSON/XML 树形结构 | 单纯的 `if a == 1 or a == 2`（用 `if` 更简单） |
| 命令模式（CMD 解析、事件分发）   | 需要调用函数计算复杂布尔逻辑（用 `if-elif`）           |
| 处理 AST（抽象语法树）       | 涉及大量非数据类对象的业务逻辑                       |
| 解包嵌套的元组/列表          | 性能极度敏感的底层循环（`match` 略有开销）             |

## match-case与if-else的性能比较

### 简单值匹配：`if` 略快一点

对于匹配单个数值或字符串这种简单场景，`if-elif` 通常会**稍快一些**（大约快 **10%**）。

这是因为 CPython 解释器对 `match-case` 的实现，在处理这种简单情况时，会多执行一两条字节码指令（如 `DUP_TOP` 和 `POP_TOP`）。虽然这个开销极小，但在纯粹的数值比较中，`if` 确实更直接。

### 结构化模式匹配：`match` 的优势区

`match-case` 的真正威力在于**结构化模式匹配**，这也是它性能优势的体现之处。在处理复杂数据结构时，`match-case` 可以将多个操作合并为一步完成。

*   **序列解构**：一次性完成类型检查、长度验证和元素提取，避免了多次手动调用 `isinstance()`、`len()` 和索引取值。
*   **字典匹配**：一次性完成键值提取和类型转换，避免了多次 `.get()` 调用。

当分支数较多（例如 **≥ 5**）且结构固定时，这种“一站式”操作能让 `match-case` 比等效的 `if-elif` 链快 **10% 到 15%**。

### 让 `match` 变慢的写法

*   **滥用守卫（Guard）**：守卫中的表达式在每次匹配失败后都可能重新执行，如果包含耗时操作，会拖慢速度。
*   **匹配大量非字符串数据**：例如用 `case str():`，其开销可能比 `type(value) is str` 慢 **2.3 倍**。
*   **复杂 OR 模式**：`case 1 | 2 | 3 | 4 | 5:` 可能退化为线性比对，不如 `if value in {1, 2, 3, 4, 5}:` 高效。
*   **高频调用**：在紧密循环中频繁调用包含复杂 `match` 的函数，其固定的解析开销可能成为瓶颈。

# 2)next()<a id="next"></a>
`next()` 是 Python 的一个内置函数，用于**从迭代器（Iterator）中逐个取出下一个元素**。它是 Python 实现“惰性求值”和流式处理数据的核心工具。

## 1. 基本语法
```python
next(iterator[, default])
```
- **iterator**：必须是一个迭代器对象（实现了 `__next__()` 方法）。
- **default**（可选）：如果迭代器已经耗尽（没有更多元素），返回该默认值，而不是抛出异常。

---

## 2. 核心用法：配合 `iter()`

`next()` 只能作用于**迭代器**，不能直接作用于列表、元组等**可迭代对象**（Iterable）。需要用 `iter()` 先将其转换为迭代器。

```python
nums = [1, 2, 3]
it = iter(nums)  # 将列表转为迭代器

print(next(it))  # 输出: 1
print(next(it))  # 输出: 2
print(next(it))  # 输出: 3
```

---

## 3. 处理耗尽（StopIteration）

当迭代器没有元素时，`next()` 默认会抛出 `StopIteration` 异常。

```python
it = iter([1])
print(next(it))  # 输出: 1
# print(next(it))  # 抛出 StopIteration
```

**推荐做法**：使用 `default` 参数来优雅地终止，避免异常处理。

```python
it = iter([1])
print(next(it, None))  # 输出: 1
print(next(it, None))  # 输出: None（不再抛异常）
print(next(it, "结束")) # 输出: "结束"
```

---

## 4. 与生成器（Generator）结合

生成器是 Python 中最常见的迭代器，`next()` 用于驱动生成器函数的执行，直到遇到 `yield`。

```python
def count_down(n):
    while n > 0:
        yield n
        n -= 1

gen = count_down(3)
print(next(gen))  # 输出: 3
print(next(gen))  # 输出: 2
print(next(gen))  # 输出: 1
```

---

## 5. 进阶：文件逐行读取（流式处理）

`next()` 常用于读取超大文件，避免一次性加载到内存。

```python
with open('large_file.txt', 'r') as f:
    first_line = next(f)       # 读取第一行
    second_line = next(f, None) # 读取第二行，若不存在则返回 None
    # 配合循环可高效遍历
```

---

## 6. 底层原理：`__next__()` 协议

当你调用 `next(it)` 时，Python 实际上是在调用 `it.__next__()` 方法。手动调用效果相同：

```python
it = iter([10, 20])
print(it.__next__())  # 输出: 10
```

---

## 7. 高级用法：哨兵值模式

```python
# 读取直到遇到空字符串
def read_until_empty():
    while True:
        data = yield
        if not data:
            return

gen = read_until_empty()
next(gen)  # 预激生成器
gen.send('hello')
gen.send('')   # 触发返回
```

虽然这里用了 `send()`，但 `next(gen)` 用于启动生成器，这是一个常见的“协程”初始化模式。

---

## 8. 重要注意事项（踩坑点）

- **一次性消费**：迭代器是有状态的，取出的元素不会保留，无法“回退”重新读取。
- **不可逆**：一旦耗尽，再次调用（且无默认值）必定抛出 `StopIteration`，想要重新遍历只能重新创建迭代器。
- **与 `for` 循环的区别**：`for item in iterator` 底层自动捕获了 `StopIteration` 并退出循环；而 `next()` 让你拥有更精细的控制权（比如手动处理特定条件）。

---

## 9. 实际应用场景

- **手动控制循环**：在 `while` 中按需取数。
- **数据流管道**：配合生成器，实现类似 Unix 管道的链式数据处理。
- **训练模型/批量加载**：从数据加载器中逐个获取 Batch，直到耗尽。

```python
# 配合 while 循环的典型模式
it = iter(range(5))
while True:
    try:
        value = next(it)
        # 处理 value
    except StopIteration:
        break
# 或者更简洁地使用默认值：
while (value := next(it, None)) is not None:
    # 处理 value（注意：如果元素本身可能为 None，则此写法不适用）
```

# 3)@property<a id="property"></a>
在 Python 中，`@property` 是一个内置装饰器，它的核心作用就是**将方法（函数）伪装成属性（变量）来调用**。

简单来说，它让你可以像写 `obj.attribute` 这样去访问数据，但实际上背后执行的是 `obj.method()` 这个函数。

## 1. 为什么要用它？（解决什么问题）
假设你有一个 `Student` 类，直接暴露年龄属性：

```python
class Student:
    def __init__(self, age):
        self.age = age  # 直接暴露属性
```
如果哪天需求变了，年龄不能为负数，你必须修改代码。如果直接改 `self.age`，所有外部调用 `s.age = -5` 的代码都会崩溃。`@property` 解决了这个困境：**你可以先以简单属性方式写代码，后续需要增加逻辑时，无缝切换成方法，而不改变外部调用方式**（这就是“统一访问原则”）。

## 2. 三大核心用法（Getter, Setter, Deleter）

### ① 只读属性（Getter）
只需加 `@property`，方法名就是属性名，**无需括号**调用。
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius  # 约定：下划线表示“受保护”，不要直接改

    @property
    def area(self):
        # 计算属性：每次访问实时计算，无需存储
        return 3.14 * self._radius ** 2

c = Circle(5)
print(c.area)  # 输出 78.5，注意没有括号！
# c.area = 100  # 这会报错，因为没定义 setter，它是只读的
```

### ② 可读写属性（Setter）
如果想让属性可以被赋值，且赋值时做校验，就用 `@属性名.setter`。
```python
class Student:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("年龄不能为负数！")
        if value > 150:
            raise ValueError("年龄过大！")
        self._age = value

s = Student(18)
print(s.age)  # 18
s.age = 20    # 调用 setter，合法
# s.age = -5  # 报错：ValueError
```

### ③ 删除属性（Deleter）
配合 `del` 关键字使用，通常用于清理缓存或释放资源。
```python
class Data:
    def __init__(self):
        self._cache = "重要数据"

    @property
    def cache(self):
        return self._cache

    @cache.deleter
    def cache(self):
        print("正在清理缓存...")
        del self._cache

d = Data()
del d.cache  # 输出：正在清理缓存...
```

## 3. 什么时候该用？（最佳实践）
- **数据校验**：赋值时检查类型、范围（如上面的年龄）。
- **计算属性**：面积、全名（`first_name + last_name`）、价格含税等，无需额外存储。
- **惰性加载（Lazy Loading）**：第一次访问时计算，后续直接返回缓存结果，提升性能。

```python
class HeavyData:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        if self._value is None:
            print("正在从数据库/网络加载巨大数据...（仅此一次）")
            self._value = 42  # 模拟耗时操作
        return self._value
```

## 4. 新手最容易踩的坑（警告⚠️）
**千万不要在 `@property` 内部操作同名的属性名，否则会无限递归，导致程序卡死（RecursionError）！**

```python
# ❌ 错误写法（无限递归）
class Bad:
    def __init__(self, x):
        self.x = x  # 注意：这里调用了下面的 setter，而不是直接赋值！

    @property
    def x(self):
        return self.x  # 这里又在调用 getter 自己，死循环！

    @x.setter
    def x(self, value):
        self.x = value  # 这里又在调用 setter 自己，死循环！
```
**✅ 正确写法**：在 `__init__` 和 setter 中，必须操作**带下划线的私有变量** `self._x`，而非 `self.x`。

```python
class Good:
    def __init__(self, x):
        self._x = x  # 直接操作私有变量，绕过 setter

    @property
    def x(self):
        return self._x  # 返回私有变量

    @x.setter
    def x(self, value):
        self._x = value  # 修改私有变量
```

## 5. 底层原理（一句话概括）
`@property` 是 Python 内置 `property()` 函数的语法糖。它的底层基于**描述符协议**，将 `fget`（getter）、`fset`（setter）、`fdel`（deleter）这三个方法绑定到了同一个属性名上。

---

**总结一句口诀**：`@property` 上马甲，方法调用变属性；赋值校验靠 setter，只读计算全靠它；内部记得加下划线，防止递归坑自己。

# 4)enumerate()<a id="enumerate"></a>
`enumerate()` 是 Python 的一个内置函数，堪称“循环计数器神器”。它的核心作用是**在遍历可迭代对象（如列表、元组、字符串）时，同时获取元素的索引和值**，让你彻底告别丑陋的 `range(len())` 写法。

### 1. 基本语法
```python
enumerate(iterable, start=0)
```
- **iterable**：任何可迭代对象（列表、元组、字符串、字典等）。
- **start**：索引起始值，默认为 `0`，你可以改为 `1` 让人性化计数。

### 2. 返回值（重要）
`enumerate()` 返回的是一个**惰性迭代器**（`enumerate` 对象），而不是列表。这意味着它不会一次性生成所有数据，而是边循环边产生，非常节省内存。

```python
print(enumerate(['a', 'b'])) 
# <enumerate object at 0x...> （不是列表！）
```

---

### 3. 基础用法（对比传统写法）

**❌ 不推荐的写法（C语言风格）**
```python
fruits = ['apple', 'banana', 'orange']
for i in range(len(fruits)):
    print(i, fruits[i])
```

**✅ Pythonic 推荐写法**
```python
fruits = ['apple', 'banana', 'orange']
for index, value in enumerate(fruits):
    print(index, value)
# 输出：0 apple / 1 banana / 2 orange
```

---

### 4. 进阶常用场景

**场景一：从 1 开始计数（start 参数）**
适合生成序号（Excel行号、排名等）：
```python
for line_num, content in enumerate(lines, start=1):
    print(f"第{line_num}行: {content}")
```

**场景二：直接转换为列表或字典**
```python
# 转为 [(0, 'a'), (1, 'b')]
list_enumerate = list(enumerate(['a', 'b']))

# 转为 {0: 'a', 1: 'b'} (字典推导式)
dict_enumerate = {i: v for i, v in enumerate(['a', 'b'])}
```

**场景三：在列表推导式中使用**
```python
# 将列表中偶数索引的元素变为大写
words = ['hello', 'world', 'python']
result = [v.upper() if i % 2 == 0 else v for i, v in enumerate(words)]
# ['HELLO', 'world', 'PYTHON']
```

---

### 5. 解包技巧（针对嵌套数据）
遍历二维列表时，可以多层解包：
```python
matrix = [['a', 'b'], ['c', 'd']]
for i, (x, y) in enumerate(matrix):  # 注意括号
    print(i, x, y)
# 0 a b
# 1 c d
```

---

### 6. 常见陷阱与注意事项

**⚠️ 陷阱1：修改列表元素时，直接用 value 修改无效**
```python
nums = [1, 2, 3]
for i, v in enumerate(nums):
    v += 10  # 这行没用！v 只是值的拷贝
print(nums) # [1, 2, 3] （原列表没变）

# 必须通过索引修改：
for i, v in enumerate(nums):
    nums[i] = v + 10  # ✅ 有效
```

**⚠️ 陷阱2：遍历时增删元素**
如果边遍历边删除列表元素，索引会错位。建议遍历副本 `for i, v in enumerate(list[:])`。

**⚠️ 陷阱3：enumerate 是迭代器，只能消费一次**
```python
e = enumerate([1, 2])
list(e) # [(0,1), (1,2)]
list(e) # [] （第二次就空了，因为迭代器已耗尽）
```

---

### 7. 性能对比
在底层 C 语言实现中，`enumerate` 比手动维护计数器（`i += 1`）速度更快，代码也更简洁。除非你需要极复杂的索引跳跃，否则优先使用 `enumerate`。

# 5)sort()和sorted()<a id="sort-sorted"></a>
在 Python 中，`sort()` 和 `sorted()` 都是用于排序的内置工具，但它们的**使用场景**和**底层机制**有本质区别。核心差异可以用一句话概括：

- **`list.sort()`** 是**列表自带的方法**，会**原地修改**原列表，返回 `None`。
- **`sorted()`** 是**内置全局函数**，会**创建新列表**返回，不改变原可迭代对象。

下面是详细的对比表格和代码示例：

### 1. 核心区别对比表

| 特性 | `list.sort()` | `sorted()` |
| :--- | :--- | :--- |
| **类型** | 列表（list）的专属方法 | Python 内置函数 |
| **返回值** | `None`（修改原对象） | 返回一个**全新的排序后列表** |
| **适用范围** | **仅限**列表 | **任何**可迭代对象（元组、字典、集合、生成器等） |
| **内存占用** | 较低（原地修改，不复制） | 较高（无论原数据是什么，都会生成一个新列表） |
| **链式调用** | 不可以（因为返回 `None`） | 可以（例如 `sorted(data, key=...)[:5]`） |

---

### 2. 代码直观演示

**场景一：原地修改 vs 返回新列表**
```python
# sort() - 原地修改
nums = [3, 1, 2]
result = nums.sort()
print(nums)    # 输出: [1, 2, 3] （原列表被改变了）
print(result)  # 输出: None

# sorted() - 返回新列表
nums = [3, 1, 2]
new_nums = sorted(nums)
print(nums)     # 输出: [3, 1, 2] （原列表安然无恙）
print(new_nums) # 输出: [1, 2, 3] （全新的列表）
```

**场景二：适用范围（sorted 更强大）**
```python
# 对元组排序 -> sorted 可以，sort 不行（因为元组没有 sort 方法）
tup = (3, 1, 2)
sorted_tup = sorted(tup)
print(sorted_tup)  # 输出: [1, 2, 3] （返回列表）

# 对字典按键排序
d = {'b': 2, 'a': 1}
sorted_keys = sorted(d)
print(sorted_keys) # 输出: ['a', 'b'] （对字典的键排序）
```

---

### 3. 进阶参数（两者通用）

两者都接受 `key` 和 `reverse` 两个关键字参数，用法完全一致：

- **`key`**：指定一个函数，用于从每个元素中提取比较的键值。
- **`reverse`**：布尔值，`True` 表示降序，默认 `False`（升序）。

```python
# 按字符串长度排序
words = ['apple', 'banana', 'pear', 'kiwi']
words.sort(key=len, reverse=True)
print(words) # 输出: ['banana', 'apple', 'pear', 'kiwi'] （按长度降序）

# 使用 sorted 对字典列表按年龄排序
students = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}]
sorted_students = sorted(students, key=lambda x: x['age'])
print(sorted_students) # 输出: [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}]
```

---

### 4. 性能与内存考量（重要）

- **`sort()` 性能略优**：因为它不需要额外复制一份数据，对于超大规模列表（如百万级数据），用 `sort()` 能显著节省内存并提升速度。
- **`sorted()` 更灵活**：如果你需要保留原始数据用于后续计算，或者处理的数据不是列表（比如从文件读取的生成器），必须用 `sorted()`。

---

### 5. 稳定性的重要特性（两者相同）

Python 的排序算法（Timsort）是**稳定排序**。这意味着如果两个元素有相同的 `key` 值，它们在排序后的相对顺序会与排序前保持一致。

```python
# 先按年龄排序，再按名字排序（此时年龄相同的顺序保持原样）
data = [[1, 'A'], [1, 'B'], [2, 'C']]
data.sort(key=lambda x: x[0]) # 只按第一个元素排序
# 输出: [[1, 'A'], [1, 'B'], [2, 'C']] -> 两个 '1' 保持了原来的 A, B 顺序
```

---

### 6. 终极选择建议（什么时候用哪个？）

1. **如果数据是列表，且不需要保留原始数据** → **用 `list.sort()`**。代码更简洁，内存效率更高。
2. **如果需要保留原始数据不变** → **用 `sorted()`**。
3. **如果数据是元组、字典、集合或生成器** → **只能用 `sorted()`**。

> **冷知识补充**：如果你想对字典按值排序，`sorted(d.items(), key=lambda item: item[1])` 是最常见的写法，返回的是排序后的键值对元组列表。
