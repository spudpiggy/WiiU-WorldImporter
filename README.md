# What/Why
I decided to look into Minecraft LCE's .ext files cus I want to see if it would be possible to generate them.
The inject method is quite annoying, esp on real hardware.
Turns out the format's dead simple, just worldname, some garbage data, and then the thumbnail as a PNG.
World options are stored in the thumbnail's metadata lol.
Even if you import a PNG without metadata it'll still show up in the game, so I decided i should make this repo and try and make something happen.
I believe PS3 uses the ext format as well, probably most LCEs do so this could be adapted.
-spudpiggy
