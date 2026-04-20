import questionary
from scaffold.config import ScaffoldConfig

def collect() -> ScaffoldConfig:
    project_name = questionary.text(
        "Project name: ",
    ).ask()

    include_auth = questionary.confirm(
        "Include auth blueprint?",
        default=False
    ).ask()

    blueprint_name = questionary.text(
        "Primary blueprint name:",
        default="home"
    ).ask()

    extra_blueprint = []
    add_more = questionary.confirm(
        "Add additional blueprints?",
        default=False
    ).ask()

    if add_more:
        count = int(questionary.text(
            "How many?",
        ).ask()

        for i in range(count):
            name = questionary.text(
                f"Blueprint {i + 1} name:"
            ).ask()
            extra_blueprint.append(name)

    return ScaffoldConfig(
        project_name=project_name,
        include_auth=include_auth,
        blueprint_name=blueprint_name,
        extra_blueprint=extra_blueprint,
    )
