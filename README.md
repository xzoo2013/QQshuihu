QQshuihu
========

This project is made for the online webpage game QQShuihu from Tencent,China

why I create this script:

Actually this webpage game is so easy to play and everyday there are just a few operations you need to do,like a routine.
What's more, all the  operations are just based on clicking. So I decide to use python to create a script to help me with 
the routines.

The module and tools I have found useful in the little project includes:

PyUserInput: mimick the mouse moves,like click, drag and move

Selenium:    a automating web application but here just help me with the game login

And I have to say that : if you want the script to run on your intended schedule , you can use the linux tool, crontab to help you 
register all the events in the Linux System.

And the general command format is :
 min hour * * * export: display=:0 && your command
 
 ! never should you forget the export: display:=0  !

openGame.py is intended to open the game window and then close it. This is to skip some unregular popups.
the firstActions.py is the main part of the operations. In fact almost all the mian operations are implemented in the first sets of operations.
onlinePrize.py and zhengshou.py is just for some minor tasks.
