import ast
import _ast
from pylama.lint import Linter as Abstract


class Linter(Abstract):
    """Linter for flagging print() functions."""

    @staticmethod
    def run(path, code=None, params=None, **meta):
        """Check code for print functions or statements.

        :return list: List of errors.
        """
        import _ast
        messages = []

        tree = ast.parse(code, path)


        for i, node in enumerate(ast.walk(tree)):
            if isinstance(node, _ast.Call):
                try:
                    if node.func.id == 'print':
                        messages.append({'lnum': node.lineno, 'text': 'Found `print` call.'})
                except AttributeError as err:
                    pass

        return messages
