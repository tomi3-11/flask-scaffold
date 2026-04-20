from dataclasses import dataclass

@dataclass
class ScaffoldConfig:
    project_name: str
    include_auth: bool
    blueprint_name: str
    extra_blueprints: list[str]
