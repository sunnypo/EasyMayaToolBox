from maya import cmds
import random

# this part is for generating the cubes
for x in range(1,61):
    cmds.polyCube(sx=20, sy=30, sz=30, name='buildings%s'%(x))
    cmds.move(0, 0, 0, 'buildings%s.scalePivot'%(x), 'buildings%s.rotatePivot'%(x))
    cmds.scale(random.randint(5,40),random.randint(20,70),random.randint(10,30),'buildings%s'%(x))
    
# this part is for rendomize the location
for x in range(1,61):
    cmds.move(random.randint(-20,20),0,random.randint(-20,20),'buildings%s'%(x))
