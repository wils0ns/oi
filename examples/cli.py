import oi

app = oi.App('myapp')
user_cmd = oi.Command(app, 'user', help='User management CLI example')

user_list_cmd = oi.Command(user_cmd, 'list', help='List users')

user_add_cmd = oi.Command(user_cmd, 'add', help='Add user')
user_add_cmd.add_argument('--name', help='User name')
user_add_cmd.add_argument('-e', '--email', help='User e-mail')
user_add_cmd.add_argument('--admin', action=oi.Command.ACTION_STORE_TRUE)

print(app.parse_args())
print(user_add_cmd.help_markdown())
