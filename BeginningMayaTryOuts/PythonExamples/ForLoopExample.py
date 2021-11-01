#this is a very basic using python in maya example

from maya import cmds    #do this to enable python use MEL command in maya(api stuff, just add it)

#you need to have the origional object, here gugu to use this
#what it does is select a gugu, move it to x meter in x axis and duplicate the nect one(and it goes back)(this repeat for 5 time because range here is (0,5))

for x in range(0,5):    #range can be any int, or arrey
    cmds.select('gugu%s'%(x))    #use '%s'in string and add %()after to show the reference
    cmds.move(x, 0, 0,'gugu%s'%(x))    #This move things to the coordinate you entered, it is not a vector, after it execute it does not select the result
    cmds.duplicate()    #This is the most simple duplicate, the name of the object will just add up number at the end, after it execute it does not select the result


variableExampleString = 'this is how to make a string variable'    #no need to add anything before if you dont need to, same apply to int or arrey, but sometime arrey is considered as string too when not used properly.
