from enum import Enum

class BookStatus(Enum):
    """图书状态"""
    AVAILABLE = '可借阅'
    BORROWED = '已被全部借出'
    WEEDED = '已剔旧'

class Book:
    """图书

    Attributes:
        book_id: 编号
        title: 书名
        author: 作者
        total_num: 总数量
        __available_num: 可用数量
        status: 状态

    Methods:
        borrow_book: 借阅图书
        return_book: 归还图书
        get_available_num: 获取可用图书数量
        member_get_status: 会员获取图书状态
        change_status: 改变图书状态
        change_num: 改变图书数量
        from_dict: 从字典创建图书对象
        to_dict: 将图书对象转换为字典
    """
    def __init__(self, book_id, title, author, total_num = 1, available_num = None, status: BookStatus|str = BookStatus.AVAILABLE):
        self.book_id: str = book_id
        self.title: str = title
        self.author: str = author
        self.total_num: int = total_num
        self.__available_num: int = total_num if available_num is None else available_num
        self.status: BookStatus = status if isinstance(status, BookStatus) else BookStatus(status if status else BookStatus.AVAILABLE.value)

    def borrow_book(self):
        self.__available_num -= 1
        if self.status == BookStatus.AVAILABLE and self.__available_num == 0:
            self.status = BookStatus.BORROWED

    def return_book(self):
        self.__available_num += 1
        if self.status == BookStatus.BORROWED:
            self.status = BookStatus.AVAILABLE

    def get_available_num(self):
        return self.__available_num

    def member_get_status(self):
        return self.status == BookStatus.AVAILABLE

    def change_status(self):
        if self.status == BookStatus.WEEDED:
            self.status = BookStatus.AVAILABLE if self.get_available_num() > 0 else BookStatus.BORROWED
        else:
            self.status = BookStatus.WEEDED

    def change_num(self, total_num):
        if total_num > self.total_num:
            self.__available_num += total_num - self.total_num
            self.total_num = total_num
            if self.status == BookStatus.BORROWED and self.__available_num > 0:
                self.status = BookStatus.AVAILABLE
        else:
            if self.total_num - total_num <= self.__available_num:
                self.__available_num -= self.total_num - total_num
                self.total_num = total_num
                if self.status == BookStatus.AVAILABLE and self.__available_num == 0:
                    self.status = BookStatus.BORROWED
            else:
                return False
        return True

    @classmethod
    def from_dict(cls, book_dict: dict) -> "Book":
        return cls(
            book_dict["book_id"],
            book_dict["title"],
            book_dict["author"],
            book_dict["total_num"],
            book_dict["available_num"],
            book_dict.get("status")
        )

    def to_dict(self) -> dict:
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "total_num": self.total_num,
            "available_num": self.get_available_num(),
            "status": self.status.value
        }
