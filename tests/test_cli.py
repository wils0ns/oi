import oi

app = oi.App('myapp')
user_cmd = oi.Command(app, 'user')

user_list_cmd = oi.Command(user_cmd, 'list')

user_add_cmd = oi.Command(user_cmd, 'add')
user_add_cmd.add_argument('--name')
user_add_cmd.add_argument('--email')

print(app.parse())
