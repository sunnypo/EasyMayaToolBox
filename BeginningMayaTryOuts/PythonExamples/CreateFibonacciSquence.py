from maya import cmds

duplicateTime = [1,2,3,4,5,6,7,8,9,10]


for x in duplicateTime:
    cmds.polyCube(w=1, h=1, d=1, name='gugu%s'%(x))
    cmds.select('gugu%s'%(x))
    cmds.move(x*0.05+1, 0, 0)
    cmds.move(0, 0, 0, 'gugu%s.scalePivot'%(x), 'gugu%s.rotatePivot'%(x))
    cmds.rotate(0, 137.51*x, 0)
#    cmds.select(clear)
