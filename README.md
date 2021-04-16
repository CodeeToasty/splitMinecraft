# splitMinecraft
Little command line utility that given a length tells you all the way you can split it in equal parts using, for example, pillars.<br>
In the output the first number for every row tells you which space between pillars will give you a perfect split. <br>
Space between pillars is marked as #, the pillars as @ and the external bounds as "L". <br>

usage: python3 splitMinecraft.py blocks_to_split

output example: splitMinecraft.py 19 <br>
  feasable solutions: <br>
  3 L###@###@###@###@###L <br>
  4 L####@####@####@####L <br>
  9 L#########@#########L <br>
  19 L###################L <br>
