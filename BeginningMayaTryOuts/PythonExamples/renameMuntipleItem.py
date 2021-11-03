from maya import cmds

#you can modify the range, name before and name after

for i in range(1,21):
    cmds.rename('gugu%s'%(i),'lotus_flower%s'%(i))
