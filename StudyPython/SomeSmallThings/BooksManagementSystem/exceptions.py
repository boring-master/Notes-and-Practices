
class LibraryError(Exception):
    def __init__(self, message = "图书管理系统错误"):
        self.message = message
        super().__init__(message)

class BookError(LibraryError):
    pass

class BookNotFoundError(BookError):
    """图书不存在"""
    def __init__(self, book_id = None, title = None, author = None):
        self.book_id = book_id
        self.title = title
        self.author = author
        if self.book_id:
            super().__init__(f"编号为 {book_id} 的图书不存在")
        elif self.title:
            super().__init__(f"书名为 {title} 的图书不存在")
        elif self.author:
            super().__init__(f"作者为 {author} 的图书不存在")
        else:
            super().__init__("图书不存在")

class BookNotAvailableError(BookError):
    """图书已借完"""
    def __init__(self, book_id):
        self.book_id = book_id
        super().__init__(f"编号为 {book_id} 的图书不可借阅")

class BookInfoNotChangeError(BookError):
    """图书信息未改变"""
    def __init__(self, book_id):
        self.book_id = book_id
        super().__init__(f"编号为 {book_id} 的图书的新信息与原来一致")

class BookNumChangeError(BookError):
    """图书数量改变"""
    def __init__(self, book_id, total_num, available_num):
        self.book_id = book_id
        self.total_num = total_num
        self.available_num = available_num
        super().__init__(f"编号为 {book_id} 的图书的新总数不能低于 {total_num-available_num} 本")

class BookInfoEmptyError(BookError):
    """图书信息为空"""
    def __init__(self, book_id = None, title = None, author = None, message = None):
        self.book_id = book_id
        self.title = title
        self.author = author
        missing = [name for name, value in (('编号', book_id), ('书名', title), ('作者', author)) if not value and value is not None]
        self.missing_fields = missing
        super().__init__(message if message is not None else f"{'、'.join(missing)}信息不能为空")

class BookNumFormatError(BookError):
    """图书总数量格式错误"""
    def __init__(self, total_num):
        self.total_num = total_num
        super().__init__(f"总数量必须为正整数（当前输入：{total_num}）")

class MemberError(LibraryError):
    pass

class MemberNotFoundError(MemberError):
    """用户不存在"""
    def __init__(self, account_id = None, member_id = None, name = None, vip_level = None):
        self.account_id = account_id
        self.member_id = member_id
        self.name = name
        self.vip_level = vip_level
        if account_id:
            super().__init__(f"账号 {account_id} 不存在")
        elif member_id:
            super().__init__(f"编号为 {member_id} 的用户不存在")
        elif name:
            super().__init__(f"姓名为 {name} 的用户不存在")
        elif vip_level is not None:
            super().__init__(f"等级为 {vip_level} 的用户不存在")
        else:
            super().__init__("用户不存在")

class MemberPasswordError(MemberError):
    """用户密码错误"""
    def __init__(self, account_id = None):
        self.account_id = account_id
        if account_id:
            super().__init__(f"账号 {account_id} 密码错误")
        else:
            super().__init__("您的原密码输入错误")

class MemberAlreadyExistsError(MemberError):
    """用户已存在"""
    def __init__(self, account_id):
        self.account_id = account_id
        super().__init__(f"账号 {account_id} 已存在")

class MemberAccountIdFormatError(MemberError):
    """用户账号格式错误"""
    def __init__(self, account_id):
        self.account_id = account_id
        super().__init__(f"账号 {account_id} 格式错误")

class MemberPasswordFormatError(MemberError):
    """用户密码格式错误"""
    def __init__(self):
        super().__init__("密码格式错误")

class MemberNameFormatError(MemberError):
    """用户姓名格式错误"""
    def __init__(self, name):
        self.name = name
        super().__init__(f"姓名 {name} 格式错误")

class MemberFreezeError(MemberError): # TODO:?
    """用户已冻结"""
    def __init__(self, member_id):
        self.member_id = member_id
        super().__init__(f"用户 {member_id} 已冻结")

class MemberInfoEmptyError(MemberError):
    """用户信息为空"""
    def __init__(self, member_id = None, name = None, vip_level = None, message = None):
        self.member_id = member_id
        self.name = name
        self.vip_level = vip_level
        missing = [name for name, value in (('编号', member_id), ('姓名', name), ('等级', vip_level)) if not value and value is not None]
        self.missing_fields = missing
        super().__init__(message if message is not None else f"{'、'.join(missing)}信息不能为空")

class MemberVipLevelFormatError(MemberError):
    """用户等级格式错误"""
    def __init__(self, vip_level):
        self.vip_level = vip_level
        super().__init__(f"等级 {vip_level} 格式错误")

class MemberVipLevelLimitError(MemberError):
    """用户等级超出限制"""
    def __init__(self, vip_level):
        self.vip_level = vip_level
        super().__init__(f"等级超出限制（当前等级：{vip_level}）")

class MemberBooksNotReturnError(MemberError):
    """用户有书未归还"""
    def __init__(self, records):
        self.records = records
        super().__init__(f"您有书未归还，无法注销账户（包括：{'、'.join([f'《{book['title']}》' for book in records])}）")

class AdminError(LibraryError):
    pass

class AdminDeleteLastError(AdminError):
    """最后一个管理员无法注销"""
    def __init__(self):
        super().__init__("最后一个管理员无法注销")

class BorrowError(LibraryError):
    pass

class DuplicateBorrowError(BorrowError):
    """重复借阅"""
    def __init__(self, book_id):
        self.book_id = book_id
        super().__init__(f"您已借过编号为 {book_id} 的图书（同一本书一人最多借阅一本）")

class BorrowLimitError(BorrowError):
    """借阅数量超出限制"""
    def __init__(self, max_books):
        self.max_books = max_books
        super().__init__(f"您已达到借阅数量上限，您最多可以借阅 {max_books} 本图书")

class BookNotBorrowedError(BorrowError):
    """图书未借阅（还书时校验用）"""
    def __init__(self, book_id):
        self.book_id = book_id
        super().__init__(f"您未借阅编号为 {book_id} 的图书，无法归还")