class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = ""
        self.set_email(email)

    def get_email(self):
        return self.__email

    def set_email(self, new_email):

        if new_email.count("@") != 1:
            print("Ошибочная почта")
            return

        local, domain = new_email.split("@")
        if "." not in domain:
            print("Ошибочная почта")
            return

        self.__email = new_email

    email = property(get_email, set_email)

k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3] # Ошибочная почта
k.email = 'prince@still@.wait'  # Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait
