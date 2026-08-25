import json
import os
from pathlib import Path

from models.admin import Admin
from models.book import Book
from models.member import Member


class DataStorage:
    """数据存储

    Attributes:
        data_dir: 数据目录
        books_file: 图书数据文件
        members_file: 用户数据文件
        records_file: 记录数据文件
        admins_file: 管理员数据文件

    Methods:
        _read_json: 读取 JSON 文件
        _write_json: 写入 JSON 文件
        load_books: 加载图书数据
        save_books: 保存图书数据
        load_members: 加载用户数据
        save_members: 保存用户数据
        load_admins: 加载管理员数据
        save_admins: 保存管理员数据
        load_records: 加载记录数据
        save_records: 保存记录数据
    """
    def __init__(self, base_dir: str|None = None):
        if base_dir is None:
            base_dir = Path(__file__).resolve().parent.parent
        self.data_dir: Path = Path(base_dir) / "data"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.books_file: Path = self.data_dir / "books.json"
        self.members_file: Path = self.data_dir / "members.json"
        self.records_file: Path = self.data_dir / "records.json"
        self.admins_file: Path = self.data_dir / "admins.json"

    def _read_json(self, file_path: Path) -> list[dict]:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return []
                return json.loads(content)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"警告：{file_path} 格式错误，已忽略")
            return []
    def _write_json(self, file_path: Path, data: list[dict]) -> None:
        tmp_path = file_path.with_suffix(".tmp")
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp_path, file_path)

    def load_books(self) -> list[Book]:
        return [Book.from_dict(book) for book in self._read_json(self.books_file)]

    def save_books(self, books: list[Book]) -> None:
        self._write_json(self.books_file, [book.to_dict() for book in books])

    def load_members(self) -> list[Member]:
        return [Member.from_dict(member) for member in self._read_json(self.members_file)]

    def save_members(self, members: list[Member]) -> None:
        self._write_json(self.members_file, [member.to_dict() for member in members])

    def load_admins(self) -> list[Admin]:
        return [Admin.from_dict(admin) for admin in self._read_json(self.admins_file)]

    def save_admins(self, admins: list[Admin]) -> None:
        self._write_json(self.admins_file, [admin.to_dict() for admin in admins])

    def load_records(self): # TODO
        pass

    def save_records(self, records): # TODO
        pass