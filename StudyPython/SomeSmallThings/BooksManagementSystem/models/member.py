from datetime import date

from models.book import Book
from utils.hash_utils import verify_password


class Member:
    """用户

    Attributes:
        member_id: 编号
        account_id: 账号
        name: 姓名
        vip_level: 等级
        __hashed_password: 密码哈希值
        __borrowed_books: 正在借阅的图书

    Methods:
        borrow_book: 借阅图书
        return_book: 归还图书
        verify_password: 验证密码
        get_borrowed_books: 获取正在借阅的图书
        change_hashed_password: 修改密码哈希值
        get_max_books: 获取可借阅的最大图书数量
        from_dict: 从字典中创建用户对象
        to_dict: 将用户对象转换为字典
    """
    def __init__(self, member_id: str, account_id: str, name: str, hashed_password: str, vip_level: int = 0, borrowed_books = None):
        self.member_id: str = member_id
        self.account_id: str = account_id
        self.name: str = name
        self.vip_level: int = vip_level # 0 1 2
        self.__hashed_password: str = hashed_password
        self.__borrowed_books: list[dict[str,str]] = borrowed_books if borrowed_books is not None else []

    def borrow_book(self, book: Book):
        self.__borrowed_books.append({'book_id': book.book_id, 'borrow_date': date.today().strftime("%Y年%m月%d日")})

    def return_book(self, book: Book):
        self.__borrowed_books = [dic for dic in self.__borrowed_books if dic['book_id'] != book.book_id]

    def verify_password(self, password: str) -> bool:
        return verify_password(self.__hashed_password, password)

    def get_borrowed_books(self) -> list[dict[str,str]]:
        return self.__borrowed_books.copy()

    def change_hashed_password(self, new_hashed_password):
        self.__hashed_password = new_hashed_password

    def get_max_books(self) -> int:
        return 3 + 3 * self.vip_level

    @classmethod
    def from_dict(cls, member_dict: dict) -> "Member":
        return cls(
            member_dict["member_id"],
            member_dict["account_id"],
            member_dict["name"],
            member_dict["hashed_password"],
            member_dict["vip_level"],
            member_dict["borrowed_books"]
        )

    def to_dict(self) -> dict:
        return {
            "member_id": self.member_id,
            "account_id": self.account_id,
            "name": self.name,
            "vip_level": self.vip_level,
            "hashed_password": self.__hashed_password,
            "borrowed_books": self.__borrowed_books
        }