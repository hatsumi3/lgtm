import click

@click.command()
@click.option('--message','-m', default='LGTM', show_default=True, help='画像の文字列')
@click.argument('keyword')
def cli(keyword, message):
    lgtm(keyword, message)
    click.echo('lgtm') # check active


def lgtm(keyword, message):
    pass