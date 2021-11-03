from maya import cmds

#you need a origional object at 1 0 0 to begin, and the name have to be gugu0

rotateAngle=0


for x in range(1,301):
    cmds.duplicate('gugu%s'%(x-1))
    cmds.move(0, x*0.0005, 0, 'gugu%s'%(x))
    cmds.rotate(0, 0, -x*.23, 'gugu%s'%(x))
    cmds.scale(10-(x*x/10000), 10-(x*x/10000), 10-(x*x/10000), 'gugu%s'%(x))
    cmds.move(0, 0, 0, 'gugu%s.scalePivot'%(x), 'gugu%s.rotatePivot'%(x))
 
for x in range(1,301):
    rotateAngle=rotateAngle+137.51
    if rotateAngle>=360:
        rotateAngle=rotateAngle-360
    cmds.rotate(0, rotateAngle, 0, 'gugu%s'%(x),relative=True)
