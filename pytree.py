#!/usr/bin/env python3
import sys
import os
path = "."
fileCounter = 0
dirCounter = 0


def printer(strs, files, level, final):  # Magic here
    pre = ""
    for i in range(level):
        pre = pre + "│   " if final[i] == 1 else pre + "    "
    print(pre + "└── " + strs) if (strs == files[len(files) - 1]) else print(pre + "├── " + strs)

def gg(subpath):
    return sorted([i for i in os.listdir(subpath) if i[0] != '.'])

def test(subpath, level, p):  # Magic there
    global fileCounter, dirCounter
    files = gg(subpath)
    for i in files:
        if os.path.isdir(subpath + "/" + i) is True:
            dirCounter += 1
            p[level - 1] = 0 if (i == files[len(files) - 1]) else 1
            printer(i, files, level - 1, p)
            test(subpath + "/" + i, level + 1, p)
        else:
            fileCounter += 1
            printer(i, files, level - 1, p)


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) == 2 else "."
    print(path)
    test(path, 1, [1 for n in range(256)])
    print("\n{} directories, {} files".format(dirCounter, fileCounter))

"""
//::::::::://:::::::::::::///////////::::://///:::::::----...-.................................--........---..............-...--
::::::::::::::::::::::::://////////::--::://+oo+/:::::----.................................-........--------......-.............
::::::::::::::::::::///:::/::::::::-----:://+ooo+/::::--.........-.................................-:////+++/-............-.....
:::::::::::///:::::////::::--::---------:://+ooooo+/::----.......................................--:/++oooooso:.................
:::::://////////::////::-:--------------:://+oooooo+/:-----..-.................................--://+++++ossyso:....-...........
/::://///////::::::::::----------------::://+oooooo+++/:--.-.-...............................--::/+++++++oosssso:...-.....-.....
///////:::::::::----------------------::////+++ooooo++++/::----............................--:///+o++++ooooosssso:..............
::::::::---------------------.-------:::/+++++++++////+////////:::::------------........---://++ooo++ooooooosssss+-.............
------------------------------------:///++o+/////////////////////////////////////:::::::::/++++osoooooosssssssssso:.............
-----------------:-:---:------:::::://///////://////////////////////////////////+///++++++++oosysoooosssssysssooss+-............
---------------:-:--:::::::///////////:::::::://////////+++++++//+////////////////++++soooooosysoooosyyyyyyyyyssoso:............
--------:::::::::////////+++++++///:::::::::::////////++++++++++++////////////////+++++osossyyysooossyhhddddhysooss/-...........
:::::://////++++++oooooo+++++//::::::::::::::://///+++++++++++///+/++////////////++///+++syyyysoooooosyhddddhysooss+-.-.........
///++++++ooooooooooo++++///:::::::::::::::::::///++++++++++/////++/+++//+/+++/////////+//+osssssooooosyhdmdhhssoooo+---.........
oooooooooooooooooo++//::::::::::::::::::::::////++++++++++++//////+///////++//++///////////++ssssoossyhmmmdhysooooo+-...........
ooooooooooo+++++++/::::::::::::::::::---:::///+++o++++++++++++//////////////+++++++//////////+oooooshdmmmddhysooooo+-...........
ooooooooo+++++++/:::::::--:::::::::-----:::///++oo++++++++++//////////////////+++////////+/////+ooshddmmddhyso+++oo/-...........
ooooo+++++++++//::-::::---:::::::::::::-::://++oo++++/////////////////////////+//++//////////////+osyyddhyssooooooo/-...........
oooo+++++++++/::::::::---::::///:::::::::://++++++++////::://////+/////////////////////////////////++osyssooooosyys/---.........
ooo+++++++++/::---------:::////////:::::///+++++++++/:::::::::////+++////////////////////////////////++oooooo+oyso++:--.........
o+++++++++//::-----.----::+syhhyo++/:::///++++++++//::::::/::::///++++++////////////////////////////////++ooooooooo+/:---.-.....
+++++//////:----......--:+yyydmmdyo/://////+++++++//::::://:::://////++++++++///////////////////////:/:///+oooosssso+::--.......
/////::::::----.......--/+ohyhmhhdy//////://////////:::::////////////+oooo++++////////////////////////::///++ooossss+/::--......
:::::::-------........--+/odhdmNmho//:::::////://////////+oyhdhhso+++++++o+++++//////////////////////////////+ooyyyso+/::--.....
-------------........--:+oohhhddy+//::::://::::////++++oshhssydNNNmyoo++++++++////////////////////////////////+ooyyys+//:--.....
------------........--::/+osyso/:::::::::::::::/+++ooyhmms//hhdmmNNNdyoo+++////////////////////////////////////++osyso+/::-.....
-----------.........-::://///::::::::::::::::::/+ossydmNy++ymNNNmmmmdho+++/////////:////////////////////////////+ossso+//:-.....
----------.........--:::::::::::::::::::::::::://++oshdmdsshdmmNNmhys+//////::::::::::/::::::///////////////////++ooo+++/:-.....
----------.........---::---:::::::::::::::::::///+++++syhhyshhhhyyo/:::::::::::::::::::::::::::::::/::://///////+/++++++/:-.....
-::::----............----::::::::::::::::::::::///++//////++oo++/////::::::--------::::::::::::::::::::::::://////++++++//:-....
::::::---....-.....-:/++ooooo++////:::::-::::::://///////////////////:::::--------:://::::::::::::::::::::::://////++++++/:--...
::/::::--........-+yyyhhhhyyyyhhyo+/:::--::::::::////::://///////////:::::---------:::::::::::::::::::::::::::://///++/++/:--...
::::::------.....+dmNmmmNNNNmmmmddhy+::-----:::::://::::::::://:::::::::::--:-------------::::::::::::::::::::::://////////:-...
/////:-------...-+dNNmmNNNNMMNNNNmdho:--------::::::::::::-----::::::::::::-----------:::::::::::::::::::::::::::://///////:-...
///::-....--...-:+shmmmmNNNMMMNNNNmho/::--:::-::::::::::---:-:---:::-::::::::::::::::::::::::::------:::::::::::::://///////:--.
//:::-...-....-:/oddmmmNmNNNNNNNNmdy+/:::::::::::::::::::--:--------:::::::::::::::::::::::::------:::::::::::::::://///////:--.
///::----------:/oydmmmNmmmNNNNmdhso+///+/////::///::::::::::::::----:::::::::::::::::::::::::::::::::::::::::::://///+//////:-.
////:--------::/+oyyddmNmmmmmdhhysoo+//:::::::::///:::::::::::::::::----:::::::::::::::::::::::::::::::::::::://////+++//////:--
///:--...---::/+osyhhhdmmdddddhyyso+++/+////////////:::::::::::::::::::::::::::::::::::::::::::::::::::::://///////++++//////::-
///:---.-----::+osyyyhhhhhhddddhyss+++/+//////////////:::::::/:::::::///::::::::/::::::::::::::::::///////////////++++++//////:-
///::---..---::/+oshddmmNmddhhhhyyoso++/+//++//////++///////:/:::////////::::////::::::::::::::://///////////////+++++++//////::
//:::--.-------::/yhddmmNNNNmmdmdhyoo+++++//////+++++++/////://///////:::://////:::::::::::://///////////////////+++++++//++///:
//::------------:/oyhhdddmmmmmmNNmdhyoo+++o+ossyyyhyys++////////////:::::://///:::::::::::////////::::::::::///+++++++++++++///:
::::-----------:::/+oshhdddmddmmddmmmdmhhhdddmdddhyyo++//////////::::::::::::::::::::::///////:::::::::::://///++++++++/++++///:
......----------::::/+oyyyhhhyhhhhhhddddhyyyyyyysso++///:///////:::::::::::::::::::::://///:::::::::::::::://///++++++/++++++//:
......-----------::::/+ossssssssoooosyssooooooooo++/////////////////://:::/::::::::://///:::::::::::::::::://///++++++++++++///:
......-----------::::::/+oooo+oo+++++++++++++++///////////////////////://::::::://:::::::::::::::::::::::::///+++++++++++++++///
.......--------:-::::::::////////////////////////////////////////////////::::::::::::::::::::::::::::::::////++++++++++++++++///
........-------:::::::::::::::::///////////////////////////////////////:::::::::/::::::::::::::::::::////////++++++++++o++++++//
........---------:::::::::::::://///////////////////////////////:::::/:::////:::/::::::::::///:/::::///////++++++++++++oooo+++//
........-------:::::::::::::::::::::////////////////////////////:::::::////////::/::::::::::::://////////++++++++++++oooooo++++/
-.......--:::-:::::::::::::://:::::://///////////////////////::::::::::://///:/::::::::::::////////////+++++++++++++oooooo++++++
-......---:::::::::::::::::/:::///////////////////////////////::::::::::::::::::::::::::::////////////++++++++++++ooooooo++++++/
----------:::::::::::::::::/::::/:////////////////////////////////:::/::::::::::::::/::::::://///////++++++++++oooooooooo++++++/
----------:::::::::::::::::::::///////////////////////////////////::::::::::::::::::::///////////////++++++++oooooooooo+++++++//
-----------:::::::::::::::::::////////////////////////////////////:::::::::::::::::://///////////////++++++oooooooooo+++++++////
----------:::::::::///::::::::/://///////////////////////////+//:::/::::::::/::////////////////////////++++oooooooo+++//+//////:
-----------:::::::::://////::::://///////////////++///////////////////////://////////////////////////+++++++++ooo+++///////////:
-------------:::::::::://////////////////////////+//////////////////+//////////////://://///////////+++++++oooo++++////////:://:
---------------:::::::::///////////////////////+///+++//++++++/+/+++++++///////////////////////////////+++++++/////////:::::::::
----------------::::::::::////++++++++++++++++++++++++++++++++++++++++///////////////////////////////+++++//////::::::::::::::::
-----------------::::::::///////+++++++++++++++o++++++++++++++++////////////////:/::///////////////+//////::////::::::::::::::/:
-------..--------:::::::://///////++++++++++++++++++++++++///////////:://////:/://///////////////////:::::::::::::::::::::::::/:
---:----...------:::::::::////////////++++++/++++//////////////::::::///////::///////::::///:/://:::::::::::::::::::::::::::://:

Don't copy my homework, DO YOUR OWN!
"""
