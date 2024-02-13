class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def __str__(self):
        return f"<User {self.username}>"

    def __repr__(self):
        return f"<User {self.username}>"


class Admin(User):
    def __init__(self, username: str, password: str, bio: str):
        super().__init__(username, password)
        self.__bio = bio

    @property
    def bio(self):
        return self.__bio

    @bio.setter
    def bio(self, value):
        self.__bio = value


admin = Admin("amir", "pass", "i am an admin for this website")
print(admin)

print(admin.bio)
