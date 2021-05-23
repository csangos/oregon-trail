# oregon-trail
A port of the 1975 HP2000 BASIC version to Python 3.9

I was inspired by Aaron A. Reed's excellent series called "50 Years of Text Games". https://if50.substack.com/p/introduction
I remember my elementary school introduction to the Oregon Trail and how much I looked forward to getting a chance score some keyboard time to play this game.
I hadn't though about this game in decause until Reed started his series by covering details behind why this program was created.
This inspired me to find the earliest source code from 1975 and create a version in Python. The HP2000 BASIC code contains some confusing logic to parse.
It was fun to get nostalgic and dig into this tangled ball of yarn.
One thing I discovered was a fairly ingenious way to select a random event which depends on both a list of numbers and the current minutes of the hour, the later in the hour, the harder the event is likely to be.

This game is super simple to play, and the logic is very straight forward as well. Yet it was ground breaking in 1971 when it debuted,
when few classrooms had any accessing to computing.

There are many things that have been added over time to make this game more enjoyable, playable, and updated, however I wanted to be true to the 1975 version.
The only two changes I made was replacing the use of the derogatory 'Indians' with 'Native Americans' and adding a series of dashses to denote
the change of dates, indicating a new turn.

I hope you enjoy.

-James
