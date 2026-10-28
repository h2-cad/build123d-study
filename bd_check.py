from importlib.metadata import version
import OCP

print(f"build123d == {version('build123d')}")
print(f"ocp-vscode == {version('ocp_vscode')}")
print(f"OCP == {OCP.__version__}")
