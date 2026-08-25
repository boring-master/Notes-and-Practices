from utils.hash_utils import verify_password


class Admin:
    """管理员

    Attributes:
        admin_id: 管理员编号
        account_id: 账号
        name: 姓名
        __hashed_password: 密码哈希值

    Methods:
        verify_password: 验证密码
        change_hashed_password: 修改密码哈希值
        from_dict: 从字典创建管理员对象
        to_dict: 将管理员对象转换为字典
    """
    def __init__(self, admin_id: str, account_id: str, name: str, hashed_password: str):
        self.admin_id: str = admin_id
        self.account_id: str = account_id
        self.name: str = name
        self.__hashed_password: str = hashed_password

    def verify_password(self, password: str) -> bool:
        return verify_password(self.__hashed_password, password)

    def change_hashed_password(self, new_hashed_password):
        self.__hashed_password = new_hashed_password

    @classmethod
    def from_dict(cls, admin_dict: dict) -> "Admin":
        return cls(
            admin_dict["admin_id"],
            admin_dict["account_id"],
            admin_dict["name"],
            admin_dict["hashed_password"]
        )

    def to_dict(self) -> dict:
        return {
            "admin_id": self.admin_id,
            "account_id": self.account_id,
            "name": self.name,
            "hashed_password": self.__hashed_password
        }