# pathfinder_character_randomizer
Randomly generate stats for a pathfinder 2e character

Reason: I wanted to have something that I could click generate random character
on and then have something to use right on the spot. Lots of stuff online seems
incomplete or not up to what I need. The closest to what I want is at
https://lcb931023.github.io/pathfinder_random_character_generator/#

Unfortunately it doesn't seem to be maintained, and also might be for first
edition?

Further stretch goal would be to have the randomness actually based on
distributions that make sense rather than pure chance. Also seems like the stats
for the generator don't always follow the rules (Not following Ancestry,
background, and class ability modifiers).

Current task (2022-11-16):
* Create backend to handle randomization of character
  1. Randomize Character Ancestry, Background, and class
  2. Randomize Character Info: Gender, Age, Height, Weight, Alignment, given
certain dependencies.  
  3. Randomize Languages and Skills, given certain dependencies
  4. Randomize Feats, given certain dependencies.
