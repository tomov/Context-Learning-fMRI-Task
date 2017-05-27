Context Learning: fMRI Task
=========

An fMRI task adapting the experimental paradigm from [Gershman (2017)](https://link.springer.com/article/10.3758%2Fs13423-016-1110-x). Written in psychopy

To run the experiment, do the following (roughly):

Step 0: Pre-generate the ITIs and the stimulus sequences for all subjects
---------

We don't want to rely on psychopy for randomizing stuff on-the-fly. Also it's good to have the whole experiment pre-generated for reference. 

Do this once before running any subjects and make sure that the generated stimulus sequences and ITIs look okay.

1) cd itis
2) run gen_itis.sh or something like that to generate itis for all subjects using optseq2  
  they should all be generated in the par/ subdirectory  
  we generate for more subjects than we need just in case; edit script parameters if necessary
3) run parse_itis.py to generate the entire stimulus sequence for all runs for all subjects based on the optseq2 iti's  
  they should all be generated in the csv/ subdirectory and have the form e.g. con001_run0_itis.csv  
  python parse_itis.py -p   # for practice rounds
4) cd ..

Step 1: Run the experiment for a given subject
---------

5) run fmri.psyexp in psychopy  
  the participant should be like: con001, con002, con003, etc  
  it uses this to pick the generated sequence from itis/csv/...  so it should match at least one of the pre-generated files  
  btw on each round of the experiment:  
    a) on test laptop, get to "Beginning round #XX" screen  
    b) on fMRI console, drag and double click the next scan sequence  
        on the first one, make sure the brain is in the yellow box -- adjust as needed  
        on subsequent ones, DON'T MOVE IT  
    c) on fMRI console, hit Apply (the green tick)  
    d) on test laptop, hit space to get to the "Waiting for scanner..." screen  
    e) on fMRI console, wait for dialog box on console and hit Continue  
       (these instructions might be deprecated after the scanner update)  
  
  if something fucks up and you need to restart experiment e.g. from round #4 (including round #4),  
    a) clicks the 'runs' loop  
    b) set 'Selected rows' to 'range(3,9)' NOTE: here it is 0-based! So round #4 is 3 here  
    c) start the experiment as usual  
    Note it will say "Beginning round #1" but in reality it will start round 4 (compare with e.g. con004_run3_itis.csv to make sure the stimuli correspond)  

Step 2: Parse & copy over the subject data
-----------

6) once the experiment is over, copy the resulting csv file from data/ (e.g. con001_blabla.csv) into the snippets/ directory
7) cd snippets
8) run parse.py to parse the data file into a format that is suitable for analysis into output file fmri.csv  
    python parse.py con001_blabla.csv fmri.csv       #  for the first subject     
    python parse.py con002_blabla.csv fmri.csv -a    #  for the subsequent subjects -- this appends to the fmri.csv file  
        note that if you don't do -a, it will overwrite the fmri.csv file, erasing all previous subjects
9) cd .. ; cd ..

Step 3: Visualize / analyze the data for all subjects so far
-----------

10) cp fmri-context-task/snippets/fmri.csv model/fmri.csv
11) cd model/  and open MATLAB and run analyze_gui2.m from there
