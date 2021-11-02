from maya import cmds

#you need a origional object at 1 0 0 to begin, and the name have to be gugu0

for x in range(1,101):

    cmds.duplicate('gugu%s'%(x-1))
    cmds.select('gugu%s'%(x))
    cmds.move(0.05, 0.05, 0, relative=True)
    cmds.move(0, 0, 0, 'gugu%s.scalePivot'%(x), 'gugu%s.rotatePivot'%(x))
 
for x in range(1,101):    
    cmds.rotate(0, 137.51*x, 0, 'gugu%s'%(x))
