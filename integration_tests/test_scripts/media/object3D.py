import wandb
from io import StringIO

output = StringIO()

# Blender v2.76 (sub 0) OBJ File: ''
# www.blender.org
output.write('mtllib cube.mtl\n')
output.write('o Cube\n')
output.write('v 1.000000 -1.000000 -1.000000\n')
output.write('v 1.000000 -1.000000 1.000000\n')
output.write('v -1.000000 -1.000000 1.000000\n')
output.write('v -1.000000 -1.000000 -1.000000\n')
output.write('v 1.000000 1.000000 -0.999999\n')
output.write('v 0.999999 1.000000 1.000001\n')
output.write('v -1.000000 1.000000 1.000000\n')
output.write('v -1.000000 1.000000 -1.000000\n')
output.write('vt 1.000000 0.333333\n')
output.write('vt 1.000000 0.666667\n')
output.write('vt 0.666667 0.666667\n')
output.write('vt 0.666667 0.333333\n')
output.write('vt 0.666667 0.000000\n')
output.write('vt 0.000000 0.333333\n')
output.write('vt 0.000000 0.000000\n')
output.write('vt 0.333333 0.000000\n')
output.write('vt 0.333333 1.000000\n')
output.write('vt 0.000000 1.000000\n')
output.write('vt 0.000000 0.666667\n')
output.write('vt 0.333333 0.333333\n')
output.write('vt 0.333333 0.666667\n')
output.write('vt 1.000000 0.000000\n')
output.write('vn 0.000000 -1.000000 0.000000\n')
output.write('vn 0.000000 1.000000 0.000000\n')
output.write('vn 1.000000 0.000000 0.000000\n')
output.write('vn -0.000000 0.000000 1.000000\n')
output.write('vn -1.000000 -0.000000 -0.000000\n')
output.write('vn 0.000000 0.000000 -1.000000\n')
output.write('usemtl Material\n')
output.write('s off\n')
output.write('f 2/1/1 3/2/1 4/3/1\n')
output.write('f 8/1/2 7/4/2 6/5/2\n')
output.write('f 5/6/3 6/7/3 2/8/3\n')
output.write('f 6/8/4 7/5/4 3/4/4\n')
output.write('f 3/9/5 7/10/5 8/11/5\n')
output.write('f 1/12/6 4/13/6 8/11/6\n')
output.write('f 1/4/1 2/1/1 4/3/1\n')
output.write('f 5/14/2 8/1/2 6/5/2\n')
output.write('f 1/12/3 5/6/3 2/8/3\n')
output.write('f 2/12/4 6/8/4 3/4/4\n')
output.write('f 4/13/5 3/9/5 8/11/5\n')
output.write('f 5/6/6 1/12/6 8/11/6\n')

all_tests = {
    "cube(in-memory)": wandb.Object3D(output, file_type="obj"),
    "cube(file)": wandb.Object3D(open("tests/fixtures/cube.obj")),
    "files(seq)": [
        wandb.Object3D(open("tests/fixtures/bunny.obj")),
        wandb.Object3D(open("tests/fixtures/cube.obj"))
    ]
}

N = 1

if __name__ == "__main__":
    wandb.init(project="test-object3D")
    for i in range(N):
        wandb.log(all_tests)
