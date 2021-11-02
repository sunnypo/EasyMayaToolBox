from maya import cmds


for x in range(0,300):
    cmds.polyCube(w=1, h=1, d=1, name='gugu%s'%(x))
    cmds.select('gugu%s'%(x))
    cmds.rotate(0, 137.51*x, 0)
    cmds.move(x*0.05+1, 0, 0)
