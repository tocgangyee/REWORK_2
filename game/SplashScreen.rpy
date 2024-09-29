image cbclogo = im.Scale("images/logo_lsize_white_wName_transparent.png", 500, 500)

label splashscreen:
    scene black

    show cbclogo with dissolve:
        xalign 0.5
        yalign 0.5

    pause 2.0

    hide cbclogo with dissolve

    pause 1.0
    
    return