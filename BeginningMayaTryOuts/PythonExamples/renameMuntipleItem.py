from maya import cmds

#you can modify the range, name before and name after

rangeBegin=1   #change the zero into the number that you want to start rename
rangeEnd=8  #change the zero into the number that you want to end rename 

oldName='pCube'
newName='renamedObject'
#for those two number, enter the number range that you want to modify
#must be an integer, can start from not zero

#for the names, you enter the old name without the number at the end 
#and enter the name you want to rename to your object
#keep everything in the ''

for i in range(rangeBegin,rangeEnd+1):
    cmds.rename('%s%s'%(oldName,i),'%s%s'%(newName,i))
