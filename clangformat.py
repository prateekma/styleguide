"""This task runs clang-format on the file."""

import subprocess
import sys

import task


class ClangFormat(task.Task):

    def get_file_extensions(self):
        return task.get_config("cExtensions") + \
            task.get_config("cppHeaderExtensions") + \
            task.get_config("cppSrcExtensions")

    def run(self, name, lines):
        args = ["-assume-filename=" + name, "-style=file", "-"]
        try:
            output = self.run_clangformat("clang-format-3.8", args, lines)
        except FileNotFoundError:
            try:
                output = self.run_clangformat("clang-format", args, lines)
            except FileNotFoundError:
                print(
                    "Error: clang-format not found in PATH. Is it installed?",
                    file=sys.stderr)
                return (lines, False, False)

        if lines == output:
            return (lines, False, True)
        else:
            return (output, True, True)

    @staticmethod
    def run_clangformat(binary, args, lines):
        proc = subprocess.Popen(
            [binary] + args, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        output = proc.communicate(lines.encode())[0]
        return output.decode()
