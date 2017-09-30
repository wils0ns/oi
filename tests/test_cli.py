import oi

cli = oi.App('test')
cmd1 = oi.Command(cli, 'cmd1')

print(cli.parser.parse_args())
