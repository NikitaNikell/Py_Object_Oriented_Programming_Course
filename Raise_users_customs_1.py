users = {
    "alice": {"name": "Alice Smith", "email": "alice@example.com"},
    "bob": {"name": "Bob Johnson", "email": "bob@example.com"},
    "jack": {"name": "Jack Wild", "email": "jack_wild@example.com"}
}
class UserNotFoundError(Exception):
    def __str__(self):
        return "User not found"

def get_user(username):
    #  напишите реализацию функции
    if username in users:
        return users[username]["name"]
    else:
        raise UserNotFoundError

try:
    username = get_user(input())
except UserNotFoundError as e:
    print(e)
else:
    print(username)