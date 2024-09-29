# Load BG
image normal = "images/bgs/BG_normal.png"
image normal glitched:
    glitch("normal", randomkey=None, chroma=False)
    pause 0.2
    glitch("normal", randomkey=None, chroma=False)
    pause 0.1
    glitch("normal", randomkey=None, chroma=False)
    pause 0.3
    "normal"

image midlevel = "images/bgs/BG_midlevel.png"
image midlevel glitched:
    glitch("midlevel", randomkey=None, chroma=False)
    pause 0.2
    glitch("midlevel", randomkey=None, chroma=False)
    pause 0.1
    glitch("midlevel", randomkey=None, chroma=False)
    pause 0.3
    "midlevel"

image abyss = "images/bgs/BG_abyss.png"
image abyss glitched:
    glitch("abyss", randomkey=None, chroma=False)
    pause 0.2
    glitch("abyss", randomkey=None, chroma=False)
    pause 0.1
    glitch("abyss", randomkey=None, chroma=False)
    pause 0.3
    "abyss"

image blackout = "images/bgs/BG_black.png"