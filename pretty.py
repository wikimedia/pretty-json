"""A command-line tool to make a JSON file prettier. JSON files thus preened should pass CI."""

import contextlib
import fire
import json
import sys


class PreenComponent:
    def json(self, file_name, dry_run=True):
        """Makes a JSON file pretty.

        Arguments:
           file_name: an input .json file
           dry_run: if True, prints output to stdout; if False, overwrites original file 

        Raises:
            JSONDecodeError if input file is invalid JSON
        """
        with open(file_name, 'r') as inp:
            original = json.load(inp)
        contents = json.dumps(original, indent=4, separators=(',', ':'))
        with contextlib.ExitStack() as stack:
            if dry_run:
                outp = sys.stdout
            else:
                outp = stack.enter_context(open(file_name, 'w'))
            outp.write(contents)


if __name__ == '__main__':
    fire.Fire(PreenComponent)
