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

**V) Outputs**

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



*V.2) The All Solution outputs into 6 files here* 

The outputs are copied into this folder

https://github.com/lequanha/Python-Turtle-Paths/tree/master/II-All%20Turtles%20Solution
 
Results for directions-1.txt

https://github.com/lequanha/Python-Turtle-Paths/blob/master/II-All%20Turtles%20Solution/allturtle-1.output 

Results for directions-2.txt

https://github.com/lequanha/Python-Turtle-Paths/blob/master/II-All%20Turtles%20Solution/allturtle-2.output 

Results for directions-3.txt

https://github.com/lequanha/Python-Turtle-Paths/blob/master/II-All%20Turtles%20Solution/allturtle-3.output 

Results for directions-4.txt

https://github.com/lequanha/Python-Turtle-Paths/blob/master/II-All%20Turtles%20Solution/allturtle-4.output 

Results for directions-5.txt

https://github.com/lequanha/Python-Turtle-Paths/blob/master/II-All%20Turtles%20Solution/allturtle-5.output 

Results for directions-6.txt

https://github.com/lequanha/Python-Turtle-Paths/blob/master/II-All%20Turtles%20Solution/allturtle-6.output 


The above files show that the 2 programs have same results, also the programs output these results into Console panel of PyCharm area

![Image of PyCharm](https://github.com/lequanha/Python-Turtle-Paths/blob/master/PyCharm/PyCharm.png)

**VI) Conclusions**

Each of the directions' files will output the below 3 results

* The end location of the turtle, 

* The full path that that turtle travelled and 

* All of the points where the turtle has traveled to more than once 

*VI.1) File directions-1.txt*

End location: (7, -9)
 
Full Path: (0,0), (0, 1), (1, 1), (1, 0), (1, 1), (2, 1), (1, 1), (1, 2), (1, 3), (1, 4), (0, 4), (-1, 4), (-1, 5), (-1, 6), (-1, 7), (-1, 8), (-1, 7), (-1, 8), (-1, 9), (-1, 10), (-1, 11), (-1, 12), (0, 12), (-1, 12), (-2, 12), (-2, 13), (-2, 12), (-2, 11), (-2, 10), (-2, 9), (-2, 8), (-2, 7), (-2, 6), (-2, 7), (-2, 8), (-2, 9), (-2, 10), (-1, 10), (-1, 9), (-1, 8), (-1, 7), (-1, 6), (-2, 6), (-2, 7), (-1, 7), (0, 7), (0, 8), (0, 7), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (-1, 10), (-2, 10), (-2, 9), (-2, 8), (-3, 8), (-3, 9), (-4, 9), (-4, 10), (-4, 11), (-4, 10), (-3, 10), (-4, 10), (-5, 10), (-5, 11), (-4, 11), (-4, 12), (-4, 13), (-4, 14), (-5, 14), (-5, 15), (-5, 16), (-4, 16), (-3, 16), (-4, 16), (-4, 17), (-4, 18), (-5, 18), (-6, 18), (-6, 17), (-6, 16), (-6, 17), (-6, 16), (-7, 16), (-8, 16), (-8, 17), (-9, 17), (-9, 16), (-9, 17), (-9, 16), (-10, 16), (-11, 16), (-12, 16), (-13, 16), (-14, 16), (-15, 16), (-16, 16), (-17, 16), (-18, 16), (-19, 16), (-19, 15), (-18, 15), (-18, 14), (-18, 13), (-17, 13), (-16, 13), (-15, 13), (-14, 13), (-15, 13), (-14, 13), (-14, 14), (-13, 14), (-14, 14), (-15, 14), (-16, 14), (-17, 14), (-17, 15), (-18, 15), (-19, 15), (-19, 16), (-19, 17), (-18, 17), (-17, 17), (-16, 17), (-16, 16), (-15, 16), (-15, 15), (-15, 14), (-15, 13), (-15, 14), (-15, 15), (-16, 15), (-17, 15), (-18, 15), (-19, 15), (-20, 15), (-21, 15), (-21, 14), (-20, 14), (-19, 14), (-19, 15), (-20, 15), (-20, 16), (-21, 16), (-21, 15), (-21, 14), (-21, 13), (-20, 13), (-20, 14), (-20, 15), (-19, 15), (-20, 15), (-20, 14), (-20, 13), (-21, 13), (-22, 13), (-21, 13), (-20, 13), (-20, 12), (-20, 11), (-20, 10), (-21, 10), (-21, 11), (-21, 12), (-21, 11), (-21, 10), (-22, 10), (-22, 11), (-22, 12), (-22, 13), (-23, 13), (-23, 14), (-24, 14), (-24, 13), (-24, 12), (-23, 12), (-22, 12), (-22, 11), (-21, 11), (-20, 11), (-21, 11), (-22, 11), (-23, 11), (-24, 11), (-25, 11), (-25, 12), (-25, 13), (-24, 13), (-23, 13), (-23, 14), (-23, 15), (-23, 16), (-23, 17), (-22, 17), (-21, 17), (-21, 16), (-21, 15), (-22, 15), (-23, 15), (-23, 16), (-23, 17), (-23, 18), (-24, 18), (-25, 18), (-24, 18), (-24, 19), (-24, 20), (-24, 21), (-24, 22), (-25, 22), (-26, 22), (-27, 22), (-27, 23), (-26, 23), (-25, 23), (-24, 23), (-24, 22), (-24, 21), (-25, 21), (-26, 21), (-26, 20), (-26, 19), (-26, 18), (-27, 18), (-27, 19), (-28, 19), (-28, 20), (-28, 21), (-29, 21), (-30, 21), (-30, 22), (-30, 23), (-30, 24), (-30, 25), (-30, 26), (-29, 26), (-29, 25), (-29, 24), (-29, 23), (-30, 23), (-31, 23), (-31, 24), (-32, 24), (-33, 24), (-33, 25), (-33, 26), (-33, 25), (-34, 25), (-35, 25), (-35, 24), (-35, 23), (-35, 22), (-35, 21), (-35, 20), (-35, 19), (-34, 19), (-34, 18), (-34, 17), (-34, 16), (-34, 17), (-33, 17), (-32, 17), (-31, 17), (-31, 18), (-31, 19), (-31, 20), (-31, 21), (-31, 20), (-31, 21), (-31, 20), (-31, 19), (-31, 18), (-32, 18), (-32, 17), (-32, 16), (-32, 15), (-32, 14), (-32, 13), (-33, 13), (-32, 13), (-31, 13), (-30, 13), (-30, 14), (-29, 14), (-28, 14), (-27, 14), (-28, 14), (-28, 15), (-27, 15), (-28, 15), (-28, 16), (-28, 17), (-28, 18), (-28, 19), (-27, 19), (-26, 19), (-25, 19), (-24, 19), (-23, 19), (-22, 19), (-21, 19), (-20, 19), (-20, 20), (-19, 20), (-18, 20), (-18, 21), (-19, 21), (-18, 21), (-18, 20), (-19, 20), (-18, 20), (-19, 20), (-20, 20), (-21, 20), (-21, 21), (-21, 22), (-21, 23), (-21, 24), (-20, 24), (-20, 25), (-20, 24), (-20, 23), (-19, 23), (-18, 23), (-18, 22), (-18, 21), (-18, 20), (-18, 19), (-18, 20), (-18, 21), (-19, 21), (-20, 21), (-20, 22), (-20, 23), (-19, 23), (-20, 23), (-21, 23), (-22, 23), (-23, 23), (-23, 22), (-23, 21), (-23, 20), (-23, 19), (-23, 18), (-23, 17), (-22, 17), (-21, 17), (-21, 16), (-21, 15), (-21, 14), (-21, 15), (-20, 15), (-19, 15), (-18, 15), (-17, 15), (-18, 15), (-19, 15), (-19, 14), (-20, 14), (-20, 13), (-19, 13), (-19, 12), (-19, 11), (-19, 10), (-18, 10), (-18, 9), (-17, 9), (-17, 10), (-17, 9), (-17, 8), (-17, 9), (-17, 10), (-17, 11), (-18, 11), (-18, 12), (-18, 11), (-18, 10), (-17, 10), (-16, 10), (-15, 10), (-16, 10), (-16, 11), (-15, 11), (-14, 11), (-13, 11), (-12, 11), (-11, 11), (-11, 12), (-11, 13), (-10, 13), (-9, 13), (-8, 13), (-8, 12), (-8, 11), (-7, 11), (-6, 11), (-5, 11), (-5, 10), (-6, 10), (-7, 10), (-7, 9), (-7, 8), (-7, 9), (-7, 10), (-7, 9), (-7, 8), (-7, 7), (-7, 6), (-7, 5), (-7, 4), (-6, 4), (-5, 4), (-6, 4), (-6, 3), (-6, 2), (-6, 1), (-6, 0), (-6, -1), (-5, -1), (-4, -1), (-3, -1), (-2, -1), (-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2), (3, -2), (4, -2), (4, -3), (4, -4), (3, -4), (3, -5), (3, -6), (2, -6), (2, -5), (2, -4), (2, -3), (3, -3), (4, -3), (5, -3), (6, -3), (6, -4), (6, -5), (7, -5), (8, -5), (7, -5), (7, -6), (8, -6), (8, -5), (9, -5), (10, -5), (10, -6), (10, -7), (11, -7), (11, -8), (11, -9), (11, -10), (11, -11), (10, -11), (10, -10), (10, -11), (10, -12), (9, -12), (8, -12), (8, -13), (9, -13), (9, -14), (9, -13), (9, -14), (9, -15), (9, -14), (10, -14), (10, -15), (11, -15), (11, -16), (11, -15), (11, -16), (10, -16), (10, -15), (10, -14), (10, -13), (9, -13), (10, -13), (11, -13), (12, -13), (12, -12), (12, -11), (12, -10), (12, -9), (11, -9), (10, -9), (10, -8), (11, -8), (11, -7), (11, -8), (11, -9), (12, -9), (13, -9), (14, -9), (15, -9), (15, -8), (15, -9), (15, -8), (15, -7), (15, -6), (16, -6), (16, -7), (16, -8), (15, -8), (14, -8), (13, -8), (12, -8), (12, -7), (12, -6), (13, -6), (14, -6), (14, -5), (15, -5), (15, -6), (15, -7), (15, -8), (15, -9), (14, -9), (14, -10), (13, -10), (13, -11), (13, -12), (13, -13), (13, -14), (12, -14), (11, -14), (10, -14), (9, -14), (9, -13), (8, -13), (8, -12), (9, -12), (10, -12), (11, -12), (11, -13), (11, -12), (11, -11), (10, -11), (10, -12), (9, -12), (8, -12), (8, -11), (7, -11), (7, -10), (7, -9), (7, -8), (7, -9)

Points visited more than once: (1, 1), (-1, 7), (-1, 8), (-1, 12), (-2, 12), (-2, 7), (-2, 8), (-2, 9), (-2, 10), (-1, 10), (-1, 9), (-1, 6), (-2, 6), (0, 7), (0, 8), (-4, 10), (-4, 11), (-4, 16), (-6, 17), (-6, 16), (-9, 17), (-9, 16), (-15, 13), (-14, 13), (-14, 14), (-18, 15), (-19, 15), (-19, 16), (-16, 16), (-15, 16), (-15, 14), (-15, 15), (-17, 15), (-20, 15), (-21, 15), (-21, 14), (-20, 14), (-20, 13), (-21, 13), (-21, 11), (-21, 10), (-22, 13), (-22, 12), (-22, 11), (-20, 11), (-24, 13), (-23, 13), (-23, 14), (-21, 16), (-23, 15), (-23, 16), (-23, 17), (-24, 18), (-24, 22), (-24, 21), (-30, 23), (-33, 25), (-34, 17), (-31, 20), (-31, 21), (-31, 19), (-31, 18), (-32, 17), (-32, 13), (-28, 14), (-28, 15), (-28, 19), (-27, 19), (-26, 19), (-24, 19), (-18, 21), (-18, 20), (-19, 20), (-20, 20), (-20, 24), (-19, 21), (-20, 23), (-19, 23), (-21, 23), (-23, 19), (-23, 18), (-22, 17), (-21, 17), (-19, 14), (-17, 9), (-17, 10), (-18, 11), (-18, 10), (-16, 10), (-5, 11), (-5, 10), (-7, 9), (-7, 10), (-7, 8), (-6, 4), (4, -3), (7, -5), (8, -5), (10, -11), (9, -13), (9, -14), (11, -15), (11, -16), (10, -15), (10, -14), (10, -13), (11, -9), (11, -8), (11, -7), (12, -9), (15, -9), (15, -8), (15, -6), (15, -7), (14, -9), (8, -13), (8, -12), (9, -12), (10, -12), (11, -13), (11, -12), (11, -11), (7, -9)







