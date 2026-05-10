
#!/usr/bin/env python3

from my_lib.calc import add, subtract, multiply, divide, power  

import click

@click.group()
def cli():
    """Simple calculator CLI."""

@cli.command("add")
@click.argument("x", type=float)
@click.argument("y", type=float)
def add_cmd(x, y):
    """Add two numbers."""
    result = add(x, y)
    #use colorful output with add

    click.secho(f"{x} + {y} = {add(x, y)}", fg="green")

@cli.command("subtract")
@click.argument("x", type=float)
@click.argument("y", type=float)
def subtract_cmd(x, y):
    """Subtract two numbers."""
    result = subtract(x, y)
    click.secho(f"{x} - {y} = {subtract(x, y)}", fg="yellow")   

@cli.command("multiply")
@click.argument("x", type=float)
@click.argument("y", type=float)
def multiply_cmd(x, y):
    """Multiply two numbers."""
    result = multiply(x, y)
    click.secho(f"{x} * {y} = {multiply(x, y)}", fg="blue")


@cli.command("divide")
@click.argument("x", type=float)
@click.argument("y", type=float)
def divide_cmd(x, y):
    """Divide two numbers."""
    try:
        result = divide(x, y)
        click.secho(f"{x} / {y} = {divide(x, y)}", fg="red")
    except ValueError as e:
        click.secho(str(e), fg="red")


@cli.command("power")
@click.argument("x", type=float)
@click.argument("y", type=float)
def power_cmd(x, y):
    """Raise x to the power of y."""
    result = power(x, y)
    click.secho(f"{x} ** {y} = {power(x, y)}", fg="magenta")


  
if __name__ == "__main__":
    cli()