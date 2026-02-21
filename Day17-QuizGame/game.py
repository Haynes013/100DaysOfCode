class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1





user_1 = User("1", "Mark")
user_2 = User("2", "Shi")
print(f'User 1 is following {user_1.following} people.')

user_1.follow(user_2)
print(f'Now they are following {user_1.following} people!')