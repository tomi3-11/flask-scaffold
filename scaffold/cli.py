import sys
from scaffold.prompt import collect
from scaffold.generator import generate
from scaffold.installer import install


def main():
    print(" Flask Scaffold\n")

    config = collect()
    generate(config)
    install(config)

    print(f"\n{config.project_name} ready. Do this: \ncd {config.project_name} \nflask run")


if __name__ == "__main__"
    main()
