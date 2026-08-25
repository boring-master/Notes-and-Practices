from exceptions import (
    LibraryError, MemberAlreadyExistsError, MemberPasswordError,
    MemberNotFoundError, MemberAccountIdFormatError, MemberPasswordFormatError,
    MemberNameFormatError, BookNotFoundError, BookNotBorrowedError,
    BookNotAvailableError, DuplicateBorrowError, BorrowLimitError,
    BookInfoNotChangeError, BookNumChangeError, BookInfoEmptyError,
    BookNumFormatError, MemberInfoEmptyError, MemberVipLevelFormatError,
    MemberVipLevelLimitError, MemberBooksNotReturnError, AdminDeleteLastError
)
from models.admin import Admin
from models.book import Book
from models.member import Member
from services.library import Library

class LibraryApp:
    """图书馆应用

    Attributes:
        library: 图书馆
        isAdmin: 是否为管理员

    Methods:
        start_menu: 开始菜单
        login_page: 登录页面
        registration_page: 注册页面
        member_main_menu: 用户主菜单
        borrow_book_page: 借阅图书
        return_book_page: 归还图书
        view_borrow_page: 查看借阅
        view_book_page: 查看书目
        change_password_page: 修改密码
        delete_account_page: 账号注销
        admin_main_menu: 管理员主菜单
        add_book_page: 添加书目
        modify_book_info_page: 修改书目
        view_member_page: 查看用户
        modify_member_info_page: 修改用户
    """
    def __init__(self):
        print('-' * 40)
        print(' ' * 13, '图书管理系统')
        print('-' * 40)
        self.library = Library()
        self.isAdmin: bool = False

    def start_menu(self):
        """【开始菜单】"""
        while True:
            print('【开始菜单】')
            print('您好！请选择操作：')
            print('退出【输入0】')
            print('登录【输入1】')
            print('注册【输入2】')
            print('-' * 40)
            choice = input().strip()
            print('-' * 40)
            match choice:
                case '0':
                    print('已退出')
                    break
                case '1':
                    self.login_page()
                case '2':
                    self.registration_page()
                case _:
                    print('请输入合适的数字！')
                    print('-' * 40)

    def login_page(self):
        """【登录页面】"""
        while True:
            print('【登录】')
            account_id = input('请输入您的账号：').strip()
            password = input('请输入您的密码：').strip()
            print('-' * 40)
            try:
                self.library.login(account_id, password)
            except (MemberNotFoundError, MemberPasswordError) as e:
                print(f'登录失败：{e}')
                print('请选择操作：')
                print('返回开始菜单【输入0或其他】')
                print('重新登录【输入1】')
                print('注册【输入2】')
                print('-'*40)
                choice = input().strip()
                print('-'*40)
                match choice:
                    case '1':
                        continue
                    case '2':
                        return self.registration_page(account_id = account_id, password = password)
                    case _:
                        return None
            except LibraryError as e:
                print(f'操作失败：{e}')
                print('-' * 40)
                return None
            print('登录成功！')
            print('-' * 40)
            if isinstance(self.library.current_user, Admin):
                self.isAdmin = True
                return self.admin_main_menu()
            else:
                return self.member_main_menu()

    def registration_page(self, account_id = None, password = None):
        """【注册页面】"""
        name = None
        while True:
            print('【注册】')
            if account_id is None:
                account_id = input('请输入您的账号（长度为11的数字）：').strip()
            if password is None:
                password = input('请输入您的密码（必须包含数字、大写字母和小写字母，长度不得小于8，不得大于64）：').strip()
            if name is None:
                name = input('请输入您的姓名：').strip()
            print('-' * 40)
            try:
                self.library.register(account_id, password, name)
            except (MemberAlreadyExistsError, MemberAccountIdFormatError) as e:
                print(f'注册失败：{e}')
                print('-' * 40)
                account_id = None
                continue
            except MemberPasswordFormatError as e:
                print(f'注册失败：{e}')
                print('-' * 40)
                password = None
                continue
            except MemberNameFormatError as e:
                print(f'注册失败：{e}')
                print('-' * 40)
                name = None
                continue
            except LibraryError as e:
                print(f'操作失败：{e}')
                return None
            print('注册成功！')
            self.isAdmin = False
            return self.member_main_menu()

    def member_main_menu(self):
        """【用户主菜单】"""
        while True:
            print('【主菜单】')
            print(f'您好！{self.library.current_user.name}')
            print(f'当前等级：{self.library.current_user.vip_level}')
            print(f'正在借阅：{len(self.library.current_user.get_borrowed_books())}本')
            print(f'还可借阅：{max(0, self.library.current_user.get_max_books() - len(self.library.current_user.get_borrowed_books()))}本')
            print('请选择操作：')
            print('退出登录【输入0】')
            print('借阅图书【输入1】')
            print('归还图书【输入2】')
            print('查看借阅【输入3】')
            print('查看书目【输入4】')
            print('修改密码【输入5】')
            print('账号注销【输入6】')
            print('-' * 40)
            choice = input().strip()
            print('-' * 40)
            match choice:
                case '0':
                    self.library.current_user = None
                    return
                case '1':
                    self.borrow_book_page()
                case '2':
                    self.return_book_page()
                case '3':
                    self.view_borrow_page()
                case '4':
                    self.view_book_page()
                case '5':
                    self.change_password_page()
                case '6':
                    if self.delete_account_page():
                        return
                case _:
                    print('请输入合适的数字！')
                    print('-' * 40)

    def borrow_book_page(self, book_id: str|None = None) -> bool|None:
        """【借阅图书】"""
        current_book_id = book_id
        while True:
            if current_book_id is None:
                print('【借阅图书】')
                current_book_id = input('请输入要借阅的图书的编号：').strip()
            try:
                self.library.borrow_book(current_book_id)
            except (BookInfoEmptyError, BookNotFoundError, BookNotAvailableError, DuplicateBorrowError, BorrowLimitError) as e:
                print(f'借阅失败：{e}')
                print('-' * 40)
                if book_id is not None:
                    return False
                current_book_id = None
                continue
            except LibraryError as e:
                print(f'操作失败：{e}')
                print('-' * 40)
                return False
            print('借阅成功！')
            print('-' * 40)
            if book_id is not None:
                return True
            while True:
                print('请选择操作：')
                print('返回主菜单【输入0】')
                print('继续借阅【输入1】')
                print('-' * 40)
                choice = input().strip()
                print('-' * 40)
                match choice:
                    case '0':
                        return None
                    case '1':
                        current_book_id = None
                        break
                    case _:
                        print('请输入合适的数字！')
                        print('-' * 40)
                        continue

    def return_book_page(self, book_id: str|None = None) -> bool|None:
        """【归还图书】"""
        current_book_id = book_id
        while True:
            if current_book_id is None:
                print('【归还图书】')
                current_book_id = input('请输入要归还的图书的编号：').strip()
            try:
                self.library.return_book(current_book_id)
            except (BookInfoEmptyError, BookNotFoundError, BookNotBorrowedError) as e:
                print(f'归还失败：{e}')
                print('-' * 40)
                if book_id is not None:
                    return False
                current_book_id = None
                continue
            except LibraryError as e:
                print(f'操作失败：{e}')
                print('-' * 40)
                return False
            print('归还成功！')
            print('-' * 40)
            if book_id is not None:
                return True
            while True:
                print('请选择操作：')
                print('返回主菜单【输入0】')
                print('继续归还【输入1】')
                print('-' * 40)
                choice = input().strip()
                print('-' * 40)
                match choice:
                    case '0':
                        return None
                    case '1':
                        current_book_id = None
                        break
                    case _:
                        print('请输入合适的数字！')
                        print('-' * 40)
                        continue

    def view_borrow_page(self):
        """【查看借阅】"""
        has_searched = False
        records: list[dict[str,str]] = []
        while True:
            print('【查看借阅】')
            if not has_searched:
                records: list[dict[str,str]] = self.library.view_borrowed_books()
                has_searched = True
            if not records:
                print('您没有借阅任何图书！')
                print('-' * 40)
                return
            print('正在借阅的图书列表：')
            max_index = len(records)
            for i, book_data in enumerate(records, 1):
                print(f'{i}. 图书编号：{book_data['book_id']}，书名：《{book_data['title']}》，借阅日期：{book_data['borrow_date']}')
            print('-' * 40)
            print('请选择操作：')
            print('返回主菜单【输入0】')
            print(f'归还图书【输入图书编号前的数字（1~{max_index}）】')
            print('-' * 40)
            choice = input().strip()
            print('-' * 40)
            match choice:
                case '0':
                    return
                case _ if choice.isdigit() and 1 <= int(choice) <= max_index:
                    if self.return_book_page(records[int(choice) - 1]['book_id']):
                        has_searched = False
                case _:
                    print('请输入合适的数字！')
                    print('-' * 40)

    def view_book_page(self):
        """【查看书目】"""
        while True:
            print('【查看书目】')
            print('请选择操作：')
            print('返回主菜单【输入0】')
            print('查看所有书目【输入1】')
            print('按书名查找【输入2】')
            print('按作者查找【输入3】')
            print('-' * 40)
            choice = input().strip()
            print('-' * 40)
            title = author = None
            match choice:
                case '0':
                    return
                case '1':
                    print('【查看所有书目】')
                case '2':
                    print('【按书名查找】')
                    title = input('请输入书名：').strip()
                    if title.startswith('《') and title.endswith('》'):
                        title = title[1:-1].strip()
                case '3':
                    print('【按作者查找】')
                    author = input('请输入作者：').strip()
                case _:
                    print('请输入合适的数字！')
                    print('-' * 40)
                    continue
            result = []
            has_searched = False
            while True:
                try:
                    if not has_searched:
                        result: list[Book] = self.library.view_books(title=title, author=author)
                        has_searched = True
                except (BookNotFoundError, BookInfoEmptyError) as e:
                    print(f'查找失败：{e}')
                    print('-' * 40)
                    break
                except LibraryError as e:
                    print(f'操作失败：{e}')
                    print('-' * 40)
                    return
                max_index = len(result)
                for i, book in enumerate(result, 1):
                    if self.isAdmin:
                        print(f'{i}. 图书编号：{book.book_id}，书名：《{book.title}》，作者：{book.author}，状态：{book.status.value}，总数量：{book.total_num}本，可用数量：{book.get_available_num()}本')
                    else:
                        print(f'{i}. 图书编号：{book.book_id}，书名：《{book.title}》，作者：{book.author}，状态：{"可借阅" if book.member_get_status() else "不可借阅"}')
                print('-' * 40)
                if not self.isAdmin:
                    remaining = max(0, self.library.current_user.get_max_books() - len(self.library.current_user.get_borrowed_books()))
                    print(f'您最多还可借阅{remaining}本图书')
                print('请选择操作：')
                print('返回主菜单【输入0】')
                if self.isAdmin:
                    print(f'修改图书信息【输入图书编号前的数字（1~{max_index}）】')
                else:
                    print(f'借阅图书【输入图书编号前的数字（1~{max_index}）】')
                print(f'返回查找【输入{max_index + 1}】')
                print('-' * 40)
                choice = input().strip()
                print('-' * 40)
                match choice:
                    case '0':
                        return
                    case _ if choice.isdigit() and 1 <= int(choice) <= max_index:
                        if self.isAdmin:
                            if self.modify_book_info_page(result[int(choice) - 1]):
                                has_searched = False
                        else:
                            if self.borrow_book_page(result[int(choice) - 1].book_id):
                                has_searched = False
                        continue
                    case _ if choice.isdigit() and int(choice) == max_index + 1:
                        break
                    case _:
                        print('请输入合适的数字！')
                        print('-' * 40)
                        continue

    def change_password_page(self):
        """【修改密码】"""
        while True:
            print('【修改密码】')
            print('请选择操作：')
            print('返回主菜单【输入0】')
            print('确认修改【输入1】')
            print('-' * 40)
            choice = input().strip()
            print('-' * 40)
            match choice:
                case '0':
                    return
                case '1':
                    try:
                        old_password = input('请输入原密码：').strip()
                        new_password = input('请输入新密码（必须包含数字、大写字母和小写字母，长度不得小于8）：').strip()
                        self.library.change_password(old_password, new_password)
                        print('修改成功！')
                        print('-' * 40)
                        return
                    except (MemberPasswordFormatError, MemberPasswordError) as e:
                        print(f'修改失败：{e}')
                        print('-' * 40)
                        continue
                    except LibraryError as e:
                        print(f'操作失败：{e}')
                        print('-' * 40)
                        return
                case _:
                    print('请输入合适的数字！')
                    print('-' * 40)
                    continue

    def delete_account_page(self):
        """【账号注销】"""
        while True:
            print('【账号注销】')
            print('请选择操作：')
            print('返回主菜单【输入0】')
            print('确认注销【输入1】')
            print('-' * 40)
            choice = input().strip()
            print('-' * 40)
            match choice:
                case '0':
                    return False
                case '1':
                    try:
                        self.library.delete_account()
                    except (MemberBooksNotReturnError, AdminDeleteLastError) as e:
                        print(f'注销失败：{e}')
                        print('-' * 40)
                        return False
                    except LibraryError as e:
                        print(f'操作失败：{e}')
                        print('-' * 40)
                        return False
                    print('注销成功！')
                    print('-' * 40)
                    self.isAdmin = False
                    return True
                case _:
                    print('请输入合适的数字！')
                    print('-' * 40)
                    continue

    def admin_main_menu(self):
        """【管理员主菜单】"""
        while True:
            print('【主菜单】')
            print(f'您好！{self.library.current_user.name}，请选择操作：')
            print('退出登录   【输入0】')
            print('查看书目   【输入1】')
            print('图书采编   【输入2】')
            print('修改图书信息【输入3】')
            print('查看用户列表【输入4】')
            print('修改用户信息【输入5】')
            print('修改密码   【输入6】')
            print('账号注销   【输入7】')
            print('-' * 40)
            choice = input().strip()
            print('-' * 40)
            match choice:
                case '0':
                    self.library.current_user = None
                    self.isAdmin = False
                    return
                case '1':
                    self.view_book_page()
                case '2':
                    self.add_book_page()
                case '3':
                    self.modify_book_info_page()
                case '4':
                    self.view_member_page()
                case '5':
                    self.modify_member_info_page()
                case '6':
                    self.change_password_page()
                case '7':
                    if self.delete_account_page():
                        return
                case _:
                    print('请输入合适的数字！')
                    print('-' * 40)

    def add_book_page(self):
        """【图书采编】"""
        while True:
            print('【图书采编】')
            print('请选择操作：')
            print('返回主菜单【输入0】')
            print('确认采编【输入1】')
            print('-' * 40)
            choice = input().strip()
            print('-' * 40)
            match choice:
                case '0':
                    return
                case '1':
                    while True:
                        title = input('请输入书名：').strip()
                        author = input('请输入作者：').strip()
                        total_num = input('请输入总数量（不填默认为1本）：').strip()
                        if title.startswith('《') and title.endswith('》'):
                            title = title[1:-1].strip()
                        try:
                            self.library.add_book(title, author, total_num)
                        except (BookInfoEmptyError, BookNumFormatError) as e:
                            print(f'采编失败：{e}')
                            print('-' * 40)
                            continue
                        except LibraryError as e:
                            print(f'操作失败：{e}')
                            print('-' * 40)
                            return
                        print('采编成功！')
                        print('-' * 40)
                        break
                case _:
                    print('请输入合适的数字！')
                    print('-' * 40)
                    continue

    def modify_book_info_page(self, book: Book|None = None) -> bool|None:
        """【修改图书信息】"""
        current_book = book
        while True:
            if current_book is None:
                print('【修改图书信息】')
                book_id = input('请输入图书编号：').strip()
                print('-' * 40)
                try:
                    result: list[Book] = self.library.view_books(book_id=book_id)
                except (BookNotFoundError, BookInfoEmptyError) as e:
                    print(f'操作失败：{e}')
                    print('-' * 40)
                    continue
                except LibraryError as e:
                    print(f'操作失败：{e}')
                    print('-' * 40)
                    return None
                current_book = result[0]
            print(
                f'图书编号：{current_book.book_id}\n'
                f'书名：《{current_book.title}》\n'
                f'作者：{current_book.author}\n'
                f'状态：{current_book.status.value}\n'
                f'总数量：{current_book.total_num}本\n'
                f'可用数量：{current_book.get_available_num()}本'
            )
            # TODO:print(borrow_records)?
            print('请选择操作：')
            if book is None:
                print('返回主菜单【输入0】')
            else:
                print('返回【输入0】')
            print('修改书名【输入1】')
            print('修改作者【输入2】')
            print('修改状态【输入3】')
            print('修改总数量【输入4】')
            print('-' * 40)
            choice = input().strip()
            print('-' * 40)
            title = author = status_num = total_num = None
            match choice:
                case '0':
                    return False
                case '1':
                    print('【修改书名】')
                    title = input('请输入新书名：').strip()
                    if title.startswith('《') and title.endswith('》'):
                        title = title[1:-1].strip()
                case '2':
                    print('【修改作者】')
                    author = input('请输入新作者：').strip()
                case '3':
                    print('【修改状态】')
                    print('取消剔旧【输入1】')
                    print('剔旧【输入2】')
                    status_num = input('请选择新状态：').strip()
                    if status_num == '1' or status_num == '2':
                        status_num = int(status_num)
                    else:
                        print('请输入合适的数字！')
                        print('-' * 40)
                        continue
                case '4':
                    print('【修改总数量】')
                    total_num = input('请输入新总数量：').strip()
                case _:
                    print('请输入合适的数字！')
                    print('-' * 40)
                    continue
            print('-' * 40)
            try:
                self.library.modify_book_info(current_book, title, author, status_num, total_num)
            except (BookInfoEmptyError, BookInfoNotChangeError, BookNumFormatError, BookNumChangeError) as e:
                print(f'修改失败：{e}')
                print('-' * 40)
                continue
            except LibraryError as e:
                print(f'操作失败：{e}')
                print('-' * 40)
                return False
            print('修改成功！')
            print('-' * 40)
            if book is not None:
                return True
            else:
                while True:
                    print('请选择操作：')
                    print('返回主菜单【输入0】')
                    print('继续修改当前图书的信息【输入1】')
                    print('修改其他图书的信息【输入2】')
                    print('-' * 40)
                    choice = input().strip()
                    print('-' * 40)
                    match choice:
                        case '0':
                            return False
                        case '1':
                            break
                        case '2':
                            current_book = None
                            break
                        case _:
                            print('请输入合适的数字！')
                            print('-' * 40)
                            continue

    def view_member_page(self):
        """【查看用户列表】"""
        while True:
            print('【用户列表】')
            print('请选择操作：')
            print('返回主菜单【输入0】')
            print('查看所有用户【输入1】')
            print('按编号查找【输入2】')
            print('按姓名查找【输入3】')
            print('按等级查找【输入4】')
            print('-' * 40)
            choice = input().strip()
            print('-' * 40)
            member_id = name = vip_level = None
            match choice:
                case '0':
                    return
                case '1':
                    print('【查看所有用户】')
                case '2':
                    print('【按编号查找】')
                    member_id = input('请输入编号：').strip()
                case '3':
                    print('【按姓名查找】')
                    name = input('请输入姓名：').strip()
                case '4':
                    print('【按等级查找】')
                    vip_level = input('请输入等级（0、1、2）：').strip()
                case _:
                    print('请输入合适的数字！')
                    print('-' * 40)
                    continue
            result = []
            has_searched = False
            while True:
                try:
                    if not has_searched:
                        result: list[Member] = self.library.view_members(member_id, name, vip_level)
                        has_searched = True
                except (MemberInfoEmptyError, MemberNameFormatError, MemberVipLevelFormatError, MemberNotFoundError) as e:
                    print(f'查找失败：{e}')
                    print('-' * 40)
                    break
                except LibraryError as e:
                    print(f'操作失败：{e}')
                    print('-' * 40)
                    return
                max_index = len(result)
                for i, member in enumerate(result, 1):
                    print(f'{i}. 编号：{member.member_id}，账号：{member.account_id}，姓名：{member.name}，等级：{member.vip_level}，最多可借：{member.get_max_books()}本，当前借阅：{'、'.join([f'《{book['title']}》' for book in self.library.view_borrowed_books(member)])}')
                print('-' * 40)
                print('请选择操作：')
                print('返回主菜单【输入0】')
                print(f'修改用户信息【输入1~{max_index}】')
                print(f'返回查找【输入{max_index + 1}】')
                print('-' * 40)
                choice = input().strip()
                print('-' * 40)
                match choice:
                    case '0':
                        return
                    case _ if choice.isdigit() and 1 <= int(choice) <= max_index:
                        if self.modify_member_info_page(result[int(choice) - 1]):
                            has_searched = False
                    case _ if choice.isdigit() and int(choice) == max_index + 1:
                        break
                    case _:
                        print('请输入合适的数字！')
                        print('-' * 40)
                        continue

    def modify_member_info_page(self, member:Member|None = None):
        """【修改用户信息】"""
        current_member = member
        while True:
            if current_member is None:
                print('【修改用户信息】')
                member_id = input('请输入用户编号：').strip()
                print('-' * 40)
                try:
                    result: list[Member] = self.library.view_members(member_id=member_id)
                except (MemberInfoEmptyError, MemberNotFoundError) as e:
                    print(f'操作失败：{e}')
                    print('-' * 40)
                    continue
                except LibraryError as e:
                    print(f'操作失败：{e}')
                    print('-' * 40)
                    return None
                current_member = result[0]
            print(
                f'用户编号：{current_member.member_id}\n'
                f'账号：{current_member.account_id}\n'
                f'姓名：{current_member.name}\n'
                f'等级：{current_member.vip_level}\n'
                f'最多可借：{current_member.get_max_books()}本\n'
                f'当前借阅：{'、'.join([f'《{book['title']}》' for book in self.library.view_borrowed_books(current_member)])}'
            )
            print('请选择操作：')
            if member is None:
                print('返回主菜单【输入0】')
            else:
                print('返回【输入0】')
            print('修改等级【输入1】')
            print('-' * 40)
            choice = input().strip()
            print('-' * 40)
            match choice:
                case '0':
                    return False
                case '1':
                    print('【修改等级】')
                    print('请选择操作：')
                    print('升级【输入1】')
                    print('降级【输入2】')
                    print('-' * 40)
                    vip_num = input().strip()
                    print('-' * 40)
                    if vip_num == '1':
                        vip_bool = True
                    elif vip_num == '2':
                        vip_bool = False
                    else:
                        print('请输入合适的数字！')
                        print('-' * 40)
                        continue
                case _:
                    print('请输入合适的数字！')
                    print('-' * 40)
                    continue
            print('-' * 40)
            try:
                self.library.modify_member_info(current_member, vip_bool)
            except MemberVipLevelLimitError as e:
                print(f'修改失败：{e}')
                print('-' * 40)
                continue
            except LibraryError as e:
                print(f'操作失败：{e}')
                print('-' * 40)
                return False
            print('修改成功！')
            print('-' * 40)
            if member is not None:
                return True
            else:
                while True:
                    print('请选择操作：')
                    print('返回主菜单【输入0】')
                    print('继续修改当前用户的信息【输入1】')
                    print('修改其他用户的信息【输入2】')
                    print('-' * 40)
                    choice = input().strip()
                    print('-' * 40)
                    match choice:
                        case '0':
                            return False
                        case '1':
                            break
                        case '2':
                            current_member = None
                            break
                        case _:
                            print('请输入合适的数字！')
                            print('-' * 40)
                            continue

if __name__ == '__main__':
    library_app = LibraryApp()
    library_app.start_menu()