"""This task ensures that the file has exactly one EOF newline."""

import task


class Newline(task.Task):

    def run(self, name, lines):
        linesep = task.get_linesep(lines)

        newlines = 0
        pos = len(lines) - 1

        # While last character is a newline
        while pos >= 0 and lines[pos] == "\n":
            newlines += 1

            # Seek to character before newline
            pos -= len(linesep)

        if newlines < 1:
            # Append newline to end of file
            return (lines + linesep, True, True)
        elif newlines > 1:
            # Truncate all but one newline
            return (lines[0:len(lines) - len(linesep) * (newlines - 1)], True,
                    True)
        else:
            return (lines, False, True)
