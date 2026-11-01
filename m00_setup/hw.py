# %%
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from importlib.metadata import version
import OCP
from build123d import *
from ocp_vscode import show, show_all, set_defaults, set_port, Camera
from bd_check import check

print(f"buiild123d: {version('build123d')}")
print(f"ocp-vscode: {version('ocp_vscode')}")
print(f"OCP: {OCP.__version__}")

set_defaults(reset_camera=Camera.KEEP)
set_port(3939)

# %%
#check(shape=Box(1,2,3), name="box", volume=6, faces=6, edges=12)


# %%
b = Box(2, 5, 5)
c = Pos(-4, 0, 0)*Cylinder(radius=1, height=20)
s = Pos(-8, 0, 0)*Sphere(radius=2)

show(b, c, s, axes=True, glass=False)

export_step(b, "./m00_setup/box.step")
