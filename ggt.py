import click

@click.command()
@click.argument('keywords', nargs=-1)
def main(keywords):
    """Program that helps you to find useful git commands."""
    print("Parameters: ", " ".join(keywords))
    #for str in keywords:
    #    click.echo('Parameters: %s' % (str))

# For Development: 
# pip install --editable .
