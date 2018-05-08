#!/usr/bin/env python
import sys
from argparse import ArgumentParser

# from hslog.export import EntityTreeExporter
from hslog.parser import LogParser


def main():
    parser = ArgumentParser()
    parser.add_argument("files", nargs="*")
    # https://stackoverflow.com/questions/9226516/
    args = parser.parse_args(sys.argv[1:])

    for filename in args.files:
        parser = LogParser()

        with open(filename) as f:
            parser.read(f)

        # EntityTreeExporter
        for game in parser.games:
            print(f"Found game {repr(game)}")
            exporter = game.export()
            print(exporter.game)


if __name__ == "__main__":
    main()