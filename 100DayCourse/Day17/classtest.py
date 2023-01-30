# classes use PascalCase
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# everything else uses snake_case
user_1 = User("001", "Andrew")
user_2 = User("002", "Becky")

user_1.follow(user_2)
print(user_1.name)
print(f"Followers: {user_1.followers}")
print(f"Following: {user_1.following}")