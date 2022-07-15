# DotScript
This is DotScript, otherwise known as DScript, a programming language made in Python. It is created to mimic English and to be easy to use to learn the fundamentals of programming.
## Download
Download the files (all three of them) and run "dscr.py". You will be given a window. This is the IDLE, and you type your code in there and click the ">" button on the top of the app. It will give the output, and if the output is not the desired output, you can change it and rerun.  
> Note: Create other files in the folder "files". You will be able to run them.
## Documentation
### Variables
Data can be stored in a variable; you do something like this: ```varname equals value```  
Variables can be called using brackets. Such as: ```[varname]```  
For integers, do: ```_i_``` with ```i``` being a number.
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
### Repeat
The repeat syntax uses a ```repeat``` and then the number of times you want to repeat and then ```with``` and then your variable name. Here is it used in code:
```
repeat 5 with i
say [i]
end
```
