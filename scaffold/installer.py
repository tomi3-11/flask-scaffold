import subprocess
from pathlib import Path
from scaffold.config import ScaffoldConfig

Deps = [
    "flask",
    "flask-restful",
    "flask-sqlalchemy",
    "flask-migrate",
    "python-dotenv",
}

AUTH_DEPS = [
    "flask-jwt-extended",
]

DEV_DEPS = [
    "ruff",
    "pytest",
]

def run(cmd: list[str], cwd: Path):
    subprocess.run(cmd, cwd=cwd, check=True)


def install(config: ScaffoldConfig):
    root = Path(config.project_name)

    print("Initialising uv...")
    run(["uv", "init", "--no-workspace"], cwd=root)

    # Install the required deps
    print("Initialising dependencies...")
    run(["uv", "add"] + DEPS, cwd=root)

    # Setup the auth dependencies
    if config.include_auth:
        print("Installing auth dependencies.")
        run(["uv", "add"] + AUTH_DEPS, cwd=root)

    # Set up development dependencies
    print("Installing dev dependencies...")
    run(["uv", "add", "--dev"] + DEV_DEPS, cwd=root)

    # Final confirmation message
    print("Installation complete")

    # Give developer instruction on how to proceed
    print("""
    Follow these steps to run your project.
    1. Activate the virtual environment
        > source .venv/bin/activate     # for linix/MacOS
        > .venv\Scripts\activate        # for windows
    2. Set up migration and database
        > flask db init
        > flask db migrate -m "Initial migration"
        > flask db upgrade
    2. Run the project
        > flask run

        Access it add: http://localhost:5000
    """)

