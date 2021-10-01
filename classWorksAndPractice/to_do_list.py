# uncompleted

todo_list = []


def __str__():
    return todo_list[0], todo_list[1], todo_list[2]


class Todo:
    def __init__(self, description, todo_item, time):
        self.description = self._check_description(description)
        self.todo_item = self._check_todo_item(todo_item)
        self.time = self._check_time(time)

    def __str__(self):
        return self.todo_item + "," + self.time

    def _check_description(self, description):
        if len(description.split()) > 256:
            raise ValueError("Reduce your input.")
        if type(description) != str:
            raise ValueError("Invalid input format")
        return description

    def _check_todo_item(self, todo_item):
        if len(todo_item.split()) > 50:
            raise ValueError("Reduce your input.")
        if type(todo_item) != str:
            raise ValueError("Invalid input format")
        return todo_item

    def _check_time(self, time):
        if len(time.split()) > 5:
            raise ValueError("Reduce your input.")
        if type(time) != str:
            raise ValueError("Invalid input format")
        return time


if __name__ == "__main__":
    todo1 = Todo("I want to wash", "Wash", "2:30")
    todo2 = Todo("I want to cook", "Cook", "5:30")
    todo3 = Todo("I want to code", "Code", "6:30")

    todo_list.append(todo1)
    todo_list.append(todo2)
    todo_list.append(todo3)

    print(todo1)
    print(todo2)
    print(todo3)
