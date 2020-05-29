# Python-Turtle-Paths

I solve the Turle Python Paths problem by 3 approaches

i) I have 6 directions' files hence I create 6 Turtles and each Turtle will progfress its path one-by-one

ii) I have 6 Turtles for 6 directions' files and they all progress together at the same time using normal FOR loops

iii) I have 6 Turtles for 6 directions' files, hence I use 6 Threads (multi-threading programming) to make 6 Turtles progressing their paths concurrently

I am making Python programs by using PyCharm IDE for Windows from here

https://www.jetbrains.com/pycharm/download/#section=windows



**I) Six Turtles progress one after another, the next Turtle will progress after the previous Turtle has done**

The program for this approach is here 

https://github.com/lequanha/Python-Turtle-Paths/blob/master/eachturtle_directions.py

you have to view python indentation better in raw format at
https://raw.githubusercontent.com/lequanha/Python-Turtle-Paths/master/eachturtle_directions.py

At first the first Blue Turtle runs the file directions-1.txt

![Image of Blue Turtle](https://github.com/lequanha/Python-Turtle-Paths/blob/master/I-Each%20Turtle%20Solution/Each-Pathway.png)

after the Blue Turtle that goes for path of directions-1.txt file, then the Green Turtle progress the second file directions-2.txt as below

![Image of Blue and Green Turtles](https://github.com/lequanha/Python-Turtle-Paths/blob/master/I-Each%20Turtle%20Solution/Each-Path2.png)

Finally, when the program has done, this is the final screen

![Image of Each Solution](https://github.com/lequanha/Python-Turtle-Paths/blob/master/I-Each%20Turtle%20Solution/Each.png)


**II) Six Turtles progress at the same time using FOR loops**

The program for this approach is here 

https://github.com/lequanha/Python-Turtle-Paths/blob/master/allturtles_directions.py

you have to view python indentation better in raw format at
https://raw.githubusercontent.com/lequanha/Python-Turtle-Paths/master/allturtles_directions.py

At first, the 6 Turtles progress 6 files: directions-1.txt, directions-2.txt, directions-3.txt, directions-4.txt, directions-5.txt and directions-6.txt by FOOR loops as below

![Image of All Pathway](https://github.com/lequanha/Python-Turtle-Paths/blob/master/II-All%20Turtles%20Solution/All-Pathway.png)

Then all 6 Turtles complete with same results as the I-Each Solution

![Image of All Turtles](https://github.com/lequanha/Python-Turtle-Paths/blob/master/II-All%20Turtles%20Solution/All.png)


**III) Six Turtles concurrently progress using 6 Threads**

This is multi-threading programming by Python, the program is here

https://github.com/lequanha/Python-Turtle-Paths/blob/master/threads_turtles.py

you have to view python indentation better in raw format at
https://raw.githubusercontent.com/lequanha/Python-Turtle-Paths/master/threads_turtles.py

In compare to the other previous 2 solutions, the multi-threading program executes super-fast than the previous 2 programs,

At first, the Multi-Thread program outputs as 

![Image of Threads Pathway](https://github.com/lequanha/Python-Turtle-Paths/blob/master/III-Multi-Thread%20Solution/Threads-Pathway.png)

when it has all done, this is the output

![Image of Threads](https://github.com/lequanha/Python-Turtle-Paths/blob/master/III-Multi-Thread%20Solution/Threads.png)

**IV) Comparison**

If I execute three programs at the same time, after a while, I have 3 below screens of 3 programs' progresses at the same time

Each-Solution Progress

![Image of Comp1](https://github.com/lequanha/Python-Turtle-Paths/blob/master/III-Multi-Thread%20Solution/each_comparison.png)

All Solution Progress

![Image of Comp2](https://github.com/lequanha/Python-Turtle-Paths/blob/master/III-Multi-Thread%20Solution/all_comparison.png)

Multi-Threading Solution Progress

![Image of Comp3](https://github.com/lequanha/Python-Turtle-Paths/blob/master/III-Multi-Thread%20Solution/threads_comparison.png)

Hence the Multi-Threading program is much quicker, however because of memory multi-threading problem when I try to call Turtle.position() functions, the Multi-Threading program cannot calculate the current positions of each Turtles to have the required outputs for the whole problem.

**V) Outputs

The Results are the same for all 3 programs / 3 solutions however I still copy here then all the same results can be compared

*V.1) The Each Solution outputs into 6 files here* 

The outputs are copied into this folder

https://github.com/lequanha/Python-Turtle-Paths/tree/master/I-Each%20Turtle%20Solution

Results for directions-1.txt
https://github.com/lequanha/Python-Turtle-Paths/blob/master/I-Each%20Turtle%20Solution/eachturtle-1.output

Results for directions-2.txt
https://github.com/lequanha/Python-Turtle-Paths/blob/master/I-Each%20Turtle%20Solution/eachturtle-2.output

Results for directions-3.txt
https://github.com/lequanha/Python-Turtle-Paths/blob/master/I-Each%20Turtle%20Solution/eachturtle-3.output

Results for directions-4.txt
https://github.com/lequanha/Python-Turtle-Paths/blob/master/I-Each%20Turtle%20Solution/eachturtle-4.output

Results for directions-5.txt
https://github.com/lequanha/Python-Turtle-Paths/blob/master/I-Each%20Turtle%20Solution/eachturtle-5.output

Results for directions-6.txt
https://github.com/lequanha/Python-Turtle-Paths/blob/master/I-Each%20Turtle%20Solution/eachturtle-6.output











