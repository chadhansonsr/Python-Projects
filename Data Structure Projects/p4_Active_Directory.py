class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    if not group:
        return False
    if user in group.get_users():
        return True
    for subgroup in group.get_groups():
        if is_user_in_group(user, subgroup):
            return True
    return False


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

parent.add_user("dad")
child.add_user("son")
sub_child.add_user("doll")

child.add_group(sub_child)
parent.add_group(child)

user, group = "dad", child
print(is_user_in_group(user, group))  # False

user, group = "mom", parent
print(is_user_in_group(user, group))  # False

user, group = "doll", sub_child
print(is_user_in_group(user, group))  # True

user, group = "doll", parent
print(is_user_in_group(user, group))  # True
