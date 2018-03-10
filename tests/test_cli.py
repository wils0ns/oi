import oi

app = oi.App('myapp')
user_cmd = oi.Command(app, 'user')

user_list_cmd = oi.Command(user_cmd, 'list')

user_add_cmd = oi.Command(user_cmd, 'add', help='add help')
user_add_cmd.add_argument('--name', help='test help     here')
user_add_cmd.add_argument('--email')

print(app.parse_args())
print(user_add_cmd.help_list(markdown=True))
