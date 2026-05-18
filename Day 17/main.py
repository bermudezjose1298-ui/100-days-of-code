class User: 
    def __init__(self, username, user_id):
        self.user = username
        self.id = user_id
        print(username,user_id)
        self.followers = 0
        self.following = 0

    def follow_user(self,user):
        user.followers += 1
        self.following += 1


user_1 = User("Jaime", 1)
user_2 = User("Jeremy", 2)

user_1.follow_user(user_2)
print(user_1.following)
print(user_1.followers)

print(user_2.following)
print(user_2.followers)



