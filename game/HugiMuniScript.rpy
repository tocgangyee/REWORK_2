label Huginn_appeared:
    "Huginn is appeared."

    return
label Muninn_appeared:
    "Muninn is appeared."

    return

label Huginn_dead:
    "Huginn's massive body hits the floor and shatters into pieces."

    if persistent.HuginnFirstDead:
        call Huginn_first_meet
    else:
        $ persistent.HuginnFirstDead = True

    return

label Muninn_dead:
    "Muninn's massive body hits the floor and shatters into pieces."

    return