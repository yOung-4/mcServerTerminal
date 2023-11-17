import typer
from rich import print
from plugins.instance import get_state, start_instance, stop_instance
from output_style.state import style_state
from plugins.config import get_config
from plugins.config import set_aws_config

app = typer.Typer()


@app.command()
def state(instance_id: str = get_config()["instance"]["default_instance_id"]):
    response = get_state(instance_id)
    color = style_state[response]
    print(
        f"the instance (id: {instance_id}) is now [bold {color}]{response}[/bold {color}]")


@app.command()
def start(instance_id: str = get_config()["instance"]["default_instance_id"]):
    response = start_instance(instance_id)
    color = style_state[response]
    print((
        f"the instance (id: {instance_id}) is now [bold {color}]{response}[/bold {color}]"))


@app.command()
def stop(instance_id: str = get_config()["instance"]["default_instance_id"]):
    response = stop_instance(instance_id)
    color = style_state[response]
    print((
        f"the instance (id: {instance_id}) is now [bold {color}]{response}[/bold {color}]"))


@app.command()
def setup():
    set_aws_config()
    print("[bold green]setted[bold green/]")


if __name__ == "__main__":
    app()
