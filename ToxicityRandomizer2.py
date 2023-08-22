import PySimpleGUI as sG
import webbrowser
import os

# Made by FrostyBoiGrim

sG.theme("Default1")
fontTF = ("TF2 Secondary", 10)
fontTFbase = ("TF2 Build", 10)
fontTFtitle = ("TF2 Build", 18)
fontTFchat = ("Verdana Bold", 10)

classesTF2 = ["Scout", "Soldier", "Pyro", "Demoman", "Heavy", "Engineer", "Medic", "Sniper", "Spy"]

taunt_list_allclass = ["The Director's Vision", "The Schadenfreude", "The High Five!", "Shred Alert", "Conga", "Flippin' Awesome", "Rock, Paper, Scissors", "Skullcracker", "Square Dance", "Kazotsky Kick", "Burstchester", "Zoomin Broom", "Mannrobics", "Second Rate Sorcery", "The Victory Lap", "Yeti Punch", "Yeti Smash", "The Fist Bump", "The Scaredy-cat!", "Killer Joke"]
taunt_list_scout = ["Battin' a Thousand", "Deep Fried Desire", "The Boston Breakdance", "The Carlton", "The Bunnyhopper", "Runner's Rhythm", "The Trackman's Touchdown", "The Scooty Scoot", "The Boston Boarder", "Spin-to-Win", "The Homerunner's Hobby", "Killer Signature"]
taunt_list_soldier = ["Fresh Brewed Victory", "Soldier's Requiem", "The Fubar Fanfare", "Panzer Pants", "Rocket Jockey", "The Profane Puppeteer", "Star-Spangled Strategy"]
taunt_list_pyro = ["Party Trick", "Pool Party", "The Balloonibouncer", "The Headcase", "The Skating Scorcher", "Scorcher's Solo", "The Hot Wheeler", "Roasty Toasty"]
taunt_list_demo = ["Oblooterated", "Spent Well Spirits", "Bad Pipes", "Scotsmann's Stagger", "The Pooped Deck", "The Drunken Sailor", "Drunk Mann's Cannon", "Shanty Shipmate"]
taunt_list_heavy = ["The Proletariat Posedown", "The Table Tantrum", "The Russian Arms Race", "The Soviet Strongarm", "Bare Knuckle Beatdown", "Russian Rubdown", "Road Rager"]
taunt_list_engi = ["Rancho Relaxo", "Bucking Bronco", "The Dueling Banjo", "The Jumping Jack", "Texas Truckin'", "Texas Twirl 'Em"]
taunt_list_medic = ["The Meet the Medic", "Results Are In", "Surgeon's Squeezebox", "Time Out Therapy", "The Mannbulance!", "Doctor's Defibrillators", "Head Doctor"]
taunt_list_sniper = ["I See You", "The Killer Solo", "Most Wanted", "Didgeridrongo", "Shooter's Stakeout"]
taunt_list_spy = ["Buy A Life", "The Box Trot", "Disco Fever", "Luxury Lounge", "The Travel Agent", "Tailored Terminal", "Teufort Tango"]

current_taunts = ["Default"]
combo_len = 21

taunt_list = []

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

    if event == "-ClassSelection-":
        if values["-ClassSelection-"] == "Scout":
            current_taunts = current_taunts[:1]
            current_taunts = current_taunts + taunt_list_scout + taunt_list_allclass
            for i in range(9):
                window.Element(f"-taunts{i}-").update(values=current_taunts, visible=True, value=values[f"-taunts{i}-"])

        elif values["-ClassSelection-"] == "Soldier":
            current_taunts = current_taunts[:1]
            current_taunts = current_taunts + taunt_list_soldier + taunt_list_allclass
            for i in range(9):
                window.Element(f"-taunts{i}-").update(values=current_taunts, visible=True, value=values[f"-taunts{i}-"])
                
        elif values["-ClassSelection-"] == "Pyro":
            current_taunts = current_taunts[:1]
            current_taunts = current_taunts + taunt_list_pyro + taunt_list_allclass
            for i in range(9):
                window.Element(f"-taunts{i}-").update(values=current_taunts, visible=True, value=values[f"-taunts{i}-"])
                
        elif values["-ClassSelection-"] == "Demoman":
            current_taunts = current_taunts[:1]
            current_taunts = current_taunts + taunt_list_demo + taunt_list_allclass
            for i in range(9):
                window.Element(f"-taunts{i}-").update(values=current_taunts, visible=True, value=values[f"-taunts{i}-"])
                
        elif values["-ClassSelection-"] == "Heavy":
            current_taunts = current_taunts[:1]
            current_taunts = current_taunts + taunt_list_heavy + taunt_list_allclass
            for i in range(9):
                window.Element(f"-taunts{i}-").update(values=current_taunts, visible=True, value=values[f"-taunts{i}-"])
                
        elif values["-ClassSelection-"] == "Engineer":
            current_taunts = current_taunts[:1]
            current_taunts = current_taunts + taunt_list_engi + taunt_list_allclass
            for i in range(9):
                window.Element(f"-taunts{i}-").update(values=current_taunts, visible=True, value=values[f"-taunts{i}-"])
                
        elif values["-ClassSelection-"] == "Medic":
            current_taunts = current_taunts[:1]
            current_taunts = current_taunts + taunt_list_medic + taunt_list_allclass
            for i in range(9):
                window.Element(f"-taunts{i}-").update(values=current_taunts, visible=True, value=values[f"-taunts{i}-"])
                
        elif values["-ClassSelection-"] == "Sniper":
            current_taunts = current_taunts[:1]
            current_taunts = current_taunts + taunt_list_sniper + taunt_list_allclass
            for i in range(9):
                window.Element(f"-taunts{i}-").update(values=current_taunts, visible=True, value=values[f"-taunts{i}-"])
                
        elif values["-ClassSelection-"] == "Spy":
            current_taunts = current_taunts[:1]
            current_taunts = current_taunts + taunt_list_spy + taunt_list_allclass
            for i in range(9):
                window.Element(f"-taunts{i}-").update(values=current_taunts, visible=True, value=values[f"-taunts{i}-"])

    if event == "Generate":
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
            with open(f"{fileLoc}/overrides/{selectedClass.lower()}.cfg", "r+") as f:
                f.seek(0, 0)
                content = f.read()
                content += "\n \n \n \n \n \n "
                content = content.split("\n")
                content.reverse()

                if values["-checkbox-"]:
                    if content[3] == f"alias randomTaunt   \"exec classes/{selectedClass}_loadout\"":
                        line1 = content[5]
                        line2 = content[4]
                        line3 = content[3]
                        line4 = content[2]
                    else:
                        line1 = ""
                        line2 = ""
                        line3 = ""
                        line4 = ""
                    line5 = f"bind {selectedKey}   \"randomTauntMessage\""
                    line6 = f"alias randomTauntMessage   \"exec classes/{selectedClass}_loadout; exec classes/messages\""
                    for i in range(6):
                        content.pop(0)
                    if content[0] == line6:
                        for i in range(3):
                            content.pop(0)
                    try:
                        if content[1] == f"alias randomTaunt   \"exec classes/{selectedClass}_loadout\"":
                            lines = line1 + line2 + line3 + line4 + "\n" + line5 + "\n" + line6
                        else:
                            lines = line1 + line2 + line3 + line4 + "\n\n" + line5 + "\n" + line6
                    except:
                        lines = line1 + line2 + line3 + line4 + "\n\n" + line5 + "\n" + line6
                    content.reverse()
                    content = "\n".join(content)
                else:
                    line1 = f"bind {selectedKey}   \"randomTaunt\""
                    line2 = f"bind {selectedKey2}   \"randomMessage\""
                    line3 = f"alias randomTaunt   \"exec classes/{selectedClass}_loadout\""
                    line4 = f"alias randomMessage   \"exec classes/messages\""
                    if content[6] == f"alias randomTauntMessage   \"exec classes/{selectedClass}_loadout; exec classes/messages\"":
                        line5 = content[7]
                        line6 = content[6]
                    else:
                        line5 = ""
                        line6 = ""

                    for i in range(4):
                        content.pop(0)
                    try:
                        if content[2] == f"alias randomTauntMessage   \"exec classes/{selectedClass}_loadout; exec classes/messages\"" and not content[6] == line3:
                            for i in range(4):
                                content.pop(0)
                            lines = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n\n" + line5 + "\n" + line6
                        elif content[6] == line3 and content[2] == f"alias randomTauntMessage   \"exec classes/{selectedClass}_loadout; exec classes/messages\"":
                            for i in range(9):
                                content.pop(0)
                            lines = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n\n" + line5 + "\n" + line6
                        elif content[3] == line3:
                            for i in range(6):
                                content.pop(0)
                            lines = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + line5 + line6
                        else:
                            lines = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + line5 + line6
                    except:
                        lines = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + line5 + line6
                    content.reverse()
                    content = "\n".join(content)
            with open(f"{fileLoc}/overrides/{selectedClass.lower()}.cfg", "w+") as f2:
                f2.write(content + "\n" + lines)

            if not os.path.exists(f"{fileLoc}/taunts/"):
                with open(f"{fileLoc}/overrides/autoexec.cfg", "a+") as f:
                    f.write("\nexec randomBind\n")
        else:
            with open(f"{fileLoc}/{selectedClass.lower()}.cfg", "r+") as f:
                f.seek(0, 0)
                content = f.read()
                content += "\n\n\n\n\n\n"
                content = content.split("\n")
                content.reverse()

                if values["-checkbox-"]:
                    if content[3] == f"alias randomTaunt   \"exec classes/{selectedClass}_loadout\"":
                        line1 = content[5]
                        line2 = content[4]
                        line3 = content[3]
                        line4 = content[2]
                    else:
                        line1 = ""
                        line2 = ""
                        line3 = ""
                        line4 = ""
                    line5 = f"bind {selectedKey}   \"randomTauntMessage\""
                    line6 = f"alias randomTauntMessage   \"exec classes/{selectedClass}_loadout; exec classes/messages\""
                    for i in range(6):
                        content.pop(0)
                    if content[0] == line6:
                        for i in range(3):
                            content.pop(0)
                    try:
                        if content[1] == f"alias randomTaunt   \"exec classes/{selectedClass}_loadout\"":
                            lines = line1 + line2 + line3 + line4 + "\n" + line5 + "\n" + line6
                        else:
                            lines = line1 + line2 + line3 + line4 + "\n\n" + line5 + "\n" + line6
                    except:
                        lines = line1 + line2 + line3 + line4 + "\n\n" + line5 + "\n" + line6
                    content.reverse()
                    content = "\n".join(content)
                else:
                    line1 = f"bind {selectedKey}   \"randomTaunt\""
                    line2 = f"bind {selectedKey2}   \"randomMessage\""
                    line3 = f"alias randomTaunt   \"exec classes/{selectedClass}_loadout\""
                    line4 = f"alias randomMessage   \"exec classes/messages\""
                    if content[
                        6] == f"alias randomTauntMessage   \"exec classes/{selectedClass}_loadout; exec classes/messages\"":
                        line5 = content[7]
                        line6 = content[6]
                    else:
                        line5 = ""
                        line6 = ""

                    for i in range(4):
                        content.pop(0)
                    try:
                        if content[
                            2] == f"alias randomTauntMessage   \"exec classes/{selectedClass}_loadout; exec classes/messages\"" and not \
                        content[6] == line3:
                            for i in range(4):
                                content.pop(0)
                            lines = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n\n" + line5 + "\n" + line6
                        elif content[6] == line3 and content[
                            2] == f"alias randomTauntMessage   \"exec classes/{selectedClass}_loadout; exec classes/messages\"":
                            for i in range(9):
                                content.pop(0)
                            lines = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n\n" + line5 + "\n" + line6
                        elif content[3] == line3:
                            for i in range(6):
                                content.pop(0)
                            lines = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + line5 + line6
                        else:
                            lines = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + line5 + line6
                    except:
                        lines = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + line5 + line6
                    content.reverse()
                    content = "\n".join(content)
            with open(f"{fileLoc}/{selectedClass.lower()}.cfg", "w+") as f2:
                f2.write(content + "\n" + lines)

            if not os.path.exists(f"{fileLoc}/taunts/"):
                with open(f"{fileLoc}/autoexec.cfg", "a+") as f:
                    f.write("\nexec randomBind\n")

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
        try:
            with open(f"{fileLoc}/classes/UsedClasses.cfg", "x+") as f:
                f.seek(0)
                f.write(f"{selectedClass}\n")
            with open(f"{fileLoc}/randomBind.cfg", "x+") as f:
                f.seek(0)
                f.write('''\n\n\n\n\n\n\n\n\nexec classes/messages
\n\n\n\n\n\n\n\n\n\nalias "message_result"  "message_1"
\n\n\n\n\n\n\n\n\n\nalias "message_cycle"   "message_rng_1"
\n\n\nalias "message_time"    "message_cycle"

bind  w       +mF
bind  s       +mB
bind  a       +mL
bind  d       +mR

alias +mF     "-back;      +forward;   alias check_F +forward;   all_classes"
alias +mB     "-forward;   +back;      alias check_B +back;      message_time"
alias +mL     "-moveright; +moveleft;  alias check_L +moveleft;  all_classes"
alias +mR     "-moveleft;  +moveright; alias check_R +moveright; message_time"
alias -mF     "-forward;   check_B;    alias check_F none;       message_time"
alias -mB     "-back;      check_F;    alias check_B none;       all_classes"
alias -mL     "-moveleft;  check_R;    alias check_L none;       message_time"
alias -mR     "-moveright; check_L;    alias check_R none;       all_classes"
alias check_F none
alias check_B none
alias check_L none
alias check_R none
alias none    ""
echo "Taunt Generator Loaded"''')
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
            with open(f"{fileLoc}/randomBind.cfg", "w+") as f:
                f.write(content)

        except FileExistsError:
            with open(f"{fileLoc}/classes/UsedClasses.cfg", "r+") as f:
                f.seek(0)
                classesUsed = f.read()
                classesUsed = classesUsed.split("\n")
            if selectedClass not in classesUsed:
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
                for i in range(len(classesUsed)-1):
                    classesUsed[i] += "_cycle"
                contentRB[30] = f'alias \"all_classes\"     \"{selectedClass}_cycle; {"; ".join(classesUsed)}\"\n'
                contentRB = "\n".join(contentRB)
                with open(f"{fileLoc}/randomBind.cfg", "w+") as f:
                    f.write(contentRB)

        sG.Popup("All Done! Restart the app to go again!", title="Finished", font=fontTFbase)
        break

window.close()
