from dataclasses import dataclass

@dataclass
class ScaffoldConfig:
    project_name: str
    db_name: str
    include_auth: bool
    blueprint_name: str
