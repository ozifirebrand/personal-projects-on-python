import re


# class Citizen:
#     def __init__(self, name, id, email, age):
#         self.id = id
#         self.name = self.is_valid_name(name)
#         self.email = self.is_valid_email(email)
#         self.age = self.is_valid_age(age)
#
#     def is_valid_name(self, name):
#         if len(name) > 20:
#             raise ValueError("Name is not valid. It exceeds 20 characters")
#         return name
#
#     def is_valid_email(self, email):
#         regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
#         if not re.match(regex, email):
#             raise ValueError("Invalid email")
#         return email
#
#     def is_valid_age(self, age):
#         if age < 0 | age > 200:
#             raise ValueError("Invalid age")
#         return age
#
#
class Citizen1:
    def __init__(self, name, id, email, age):
        self.id = id
        self.name = name
        self.email = email
        self.age = age

        @property
        def id(self):
            return self._id

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            if len(value) > 20:
                raise ValueError("Name cannot exceed 20 characters.")
            self._name = value

        @property
        def email(self):
            return self._email

        @email.setter
        def email(self, value):
            regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
            if not re.match(regex, value):
                raise ValueError("It is not an email address.")
            self._email = value

            @property
            def age(self):
                return self._age

            @age.setter
            def age(self, value):
                if value < 0:
                    raise ValueError("Age cannot be negative.")
                self._age = value


# xiaocu = Citizen1("Ozi", "1", "oziomaokoroafor@gmail.com", 12)
xiaocu = Citizen1("OzauW839kjgfduykjyftkhlftydkulkuhr287EJKQ8842792adjhai", "2", "oziomaokoroafor@gmail.com", 45)
# xiaocu = Citizen("id1", "xiaoxu gao", "xiaoxugao@gmail.c", 27)

print(xiaocu.email)
print(xiaocu.name)
print(xiaocu.id)
print(xiaocu.age)
