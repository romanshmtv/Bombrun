import re
import random
import math
import sys


def is_web():
    return "__BRYTHON__" in globals()

def write(message, end=' '):
    if is_web():
        from browser import document
        console = document.getElementById('console')
        p = document.createElement('p')
        p.textContent = '> ' + message
        console.appendChild(p)
        console.scrollTop = console.scrollHeight
    else:
        print(message, end = end)


async def read():
    if is_web():
        from browser import document, aio
        inp = document.getElementById('input')
        while True:
            event = await aio.event(inp, 'keydown')
            if event.key == 'Enter':
                tmp = event.target.value
                event.target.value = ''
                print(tmp)
                return tmp
    else:
        return input()


def run(function):
    if is_web():
        from browser import aio
        aio.run(function)
    else:
        import asyncio
        asyncio.run(function)

async def instr():
    write("YOU HAVE THE OPTION OF MAKING FOUR PASSES OVER THE TARGET,\n")
    write("WITH THE ABILITY TO DROP A BOMB ONCE DURING EACH OF\n")
    write("THESE PASSES.  ALTITUDE CHANGES MAY BE MADE THROUGH THE\n")
    write( "'CLIMB/DIVE' COMMAND BY write(ING 'CLIMB' OR 'DIVE',FOL-\n")
    write("LOWED BY A COMMA AND THE DESIRED ANGLE (IN DEGREES). NEW\n")
    write("VELOCITIES (RANGING FROM 300 TO 900 FEET PER SECOND) MAY\n")
    write("BE INPUT AFTER THE 'AIRSPEED' QUESTION MARK.  'CLIMB/DIVE'\n")
    write("ANGLES, VARYING FROM 0 TO 15 DEGREES, WILL ADD AS SPEC-\n")
    write("IFIED BY 'CLIMB' OR'DIVE' COMMANDS TO YIELD A NET INCLIN-\n")
    write( "ATION/DECLINATION ANGLE BETWEEN 0 TO 60 DEGREES, CLIMBING\n")
    write( "OR DIVING.  A MINIMUM ALTITUDE OF 100 FEET MUST ALSO BE\n")
    write("MAINTAINED.  WILLFULLY EXCEEDING ANY OF THE MAX./MIN. SPECS\n")
    write("WILL RESULT IN THE CRASH OF YOUR BOMBER. ALSO , A BOMB\n")
    write("COMMAND OF 'DROP' DURING A DIVE WILL GIVE YOUR BOMB AN IN-\n")
    write("ITIAL DOWNWARD VELOCITY, SHORTENING THE DROP TIME, AS A\n")
    write("'CLIMB' COMMAND WILL LENGTHEN THIS TIME.  THE BOMB WILL BE\n")
    write("LAUNCHED IMMEDIATELY FOLLOWING THE MOST RECENT 'STATS' READ-\n")
    write( "OUT UPON 'DROP' COMMAND, AND WILL BE HELD FOR FURTHER\n")
    write("POSITIONING INFORMATION UPON THE COMMAND 'STAND BY'.  THE\n")
    write("TARGET IS 1 FOOT IN DIAMETER.  GOOD LUCK\n")

p = ""
z1 = 1000
z2 = 1000
z3 = 1000
z4 = 1000
v = 0
v1 = 0
R = 0
rStr = ""
w1 = 0
x2 = 0
w3 = 0
w4 = 0
t = 0
a1 = 0
a = 0
y = 0
aStr = ""
c = ""
x = 4500
w1 = 0
w2 = 0
w3 = 0
w4 = 0
x5 = random.random() * 600
t3 = 0
b = 0
e = 0

async def goto410():
    global v, v1
    while v < 300 or v > 900:
        v1 = random.random()
        v = v1 * 1000
    return v

async def goto440():
    global y, y1
    while y < 100:
        y1 = random.random()
        y = y1 * 500
    return y

async def default():
    global c, w1, a1, w3, w4, aStr, c, p, z1, z2, z3, z4, t, a
    w1 = 0
    w3 = 0
    w4 = 0
    a1 = 0
    z1 = 1000
    z2 = 1000
    z3 = 1000
    z4 = 1000
    t = 0
    a = 0


async def goto540():
    global c, p ,aStr
    if R >= 1:
        await default()
    else:
        c = ""
        p = ""
        aStr = ""
    write("\nBOMB COMMAND\n")
    c = await read()
    while (c != "STAND") and (c != "DROP"):
        c = await read()

    if c == "STAND":
        await goto640()
    if c == "DROP":
        await goto1680()

async def goto1680():
    global t3, v, y, x, R
    write("BOMB DROPPED.\n")
    t3 = (math.sqrt((v * math.sin(b)) ** 2 + 64.4 * y) + v * math.sin(b))/32.2
    write("TIME TO EXPLOSION... ")
    write(str(t3))
    write(" SECONDS\n")
    x = x - v*math.cos(b) * t3
    x = int(x*100)/100
    write("\n")
    if x < -1500:
        write("THE BOMB LANDED ")
        write(str(-x))
        write(" FEET BEYOND THE TARGETS CENTER.\n")
        await goto1810()
    if x >1500:
        write("THE BOMB LANDED ")
        write(str(x))
        write(" FEET IN FRONT THE TARGETS CENTER.\n")
        await goto1810()
    if x > -1500 and x <1500:
        R+=1
        write("CONGRATULATIONS, YOU SCORED A PERFECT HIT.\n")
    await goto2030()


async def play_again():
    global aStr, R
    write("WOULD YOU LIKE TO RELOAD AND PLAY AGAIN?\n")
    aStr = ""
    aStr = await read()
    while aStr != "YES" and aStr != "NO":
        write("YOU MUST BE A LOUSY SPELLER. REPLY YES OR NO.\n")
        aStr = await read()
    if aStr == "NO":
        await goto2590()
    if aStr == "YES":
        await goto290()

async def goto2030():
    if rStr == "NO":
        await goto2590()
    await play_again()

async def goto1810():
    global R
    if R == 1 or R == 2 or R == 3 or R == 4:
        await goto1930()




async def goto640():
    write("STANDING BY\n")
    await goto700()

async def goto700():
    global p
    write("MAINTAIN PRESENT RESULTANT ANGLE\n")
    p = await read()
    if p == "YES":
        await goto1130()
    if p == "NO":
        await goto770()

async def goto1130():
    global w4, v
    write("AIRSPEED\n")
    v = int(await read())
    while v > 900:
        write("YOUR BOMBER ISNT CAPABLE OF ATTAINING THAT VELOCITY\n")
        write("INPUT AN AIRSPEED LESS THAN 900 FEET PER SECOND\n")
        v = int(await read())
    while v < 300:
        w4 += 1
        if w4 == 2:
            await goto2250()
            break
        v = int(await read())
    await goto1290()

async def goto1290():
    global v, y, x, a, t, b, e
    w5 = 0
    t += 1
    b = a * 3.14/180
    y += v * math.sin(b)
    if y > 100:
        x -= v*math.cos(b)
        e = x/(v*math.cos(b))
        write("\n***STATS***")
        await goto1430()
        if x <= 0:
            await goto2350()
    else:
        w5 += 1
    if w5 == 2:
        play_again()
    write("IF YOUR ALTITUTE ISNT INCREASED IMMEDIATELY TO A MIN-\n")
    write("IMUM OF 100 FEET, A CRASH IS IMMINENT.\n")
    await goto670()

async def goto670():
    global a
    global t
    a -= a1
    t -= 1
    await goto770()

async def goto770():
    global a, a1, aStr
    global w1
    while (aStr != "CLIMB" and aStr != "DIVE"):
        write("CLIMB/DIVE COMMAND\n")
        aStr = await read()
    write("INPUT DEGREES.\n")
    a1 = int(await read())
    write("\n")
    if a1 < 0:
        write("ANGLE INPUT MUST BE POSITIVE. IF NECESSARY, CHANGE THE\n")
        write("'DIVE' COMMAND TO 'CLIMB', OR VICE VERSA.\n")
        aStr = ""
        await goto770()
    if a1 > 15:
        w1 += 1
        if w1 == 2:
            play_again()
        write("YOUR BOMBER CANNOT TOLERATE THE STRESS CAUSED BY ANGLE\n")
        write("INPUTS EXCEEDING 15 DEGREES. RECONSIDER YOUR VOICE.\n")
        aStr = ""
        await goto770()
    await goto930()

async def goto930():
    global a, aStr, w2, w3, a1
    write(aStr == "CLIMB")
    if aStr == "CLIMB":
        a += a1
    a1 = -a1
    if a < -60:
        w2 += 1
        if w2 == 2:
            play_again()
        write("YOUR PRESENT 'DIVE' COMMAND WILL EXCEED THE MAXIMUM RE-\n")
        write("SULTANT DIVE ANGLE OF 60 DEGREES, CAUSING AN IPREVERSIBLE\n")
        write("NOSEDIVE. RECONSIDER YOUR CHOICE.")
        await goto670()
    if a > 60:
        w3 += 1
        if w3 == 2:
            play_again()
        write("YOUR PRESENT 'CLIMB' COMMAND WILL EXCEED THE MAXIMUM RE-\n")
        write("SULTANT CLIMB ANGLE OF 60 DEGREES, CAUSING YOUR\n")
        write(" ENGINES TO FAIL AND YOUR PLANE TO CRASH. RECONSIDER YOUR\n")
        write("CHOICE\n")
        await goto670()
    await goto1130()




async def goto2350():
    write("\n SAY, YOU NO LONGER THREATEN ITS EXISTANCE.\n")
    if R == 2:
        Q = "THIRD\n"
    if R == 3:
        Q = "FOURTH AND FINAL\n"
    if R == 4:
        await goto1930()

async def goto2340():
    global R
    write("YOUR BOMBER JUST PASSED UP THE TARGET, AND NEEDLESS TO\n")
    write("SAY, YOU NO LONGER THREATEN ITS EXISTANCE.")
    if R == 1:
        write("FIRST GONE\n")
        await play_again()
    if R == 2:
        write("SECOND GONE\n")
    if R == 3:
        write("THIRD GONE\n")
    if R == 4:
        write("FOURTH AND FINAL\n YOU WIN.")
        exit()

async def goto1930():
    global x5, rStr, aStr, R
    write("\n")
    if R > 0:
        await goto2340()
    if x5 > 300:
        write("DURING YOUR ")
        write(str(R))
        write(" -PASS BUMBRUN, YOU FAILED TO EVEN\n")
        write("THREATEN THE TARGET WITH A HIT. BETTER LUCK NEXT TIME.\n")
    else:
        write("DURING YOUR ")
        write(str(R))
        write(" -PASS BUMBRUN, YOU FAILED TO EVEN\n")
        write("WITHIN ")
        write(str(x5))
        write(" FEET OF TARGET.\n")
    if rStr == "NO":
        await goto2590()
    await play_again()
    
    
async def goto290():
    await goto410()
    await goto440()
    await goto1430()
    
    
    


async def goto2590():
    write("LOOK OVER THE PHYSICS LAWS GOVERNING FALLING BODIES,\n")
    write(" ADN RETURN TO PLAY AGAIN SOON.")
    sys.exit()



async def goto2250():
    global h
    write("\n THE VELOCITY OF YOUR BOMBER FAILED WHILE CLIMBING THE\n")
    write("STEEP ANGLE INPUT DURING YOUR ANGLE COMMAND OPPORTUNITY\n")
    h = 1

async def goto1430():
    global x, v, e, t, a1, aStr, a, c, p
    v
    e = x/v
    write("\n")
    if t!= 1:
        write("\t\t ELAPSED TIME...")
        write("SECONDS\n")
    write("\t\t ELAPSED TIME... 1 SECOND\n")
    if a1 != 0:
        if aStr == "CLIMB":
            write("\t\t PRESENT ANGLE COMMAND...")
            write(str(a1))
            write("DEGREES\n")
        write("\t\t PRESENT ANGLE COMMAND...")
        write((-a1))
        write("DEGREES\n")
    write("\t\t PRESENT ANGLE COMMAND... 0 DEGREE\n")
    if a < 0:
        write("\t\t RESULTANT ANGLE...")
        write(str(-a1))
        write("DEGREES DIVING\n")
    if a > 0:
        write("\t\t RESULTANT ANGLE...")
        write(str(a))
        write("DEGREES CLIMBING\n")
    write("\t\t PRESENT VELOCITY...")
    write(str(v))
    write("FEET PER SECOND\n")
    write("\t\tALTITUDE... ")
    write(str(y))
    write("FEET\n")
    write("\t\t DISTANCE FROM SITE... ")
    write(str(x))
    write("FEET\n")
    write("\t\tESTIMATED TIME OF ARRIVAL... ")
    write(str(e))
    write("SECONDS\n\n")
    aStr = ""
    c = ""
    p = ""
    await goto540()
    return e




async def game():
    global v, x5, y, x, t, a
    write("\t\t\tBOMBRUN\n")
    write("\t\t   CREATIVE COMPUTING\n")
    write("\t\t  MORRISTOWN, NEW JERSEY\n\n")
    write("THIS PROGRAM SIMULATES A BOMBING RUN. DO YOU NEED INSTRUCTIONS?\n")
    x5 = 3000
    I = ''
    while (I != 'Y') and (I != 'N'):
        I = await read()
        if I == 'Y':
            instr()
        if (I != 'Y') and (I != 'N'):
            write("ILLOGICAL RESPONSE. REPLY 'Y' OR 'N'\n")
    await goto410()
    
    await goto440()
    write("\n\n")
    write("\t\t\t**INITIAL**\n")
    write("\t\t\t***STATS***\n")
    write("\n")
    await goto1430()
    

run(game())