import re
class Citizen:
    def __init__(self, name, id, email, age):
        self.id = id
        self.name = self.is_valid_name(name)
        self.email = self.is_valid_email(email)
        self.age = self.is_valid_age(age)

    def is_valid_name(self, name):
        if len(name) > 20:
            raise ValueError("Name is not valid. It exceeds 20 characters")
        return name

    def is_valid_email(self, email):
        regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.match(regex, email):
            raise ValueError("Invalid email")
        return email

    def is_valid_age(self, age):
        if age < 0 | age > 200:
            raise ValueError("Invalid age")
        return age


# xiaocu = Citizen("Ozi", "1", "oziomaokoroafor@gmail.com", 12)
# xiaocu = Citizen("OzauW839287EJKQ8842792adjhai", "2", "oziomaokoroafor@gmail.com", 45)
xiaocu = Citizen("id1", "xiaoxu gao", "xiaoxugao@gmail.c", 27)

print(xiaocu.email)
print(xiaocu.name)
print(xiaocu.id)
print(xiaocu.age)

