import click
import random
import os
import calendar
import datetime


def get_data():
    import pandas

    df = pandas.DataFrame({
        'col_a': [i for i in range(20)],
        'col_b': [j for j in range(20, 40)]
    })
    df.drop(columns='col_b', inplace=True)
    return df


@click.group(epilog="(c) 2025 by the simple_echo project")
@click.version_option()
def cli() -> None:
    """A simple echo program."""
    pass


@cli.command
def get_average() -> None:
    """Print the average of a pandas DataFrame."""
    data = get_data()

    average_a = data['col_a'].mean()
    assert average_a < 10

    click.echo(
        f"The average of col_a is {average_a}"
    )


@cli.command
def get_random_number() -> None:
    """Print a random number."""

    click.echo(
        f"Random number: {random.randint(0, 100)}"
    )
