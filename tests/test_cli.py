import oi

cli = oi.App('test')
cmd1 = oi.Command(cli, 'cmd1')
cmd2 = oi.Command(cmd1, 'cmd2')
print(cli.parser.parse_args())
