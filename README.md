# codeforces-contest-parser
To download the input and output files of all the problems of a particular contest.

# Requirements
 `python3` <br>
 `BeautifulSoup` <br>
 `requests module in python` <br>

# Usage: 
Download this repository manually or by using git clone on terminal.<br>

Open terminal and type: <br>
$ `python3 parser.py contest_number` <br>

`contest_number` can be found in the url of the contest page on Codeforces. The above command will create a directory named `contest_number` e.g. `1371` and inside it input and output of every problem will be stored in directories with problem name.<br>

If you want to just parse a single problem instead of whole contest you can specify it's name after the `contest_number` in command line argument while running the file `parser.py` like below:

$ `python3 parser.py contest_number problem_name` <br>

`problem_name` is the name of problem e.g. `A`, `B`, `D1` etc. <br>
Suppose the problem has 4 test cases then it will create 4 files for input with name `in0, in1, in2, in3` and 4 files for output with name `out0, out1, out2, ou3`.


# Preview:

![First Way](https://i.ibb.co/PW5rJQT/term.png) <br>

**Note**: you can also give the contest number and problem name(optional) as input.

![Second Way](https://i.ibb.co/840VNfJ/term2.png) <br>


