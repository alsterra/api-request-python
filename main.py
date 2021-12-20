from user import User
from post import Post
app_user1 = User("als@gl.com", "Alsterra Shaad", "pwd1", "Software Engineer")
app_user1.get_user_info()

app_user2 = User("maryum@ml.com","Maryam Aurora Sophia", "pwd2", "DevOps Engineer")
app_user2.get_user_info()

new_post = Post("on a secret mission today.", app_user2.name)
new_post.get_post_info()