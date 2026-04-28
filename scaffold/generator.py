import os
from pathlib import Path
from scaffold.config import ScaffoldConfig


TEMPLATES_DIR = Path(__file__).parent / "templates"


def render(template_name: str, context: dict) -> str:
    template_path = TEMPLATES_DIR / template_name
    content = template_path.read_text()
    for key, value in context.items():
        content = content.replace(f"{{{{{key}}}}}", str(value))
    return content


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def generate(config: ScaffoldConfig):
    root = Path(config.project_name)
    ctx = {
        "project_name": config.project_name,
        "blueprint_name": config.blueprint_name,
        "include_auth": config.include_auth,
    }

    # root files
    write(root / "run.py", render("run.py.tpl", ctx))
    write(root / "config.py", render("config.py.tpl", ctx))
    write(root / ".env", render("env.tpl", ctx))
    write(root / ".env.example", render("env.example.tpl", ctx))
    write(root / ".gitignore", render("gitignore.tpl", ctx))
    write(root / "README.md", f'# {config.project_name}\n)

    # app
    write(root / "app" / "__init__.py", render("app_init.py.tpl", ctx))
    write(root / "app" / "models.py", render("models.py.tpl", ctx))

    # primary blueprint
    bp = config.blueprint_name
    write(root / "app" / "blueprints" / bp / "__init__.py", render("blueprint_init.py.tpl", {"blueprint_name": bp}))
    write(root / "app" / "blueprints" / bp / "routes.py", render("blueprint_routes.py.tpl", {"blueprint_name": bp}))
    write(root / "app" / "blueprints" / bp / "resources.py", render("blueprint_resources.py.tpl", {"blueprint_name": bp}))
    write(root / "app" / "blueprints" / bp / "services.py", render("blueprint_services.py.tpl", {"blueprint_name": bp}))

    # extra blueprints
    for extra in config.extra_blueprints:
        write(root / "app" / "blueprints" / extra / "__init__.py", render("blueprint_init.py.tpl", {"blueprint_name": extra}))
        write(root / "app" / "blueprints" / extra / "routes.py", render("blueprint_routes.py.tpl", {"blueprint_name": extra}))
        write(root / "app" / "blueprints" / extra / "resources.py", render("blueprint_resources.py.tpl", {"blueprint_name": extra}))
        write(root / "app" / "blueprints" / extra / "services.py", render("blueprint_services.py.tpl", {"blueprint_name": extra}))

    # auth
    if config.include_auth:
        write(root / "app" / "blueprints" / "auth" / "__init__.py", render("auth_init.py.tpl", ctx))
        write(root / "app" / "blueprints" / "auth" / "routes.py", render("auth_routes.py.tpl", ctx))
        write(root / "app" / "blueprints" / "auth" / "resources.py", render("auth_resources.py.tpl", ctx))
        write(root / "app" / "blueprints" / "auth" / "services.py", render("auth_services.py.tpl", {"blueprint_name": ctx))

    # tests
    write(root / "tests" / "conftest.py", render("conftest.py.tpl", ctx)

    print(f" Project structure created")
