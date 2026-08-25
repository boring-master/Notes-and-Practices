

使用python基于面向对象的编程思想开发的**简陋**的图书管理系统

## 技术栈

- uv
- ruff

## 项目结构

```
BooksManagementSystem/
├── data/
│   ├── books.json
│   ├── members.json
│   └── admins.json
├── models/
│   ├── book.py
│   ├── member.py
│   └── admin.py
├── services/library.py
├── utils/                      # 工具函数
│   ├── hash_utils.py
│   ├── id_utils.py
│   ├── validation.py
│   └── data_storage.py
├── exceptions.py
├── main.py                     # 程序入口
├── pyproject.toml              # 项目依赖配置
└── uv.lock                     # uv 依赖锁定文件
```

## 类结构

### class Book

- 属性
  - `book_id` (`str`): 编号
  - `title` (`str`): 书名
  - `author` (`str`): 作者
  - `total_num` (`int`): 总数量
  - `__available_num` (`int`): 可用数量
  - `status` (`BookStatus`): 状态
- 方法
  - `borrow_book`: 借阅图书
  - `return_book`: 归还图书
  - `get_available_num`: 获取可用图书数量
  - `member_get_status`: 会员获取图书状态
  - `change_status`: 改变图书状态
  - `change_num`: 改变图书数量
  - `from_dict`: 从字典中创建图书对象
  - `to_dict`: 将图书对象转换为字典

### class Member

- 属性
  - `member_id` (`str`): 编号
  - `account_id` (`str`): 账号
  - `name` (`str`): 姓名
  - `vip_level` (`int`): 等级
  - `__hashed_password` (`str`): 密码哈希值
  - `__borrowed_books` (`list[dict[str,str]]`): 正在借阅的图书
- 方法
  - `borrow_book`: 借阅图书
  - `return_book`: 归还图书
  - `verify_password`: 验证密码
  - `get_borrowed_books`: 获取正在借阅的图书
  - `change_hashed_password`: 修改密码哈希值
  - `get_max_books`: 获取可借阅的最大图书数量
  - `from_dict`: 从字典中创建用户对象
  - `to_dict`: 将用户对象转换为字典

### class Admin

- 属性
  - `admin_id` (`str`): 管理员编号
  - `account_id` (`str`): 账号
  - `name` (`str`): 姓名
  - `__hashed_password` (`str`): 密码哈希值
- 方法
  - `verify_password`: 验证密码
  - `change_hashed_password`: 修改密码哈希值
  - `from_dict`: 从字典创建管理员对象
  - `to_dict`: 将管理员对象转换为字典

### class Library

- 属性
  - `books` (`dict[str, Book]`): 所有图书
  - `members` (`dict[str, Member]`): 所有用户
  - `admins` (`dict[str, Admin]`): 所有管理员
  - `current_user` (`Admin|Member|None`): 当前用户
  - `data_storage` (`DataStorage`): 数据存储
- 方法
  - `load_books_data`: 加载图书数据
  - `load_members_data`: 加载用户数据
  - `load_admins_data`: 加载管理员数据
  - `login`: 登录
  - `_admin_login`: 管理员登录
  - `register`: 注册
  - `borrow_book`: 借阅图书
  - `return_book`: 归还图书
  - `view_borrowed_books`: 查看已借阅图书
  - `view_books`: 查看图书
  - `change_password`: 修改密码
  - `delete_account`: 删除账户
  - `modify_book_info`: 修改图书信息
  - `add_book`: 添加图书
  - `view_members`: 查看用户
  - `modify_member_info`: 修改用户信息

### class DataStorage

- 属性
  - `data_dir` (`Path`): 数据目录
  - `books_file` (`Path`): 图书数据文件
  - `members_file` (`Path`): 用户数据文件
  - `records_file` (`Path`): 记录数据文件
  - `admins_file` (`Path`): 管理员数据文件
- 方法
  - `_read_json`: 读取 JSON 文件
  - `_write_json`: 写入 JSON 文件
  - `load_books`: 加载图书数据
  - `save_books`: 保存图书数据
  - `load_members`: 加载用户数据
  - `save_members`: 保存用户数据
  - `load_admins`: 加载管理员数据
  - `save_admins`: 保存管理员数据

## 数据存储结构

### books.json

```json
[
  {
    "book_id": str,       //编号
    "title": str,         //书名
    "author": str,        //作者
    "total_num": int,     //总数量
    "available_num": int, //可用数量
    "status":str          //图书状态
  }
]
```

### members.json

```json
[
  {
    "member_id": str,       //编号
    "account_id": str,      //账号
    "name": str,            //姓名
    "vip_level": int,       //等级
    "hashed_password": str, //密码哈希值
    "borrowed_books":       //正在借阅的图书
    [     
      {
        "book_id": str,     //编号
        "borrow_date": str  //借阅时间
      }
    ]
  }
]
```

### admins.json

```json
[
  {
    "admin_id": str,        //编号
    "account_id": str,      //账号
    "name": str,            //姓名
    "hashed_password": str  //密码哈希值
  }
]
```

## 初始管理员账号

- 账号:12345678999
- 密码: 123qweASD