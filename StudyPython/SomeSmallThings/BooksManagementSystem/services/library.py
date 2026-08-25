from exceptions import (
    MemberNotFoundError, MemberPasswordError, MemberAlreadyExistsError,
    MemberAccountIdFormatError, MemberPasswordFormatError, MemberNameFormatError,
    BookNotFoundError, BookNotBorrowedError, BookNotAvailableError,
    DuplicateBorrowError, BorrowLimitError, BookInfoNotChangeError,
    BookNumChangeError, BookInfoEmptyError, BookNumFormatError,
    MemberInfoEmptyError, MemberVipLevelFormatError, MemberVipLevelLimitError,
    MemberBooksNotReturnError, AdminDeleteLastError
)
from models.member import Member
from models.book import BookStatus, Book
from models.admin import Admin
from utils.data_storage import DataStorage
from utils.validation import validate_account_id as vali_acc, validate_password as vali_pwd, validate_name as vali_name
from utils.hash_utils import hash_password as hash_psw
from utils.id_utils import generate_member_id, generate_book_id

class Library:
    """图书馆

    Attributes:
        books: 所有图书
        members: 所有用户
        admins: 所有管理员
        current_user: 当前用户
        data_storage: 数据存储

    Methods:
        load_books_data: 加载图书数据
        load_members_data: 加载用户数据
        load_admins_data: 加载管理员数据
        login: 登录
        _admin_login: 管理员登录
        register: 注册
        borrow_book: 借阅图书
        return_book: 归还图书
        view_borrowed_books: 查看已借阅图书
        view_books: 查看图书
        change_password: 修改密码
        delete_account: 删除账户
        modify_book_info: 修改图书信息
        add_book: 添加图书
        view_members: 查看用户
        modify_member_info: 修改用户信息
    """
    def __init__(self):
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}
        self.admins: dict[str, Admin] = {}
        self.current_user: Admin|Member|None = None
        self.data_storage: DataStorage = DataStorage()
        self.load_books_data()
        self.load_members_data()
        self.load_admins_data()

    def load_books_data(self):
        books_data: list[Book] = self.data_storage.load_books()
        for book in books_data:
            self.books[book.book_id] = book

    def load_members_data(self):
        members_data = self.data_storage.load_members()
        for member in members_data:
            self.members[member.member_id] = member

    def load_admins_data(self):
        admins_data = self.data_storage.load_admins()
        for admin in admins_data:
            self.admins[admin.admin_id] = admin

    def login(self, account_id, password: str):
        member = next((member for member in self.members.values() if member.account_id == account_id), None)
        if member is not None:
            if not member.verify_password(password):
                raise MemberPasswordError(account_id)
            self.current_user = member
            return None
        if any(admin.account_id == account_id for admin in self.admins.values()):
            return self._admin_login(account_id, password)
        raise MemberNotFoundError(account_id=account_id)

    def _admin_login(self, account_id, password):
        admin = next((admin for admin in self.admins.values() if admin.account_id == account_id), None)
        if not admin.verify_password(password):
            raise MemberPasswordError(account_id)
        self.current_user = admin

    def register(self, account_id, password, name):
        if account_id in [member.account_id for member in self.members.values()] or account_id in [admin.account_id for admin in self.admins.values()]:
            raise MemberAlreadyExistsError(account_id)
        if not vali_acc(account_id):
            raise MemberAccountIdFormatError(account_id)
        if not vali_pwd(password):
            raise MemberPasswordFormatError()
        if not vali_name(name):
            raise MemberNameFormatError(name)
        member_id = generate_member_id()
        hashed_password = hash_psw(password)
        member = Member(member_id, account_id, name, hashed_password)
        self.members[member_id] = member
        self.current_user = member
        self.data_storage.save_members(list(self.members.values()))

    def borrow_book(self, book_id):
        if not book_id:
            raise BookInfoEmptyError(book_id = book_id)
        if book_id not in self.books:
            raise BookNotFoundError(book_id = book_id)
        if not self.books[book_id].member_get_status():
            raise BookNotAvailableError(book_id)
        if book_id in [book['book_id'] for book in self.current_user.get_borrowed_books()]:
            raise DuplicateBorrowError(book_id)
        if self.current_user.get_max_books() < len(self.current_user.get_borrowed_books()) + 1:
            raise BorrowLimitError(self.current_user.get_max_books())
        self.current_user.borrow_book(self.books[book_id])
        self.books[book_id].borrow_book()
        self.members[self.current_user.member_id] = self.current_user
        self.data_storage.save_members(list(self.members.values()))
        self.data_storage.save_books(list(self.books.values()))

    def return_book(self, book_id):
        if not book_id:
            raise BookInfoEmptyError(book_id = book_id)
        if book_id not in self.books:
            raise BookNotFoundError(book_id = book_id)
        if book_id not in [book['book_id'] for book in self.current_user.get_borrowed_books()]:
            raise BookNotBorrowedError(book_id)
        self.current_user.return_book(self.books[book_id])
        self.books[book_id].return_book()
        self.members[self.current_user.member_id] = self.current_user
        self.data_storage.save_members(list(self.members.values()))
        self.data_storage.save_books(list(self.books.values()))

    def view_borrowed_books(self, member: Member|None = None) -> list[dict[str,str]]:
        if member is None:
            borrowed_books: list[dict[str,str]] = self.current_user.get_borrowed_books()
        else:
            borrowed_books: list[dict[str,str]] = member.get_borrowed_books()
        records = []
        for book_data in borrowed_books:
            book = self.books.get(book_data['book_id'])
            if book is None:
                continue
            records.append({
                'book_id': book_data['book_id'],
                'title': book.title,
                'borrow_date': book_data['borrow_date']
            })
        return records

    def view_books(self, book_id = None, title = None, author = None) -> list[Book]:
        result = list(self.books.values())
        if title is not None:
            if not title:
                raise BookInfoEmptyError(title = title)
            result = [book for book in result if title in book.title]
        elif author is not None:
            if not author:
                raise BookInfoEmptyError(author = author)
            result = [book for book in result if author in book.author]
        elif book_id is not None:
            if not book_id:
                raise BookInfoEmptyError(book_id = book_id)
            result = [book for book in result if book_id == book.book_id]
        if not result:
            raise BookNotFoundError(book_id = book_id, title = title, author = author)
        status_order = {BookStatus.AVAILABLE: 0, BookStatus.BORROWED: 1, BookStatus.WEEDED: 2}
        return sorted(result, key = lambda book: status_order[book.status]) # 可借阅的优先

    def change_password(self, old_password, new_password):
        if not self.current_user.verify_password(old_password):
            raise MemberPasswordError()
        if not vali_pwd(new_password):
            raise MemberPasswordFormatError()
        self.current_user.change_hashed_password(hash_psw(new_password))
        if isinstance(self.current_user, Admin):
            self.admins[self.current_user.admin_id] = self.current_user
            self.data_storage.save_admins(list(self.admins.values()))
        else:
            self.members[self.current_user.member_id] = self.current_user
            self.data_storage.save_members(list(self.members.values()))

    def delete_account(self):
        if isinstance(self.current_user, Member):
            if self.current_user.get_borrowed_books():
                raise MemberBooksNotReturnError(self.view_borrowed_books(self.current_user))
            del self.members[self.current_user.member_id]
            self.data_storage.save_members(list(self.members.values()))
        else:
            if len(self.admins) == 1:
                raise AdminDeleteLastError()
            del self.admins[self.current_user.admin_id]
            self.data_storage.save_admins(list(self.admins.values()))
        self.current_user = None

    def modify_book_info(self, book: Book, title: str|None, author: str|None, status_num: int|None, total_num: str|None):
        if not title and not author and not status_num and not total_num:
            raise BookInfoEmptyError(message = '信息不能为空')
        if (title is not None and title == book.title) or (author is not None and author == book.author) or ( total_num is not None and total_num.isdigit() and int(total_num) == book.total_num):
            raise BookInfoNotChangeError(book.book_id)
        if title is not None:
            book.title = title
        elif author is not None:
            book.author = author
        elif status_num is not None:
            if status_num == 1 and book.status != BookStatus.WEEDED:
                raise BookInfoNotChangeError(book.book_id)
            elif status_num == 2 and book.status == BookStatus.WEEDED:
                raise BookInfoNotChangeError(book.book_id)
            book.change_status()
        elif total_num is not None:
            try:
                total_num = int(total_num)
            except ValueError:
                raise BookNumFormatError(total_num)
            if total_num <= 0:
                raise BookNumFormatError(total_num)
            if not book.change_num(total_num):
                raise BookNumChangeError(book.book_id, book.total_num, book.get_available_num())
        self.books[book.book_id] = book
        self.data_storage.save_books(list(self.books.values()))

    def add_book(self, title, author, total_num):
        if not title or not author:
            raise BookInfoEmptyError(title = title, author = author)
        if total_num:
            try:
                total_num = int(total_num)
            except ValueError:
                raise BookNumFormatError(total_num)
            if total_num <= 0:
                raise BookNumFormatError(total_num)
        book_id = generate_book_id()
        if not total_num:
            book = Book(book_id, title, author)
        else:
            book = Book(book_id, title, author, total_num)
        self.books[book_id] = book
        self.data_storage.save_books(list(self.books.values()))

    def view_members(self, member_id:str|None = None, name:str|None = None, vip_level:str|None = None) -> list[Member]:
        result = list(self.members.values())
        if member_id is not None:
            if not member_id:
                raise MemberInfoEmptyError(member_id = member_id)
            result = [member for member in result if member.member_id == member_id]
        elif name is not None:
            if not name:
                raise MemberInfoEmptyError(name = name)
            if not vali_name(name):
                raise MemberNameFormatError(name)
            result = [member for member in result if name in member.name]
        elif vip_level is not None:
            if not vip_level:
                raise MemberInfoEmptyError(vip_level = vip_level)
            try:
                vip_level = int(vip_level)
            except ValueError:
                raise MemberVipLevelFormatError(vip_level)
            if vip_level not in (0, 1, 2):
                raise MemberVipLevelFormatError(vip_level)
            result = [member for member in result if member.vip_level == vip_level]
        if not result:
            raise MemberNotFoundError(member_id = member_id, name = name, vip_level = vip_level)
        return result

    def modify_member_info(self, member: Member, vip_bool:bool):
        if vip_bool:
            if member.vip_level == 2:
                raise MemberVipLevelLimitError(member.vip_level)
            member.vip_level += 1
        else:
            if member.vip_level == 0:
                raise MemberVipLevelLimitError(member.vip_level)
            member.vip_level -= 1
        self.members[member.member_id] = member
        self.data_storage.save_members(list(self.members.values()))