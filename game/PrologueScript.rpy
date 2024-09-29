# game prologue scene.
image bg prologue1 = "images/story_prologue/prologue1.png"
image bg prologue2 = "images/story_prologue/prologue2.png"
image bg prologue3 = "images/story_prologue/prologue3.png"
image bg prologue4 = "images/story_prologue/prologue4.png"
image bg prologue5 = "images/story_prologue/prologue5.png"
image bg prologue6 = "images/story_prologue/prologue6.png"
image bg prologue7 = "images/story_prologue/prologue7.png"
image bg prologue8 = "images/story_prologue/prologue8.png"
image bg prologue9 = "images/story_prologue/prologue9.png"
image bg prologue10 = "images/story_prologue/prologue10.png"

define you = Character(_("You"))
define muscular_man = Character(_("Muscular Man"))
define wronged_man1 = Character(_("Wronged Man"))
define wronged_man2 = Character(_("Potty-mouth Man"))
define bald_man = Character(_("Bald Man"))

label Prologue:
    $ sayVariable["state"] = SayState.CutScene

    hide screen DefaultUI
    scene prologue1

    you "Ah, today's another bust..."

    "Inside the worn-out tavern, the goddess of fortune hasn't favored you for days now."

    show prologue2

    "Oblivious to the burning frustration within you, a single fly buzzes annoyingly in front of your face."
    "Your concentration on the cards that are to secure today's meal wavers, and all your attention shifts to chasing the fly."

    show prologue3

    "Finally, the fly lands on the tray,"

    show prologue4

    "With all your pent-up frustration, you smack the tray with all your might."

    show prologue5

    "The fly eludes your grasp as if to mock you, and the precariously balanced tray flies off, striking a man sitting far away."

    show prologue6


    muscular_man "Hey you, enough is enough!"

    "The man who was hit by the tray, seemingly quite drunk, begins to take out his anger by grabbing the collar of a bystander."

    wronged_man1 "What, hey? If you're drunk, just crawl home quietly!"
    wronged_man2 "Think you're tough because you're big? Did mommy feed you too much?"

    "As the man's friend joins in with a comment, the scale of the fight begins to grow."

    show prologue7

    "The fight spreads throughout the entire tavern, becoming uncontrollable."
    "Flustered by the chaos caused by a small fly, you lock eyes with a man."

    bald_man "What, you find it funny that I'm bald too? It shines like crazy, doesn't it? Huh?"

    "You turn your back on the man approaching with large strides, slowly turning around to leave the tavern"

    show prologue8

    "The tavern's door slowly closes, and the noise inside begins to fade away."
    "Shrinking in the cold night air, you quicken your pace to shake off the approaching man."

    show prologue9

    you "At least I'm not completely broke..."

    "You have enough money for tomorrow breakfast, but not enough to get to the inn."

    bald_man "Where's this asshole?"

    "You look in the direction of the sound, and judging by the glare in your eyes, it's a bald man chasing you."

    show prologue10

    "With nowhere to lay down, you decide to wander off the beaten path."
    "There's a tower around town that seems to be right under your nose, even though it's quite far away. You head there for now."

    $ sayVariable["state"] = SayState.Normal
    $ persistent.Prologue = True

    return


