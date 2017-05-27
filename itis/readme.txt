


--ntp = total run time = (20 * 4 + 4 * 6) (stimulus / decision / feedback time) * 1.5    about 50% of trial time for jitter -- play around with that
   all the times will add up to this. This is the scan run time (+ whatever Ross adds for sequence) -- we give this # to ross

--tr = 2 seconds. how quickly it goes thru the brain

--tprescan = 0   deprecated

--psdwin = 0 12      = from 0 to 12; window of time 

all the events: --ev R1D1 4 5 --ev R1D2 4 5 --ev R2D1 4 5 --ev R2D2 4 5 --ev test 6 4
      number of seconds, number of trials

--nsearch 10000    = how many times to try

--nkeep 9 * 30     = how many of them to keep

--mtx conLearnDesign_012_v5 --log conLearnDesign_012_v5 --o conLearnDesign_012_v5   == diff output prefixes

--tnullmin 2 --tnullmax 12      = min and maximum jitter (clip)
