import PySimpleGUI as sG
import webbrowser
import os

# Made by FrostyBoiGrim

sG.theme("Default1")
font_path = os.path.join(os.getcwd(), "fonts", "tf2build.ttf")
custom_font = (font_path, 12)
fontTF = ("fonts/TF2secondary.ttf", 10)
fontTFbase = ("fonts/tf2build.ttf", 10)
fontTFtitle = (font_path, 18)
fontTFchat = ("fonts/Verdana Bold", 10)

classesTF2 = ["Scout", "Soldier", "Pyro", "Demoman", "Heavy", "Engineer", "Medic", "Sniper", "Spy"]

taunt_list_allclass = ["The Director's Vision", "The Schadenfreude", "The High Five!", "Shred Alert", "Conga", "Flippin' Awesome", "Rock, Paper, Scissors", "Skullcracker", "Square Dance", "Kazotsky Kick", "Burstchester", "Zoomin Broom", "Mannrobics", "Second Rate Sorcery", "The Victory Lap", "Yeti Punch", "Yeti Smash", "The Fist Bump", "The Scaredy-cat!", "Killer Joke"]
classesTF2_dict = {
    "Scout": ["Default", "Battin' a Thousand", "Deep Fried Desire", "The Boston Breakdance", "The Carlton", "The Bunnyhopper", "Runner's Rhythm", "The Trackman's Touchdown", "The Scooty Scoot", "The Boston Boarder", "Spin-to-Win", "The Homerunner's Hobby", "Killer Signature"],
    "Soldier": ["Default", "Fresh Brewed Victory", "Soldier's Requiem", "The Fubar Fanfare", "Panzer Pants", "Rocket Jockey", "The Profane Puppeteer", "Star-Spangled Strategy"],
    "Pyro": ["Default", "Party Trick", "Pool Party", "The Balloonibouncer", "The Headcase", "The Skating Scorcher", "Scorcher's Solo", "The Hot Wheeler", "Roasty Toasty"],
    "Demoman": ["Default", "Oblooterated", "Spent Well Spirits", "Bad Pipes", "Scotsmann's Stagger", "The Pooped Deck", "The Drunken Sailor", "Drunk Mann's Cannon", "Shanty Shipmate"],
    "Heavy": ["Default", "The Proletariat Posedown", "The Table Tantrum", "The Russian Arms Race", "The Soviet Strongarm", "Bare Knuckle Beatdown", "Russian Rubdown", "Road Rager"],
    "Engineer": ["Default", "Rancho Relaxo", "Bucking Bronco", "The Dueling Banjo", "The Jumping Jack", "Texas Truckin'", "Texas Twirl 'Em"],
    "Medic": ["Default", "The Meet the Medic", "Results Are In", "Surgeon's Squeezebox", "Time Out Therapy", "The Mannbulance!", "Doctor's Defibrillators", "Head Doctor"],
    "Sniper": ["Default", "I See You", "The Killer Solo", "Most Wanted", "Didgeridrongo", "Shooter's Stakeout"],
    "Spy": ["Default", "Buy A Life", "The Box Trot", "Disco Fever", "Luxury Lounge", "The Travel Agent", "Tailored Terminal", "Teufort Tango"]
}
current_taunts = []
taunt_list = []
combo_len = 21


# Edits the selected classes config to have a shared taunt and message button
def message_together(class_content):
    if class_content[3] == f"alias randomTaunt   \"exec classes/{selectedClass}_loadout\"":
        line1 = class_content[5]
        line2 = class_content[4]
        line3 = class_content[3]
        line4 = class_content[2]
    else:
        line1 = ""
        line2 = ""
        line3 = ""
        line4 = ""
    line5 = f"bind {selectedKey}   \"randomTauntMessage\""
    line6 = f"alias randomTauntMessage   \"exec classes/{selectedClass}_loadout; exec classes/messages\""
    for _ in range(6):
        class_content.pop(0)
    if class_content[0] == line6:
        for _ in range(3):
            class_content.pop(0)
    try:
        if class_content[1] == f"alias randomTaunt   \"exec classes/{selectedClass}_loadout\"":
            lines = line1 + line2 + line3 + line4 + "\n" + line5 + "\n" + line6
        else:
            lines = line1 + line2 + line3 + line4 + "\n\n" + line5 + "\n" + line6
    except:
        lines = line1 + line2 + line3 + line4 + "\n\n" + line5 + "\n" + line6
    class_content.reverse()
    class_content = "\n".join(class_content)
    return class_content, lines


# Edits the selected classes config to have separate taunt and message buttons
def message_separate(class_content):
    line1 = f"bind {selectedKey}   \"randomTaunt\""
    line2 = f"bind {selectedKey2}   \"randomMessage\""
    line3 = f"alias randomTaunt   \"exec classes/{selectedClass}_loadout\""
    line4 = f"alias randomMessage   \"exec classes/messages\""
    if class_content[6] == f"alias randomTauntMessage   \"exec classes/{selectedClass}_loadout; exec classes/messages\"":
        line5 = class_content[7]
        line6 = class_content[6]
    else:
        line5 = ""
        line6 = ""

    for _ in range(4):
        class_content.pop(0)
    try:
        if class_content[2] == f"alias randomTauntMessage   \"exec classes/{selectedClass}_loadout; exec classes/messages\"" and not class_content[6] == line3:
            for _ in range(4):
                class_content.pop(0)
            lines = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n\n" + line5 + "\n" + line6
        elif class_content[6] == line3 and class_content[2] == f"alias randomTauntMessage   \"exec classes/{selectedClass}_loadout; exec classes/messages\"":
            for _ in range(9):
                class_content.pop(0)
            lines = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n\n" + line5 + "\n" + line6
        elif class_content[3] == line3:
            for _ in range(6):
                class_content.pop(0)
            lines = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + line5 + line6
        else:
            lines = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + line5 + line6
    except:
        lines = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + line5 + line6
    class_content.reverse()
    class_content = "\n".join(class_content)

    return class_content, lines


# Parses the above functions based on user choice
def class_config(extra_path):
    with open(f"{fileLoc}/{extra_path}{selectedClass.lower()}.cfg", "r+") as f:
        f.seek(0, 0)
        class_content = f.read()
        class_content += "\n \n \n \n \n \n "
        class_content = class_content.split("\n")
        class_content.reverse()
        lines = ""

        if values["-checkbox-"]:
            message_together(class_content)
        else:
            message_separate(class_content)

            return class_content, lines


# helps create the file randomBind.cfg which is what glues all the other CFG files together
def random_bind_creation():
    with open(f"{fileLoc}/randomBind.cfg", "r+") as f:
        content = f.read()
        content = content.split("\n")
    print(content)
    content.pop(0)
    content[0] = f"exec classes/{selectedClass}_loadout\n"
    content.pop(10)
    content[10] = f"alias \"{selectedClass}_result\"    \"{selectedClass}_taunt_1\"\n"
    content.pop(20)
    content[20] = f"alias \"{selectedClass}_cycle\"     \"{selectedClass}_rng_1\"\n"
    content.pop(30)
    content[30] = f"alias \"all_classes\"     \"{selectedClass}_cycle\"\n"
    content = "\n".join(content)

    return content


# edits randomBind.cfg to add new classes as they're needed. Its sloppy but it do work tho.
def random_bind_edit(classesUsed):
    with open(f"{fileLoc}/classes/UsedClasses.cfg", "w+") as f:
        classesUsed = "\n".join(classesUsed)
        f.write(classesUsed)
        f.write(f"{selectedClass}\n")
    with open(f"{fileLoc}/randomBind.cfg", "r+") as f:
        f.seek(0, 0)
        contentRB = f.read()
        contentRB = contentRB.split("\n")

    classesUsed = classesUsed.split("\n")
    addedPos = int(len(classesUsed)) - 1
    contentRB.pop(0 + addedPos)
    contentRB[0 + addedPos] = f"exec classes/{selectedClass}_loadout\n"
    contentRB.pop(10 + addedPos)
    contentRB[10 + addedPos] = f"alias \"{selectedClass}_result\"    \"{selectedClass}_taunt_1\"\n"
    contentRB.pop(20 + addedPos)
    contentRB[20 + addedPos] = f"alias \"{selectedClass}_cycle\"     \"{selectedClass}_rng_1\"\n"
    contentRB.pop(30)
    print(classesUsed)
    print(type(classesUsed))
    for i in range(len(classesUsed) - 1):
        classesUsed[i] += "_cycle"
    contentRB[30] = f'alias \"all_classes\"     \"{selectedClass}_cycle; {"; ".join(classesUsed)}\"\n'
    contentRB = "\n".join(contentRB)

    return contentRB


layout = [
    [sG.Text("Toxicity Randomizer Generator", size=(30, 1), font=fontTFtitle)],
    [sG.Text("⸺" * 32)],
    [sG.Input(default_text="C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf/cfg", size=(55, 1), font=fontTFchat,  key="-fileLoc-"), sG.FolderBrowse(button_text="Browse", font=fontTFbase), sG.Button("?", font=fontTFbase, key="help1")],  # Value 0

    [sG.Text("⸺" * 32)],
    [sG.Text("Bind:", font=fontTFbase, size=(4, 1)), sG.Input(default_text="mouse4", size=(14, 1), font=fontTF, enable_events=True, key='-BindSelection-'), sG.Button(button_text="Check", tooltip="Brings you to the TF2 wiki page on keybinds", font=fontTFbase, key="-Link-"), sG.Button("?", font=fontTFbase, key="help2")],
    [sG.Text("", font=fontTFbase, size=(4, 1)), sG.Input(default_text="mouse5", size=(14, 1), font=fontTF, enable_events=True, key='-BindSelection2-', tooltip="used for taunts unless taunts are bound to same key")],
    [sG.Text("⸺" * 32)],

    [sG.Text("Class:", font=fontTFbase, size=(5, 1)), sG.Combo(classesTF2, size=(14, 1), font=fontTF, enable_events=True, key="-ClassSelection-"), sG.Button("?", font=fontTFbase, key="help3")],
    [sG.Text("1", font=fontTFbase, size=(1, 1)), sG.Combo(current_taunts, size=(combo_len, 1), font=fontTF, enable_events=True, key="-taunts0-"),
     sG.Text("2", font=fontTFbase, size=(1, 1)), sG.Combo(current_taunts, size=(combo_len, 1), font=fontTF, enable_events=True, key="-taunts1-"),
     sG.Text("3", font=fontTFbase, size=(1, 1)), sG.Combo(current_taunts, size=(combo_len, 1), font=fontTF, enable_events=True, key="-taunts2-")],
    [sG.Text("4", font=fontTFbase, size=(1, 1)), sG.Combo(current_taunts, size=(combo_len, 1), font=fontTF, enable_events=True, key="-taunts3-"),
     sG.Text("5", font=fontTFbase, size=(1, 1)), sG.Combo(current_taunts, size=(combo_len, 1), font=fontTF, enable_events=True, key="-taunts4-"),
     sG.Text("6", font=fontTFbase, size=(1, 1)), sG.Combo(current_taunts, size=(combo_len, 1), font=fontTF, enable_events=True, key="-taunts5-")],
    [sG.Text("7", font=fontTFbase, size=(1, 1)), sG.Combo(current_taunts, size=(combo_len, 1), font=fontTF, enable_events=True, key="-taunts6-"),
     sG.Text("8", font=fontTFbase, size=(1, 1)), sG.Combo(current_taunts, size=(combo_len, 1), font=fontTF, enable_events=True, key="-taunts7-"),
     sG.Text("9", font=fontTFbase, size=(1, 1)), sG.Combo(current_taunts, size=(combo_len, 1), font=fontTF, enable_events=True, key="-taunts8-")],

    [sG.Text("Messages:", font=fontTFbase, size=(8, 1)), sG.Button("?", font=fontTFbase, key="help4")],
    [sG.Multiline(font=fontTF, size=(80, 15), key="-messageBox-")],
    [sG.Checkbox("Include message bind on taunt?", font=fontTF, key="-checkbox-")],

    [sG.Text("⸺" * 32)],

    [sG.Button("Generate", font=fontTFbase, button_color="white on dark green"), sG.Button("About", font=fontTFbase), sG.Text(' ' * 97), sG.Button("Quit", font=fontTFbase, button_color="white on dark red")]
]

window = sG.Window("Toxic Randomizer Generator", icon="TF2Icon.ico", finalize=True).Layout(layout)

while True:
    event, values = window.read()

    if event == sG.WIN_CLOSED or event == "Quit":
        break

    fileLoc = values["-fileLoc-"]
    selectedKey = values["-BindSelection-"]
    selectedKey2 = values["-BindSelection2-"]
    selectedClass = values["-ClassSelection-"]
    messages = values["-messageBox-"].split("\n")

    if event == "help1":
        sG.Popup("Navigate to the location of your cfg folder. The default location should be:", "C:/Program Files (x86)/Steam/steamapps/common/Team Fortress 2/tf/cfg", font=fontTF, title="About")
        continue
    elif event == "help2":
        sG.Popup("Enter the key you wish to bind the actions to.", title="About", font=fontTF)
        continue
    elif event == "help3":
        sG.Popup("Choose your class, put the taunts you want to be randomly used in order, and then press generate to generate a randomization script for that class", title="About", font=fontTF)
        continue
    elif event == "help4":
        sG.Popup("Enter the messages you want to be randomly generate (One per line), then hit generate to generate a randomization script for the messages", title="About", font=fontTF)
        continue

    if event == "About":
        webbrowser.open("https://github.com/FrostyBoiGrim/ToxicityConfigGenerator")
    if event == "-Link-":
        webbrowser.open("https://wiki.teamfortress.com/wiki/Scripting#List_of_key_names")

    # Makes sure that only the taunts applicable to the selected class are shown
    if event == "-ClassSelection-":
        if selectedClass in classesTF2_dict:
            current_taunts = classesTF2_dict[selectedClass]
            current_taunts = current_taunts + taunt_list_allclass
            for i in range(9):
                window.Element(f"-taunts{i}-").update(values=current_taunts, value=values[f"-taunts{i}-"])

    if event == "Generate":
        # Creates the files needed for the scripts to run (THIS SHIT BREAKS THE PYTHON CODE IF WINDOWS CANT ACCESS IT LOL)
        if not os.path.exists(f"{fileLoc}/taunts/"):
            os.makedirs(f"{fileLoc}/taunts/")
        if not os.path.exists(f"{fileLoc}/classes/"):
            os.makedirs(f"{fileLoc}/classes/")

        if selectedClass not in classesTF2:
            sG.Popup("Please only use classes and taunts provided by the list", title="WARNING", font=fontTF)
            continue

        if selectedKey == selectedKey2:
            sG.Popup("Please use different keys for both bind inputs", title="WARNING", font=fontTF)
            continue

        if os.path.exists(f"{fileLoc}/overrides/"):
            class_config_info = class_config("overrides/")
            with open(f"{fileLoc}/overrides/{selectedClass.lower()}.cfg", "w+") as f2:
                f2.write(str(class_config_info[0]) + "\n" + str(class_config_info[1]))
            if not os.path.exists(f"{fileLoc}/taunts/"):
                with open(f"{fileLoc}/overrides/autoexec.cfg", "a+") as f:
                    f.write("\nexec randomBind\n")
        else:
            class_config_info = class_config("")
            with open(f"{fileLoc}/{selectedClass.lower()}.cfg", "w+") as f2:
                f2.write(str(class_config_info[0]) + "\n" + str(class_config_info[1]))
            if not os.path.exists(f"{fileLoc}/taunts/"):
                with open(f"{fileLoc}/autoexec.cfg", "a+") as f:
                    f.write("\nexec randomBind\n")

        # Creates the taunt cfgs needed to actually perform taunts
        for i in range(9):
            if values[f"-taunts{i}-"] in current_taunts:
                taunt_list.append(values[f"-taunts{i}-"])
        while "" in taunt_list:
            taunt_list.remove("")

        for i in range(len(taunt_list)):
            taunt_list[i] = taunt_list[i].replace(" ", "_")
            with open(f"{fileLoc}/taunts/{taunt_list[i]}.cfg", "w") as f:
                f.seek(0)
                taunt_list[i] = taunt_list[i].replace("_", " ")
                if taunt_list[i] == "Shred Alert":
                    f.write(f"taunt_by_name {taunt_list[i]}")
                else:
                    f.write(f"taunt_by_name Taunt: {taunt_list[i]}")

        # creates the class_loadout configs that allow randomization to work
        with open(f"{fileLoc}/classes/{selectedClass}_loadout.cfg", "w") as f:
            f.seek(0)
            for i in range(len(taunt_list)):
                taunt_list[i] = taunt_list[i].replace(" ", "_")
                if taunt_list[i] == "Default":
                    f.write(f"alias   \"{selectedClass}_taunt_{i + 1}\" \"taunt\"\n")
                else:
                    f.write(f"alias   \"{selectedClass}_taunt_{i+1}\" \"exec taunts/{taunt_list[i]}\"\n")
            f.write("\n")
            for i in range(len(taunt_list)):
                taunt_list[i] = taunt_list[i].replace(" ", "_")
                if i+1 < len(taunt_list):
                    f.write(f"alias   \"{selectedClass}_rng_{i+1}\"   \"alias {selectedClass}_result {selectedClass}_taunt_{i+1}; alias {selectedClass}_cycle {selectedClass}_rng_{i+2}\"\n")
                else:
                    f.write(f"alias   \"{selectedClass}_rng_{i+1}\"   \"alias {selectedClass}_result {selectedClass}_taunt_{i+1}; alias {selectedClass}_cycle {selectedClass}_rng_1\"\n")
            f.write("\n")
            f.write(f"{selectedClass}_result")

        # same as above but for messages
        if messages:
            with open(f"{fileLoc}/classes/messages.cfg", "w") as f:
                f.seek(0)
                for i in range(len(messages)):
                    messages[i] = messages[i].replace('"', "'" * 2)
                    f.write(f"alias   \"message_{i+1}\"          \"say {messages[i]}\"\n")
                f.write("\n")
                for i in range(len(messages)):
                    if i + 1 < len(messages):
                        f.write(f"alias   \"message_rng_{i+1}\"   \"alias message_result message_{i+1}; alias message_cycle message_rng_{i + 2}\"\n")
                    else:
                        f.write(f"alias   \"message_rng_{i+1}\"     \"alias message_result message_{i+1}; alias message_cycle message_rng_1\"\n")
                f.write("\n")
                f.write("message_result")

        # Makes randomBind.cfg which is the fundamental backbone of the scripts
        # Specifically, this creates the file
        try:
            with open(f"{fileLoc}/classes/UsedClasses.cfg", "x+") as f:
                f.seek(0)
                f.write(f"{selectedClass}\n")
            with open(f"{fileLoc}/randomBind.cfg", "x+") as f:
                f.seek(0)
                # This is the default part of randomBind that gets filled in, it handles the random number generation.
                # I'm sure there's a pythonic way to do this but this is so much easier.
                f.write('''\n\n\n\n\n\n\n\n\nexec classes/messages
\n\n\n\n\n\n\n\n\n\nalias "message_result"  "message_1"
\n\n\n\n\n\n\n\n\n\nalias "message_cycle"   "message_rng_1"
\n\n\nalias "message_time"    "message_cycle"

bind  w       +mF\nbind  s       +mB\nbind  a       +mL\nbind  d       +mR

alias +mF     "-back;      +forward;   alias check_F +forward;   all_classes"\nalias +mB     "-forward;   +back;      alias check_B +back;      message_time"\nalias +mL     "-moveright; +moveleft;  alias check_L +moveleft;  all_classes"\nalias +mR     "-moveleft;  +moveright; alias check_R +moveright; message_time"
alias -mF     "-forward;   check_B;    alias check_F none;       message_time"\nalias -mB     "-back;      check_F;    alias check_B none;       all_classes"\nalias -mL     "-moveleft;  check_R;    alias check_L none;       message_time"\nalias -mR     "-moveright; check_L;    alias check_R none;       all_classes"
alias check_F none\nalias check_B none\nalias check_L none\nalias check_R none
alias none    ""

echo "Taunt Generator Loaded"''')
            randomBind = random_bind_creation()
            with open(f"{fileLoc}/randomBind.cfg", "w+") as f:
                f.write(randomBind)
        # and this edits it if it already exists
        except FileExistsError:
            with open(f"{fileLoc}/classes/UsedClasses.cfg", "r+") as f:
                f.seek(0)
                classesUsed = f.read()
                classesUsed = classesUsed.split("\n")
            if selectedClass not in classesUsed:
                randomBindE = random_bind_edit(classesUsed)
                with open(f"{fileLoc}/randomBind.cfg", "w+") as f:
                    f.write(randomBindE)

        sG.Popup("All Done! Restart the app to go again!", title="Finished", font=fontTFbase)
        break

window.close()
