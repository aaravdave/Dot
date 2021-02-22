# DScript
This is DScript, a one-file programming language made in Python. It is like English.
## Download
Download the files (all three of them) and run "dscr.py". You will be given a window. This is the IDLE, and you type your code in there and click the ">" button on the top of the app. It will give the output, and if the output is not the desired output, you can change it and rerun.  
> Note: In the same directory of the compiler and the IDLE, create a folder with the code.dscr. You can create other files, and select it when you run the script.
## Documentation
### Variables
Data can be stored in a variable; you do something like this: ```varname equals value```  
Variables can be called using brackets. Such as: ```[varname]```
### Say
To print things in the console, you use the ```say``` function.  
Context is as such: ```say Hello World!```  
You can use variables in ```say``` functions like this: ```say [varname]```
### If
You can use anything in the if condition. We currently support ```equals``` and ```not equals```. Here is it used in code:
```
user equals orangutan
if [user] not equals human
say You are a [user] and not a human.
end
```
