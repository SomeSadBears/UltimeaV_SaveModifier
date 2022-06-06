import struct

# function that updates the file using custom
# stat values for a specific character
# pm_of = party member offset
# st_of = stat offset
# data_size = either 1 or 2 (for byte or word)
# val = custom value to set char stat
def updateFile(pm_of, st_of, data_size, val):

    # sets the cursor to a postion equal to:
    # start of file + character offset
    file.seek(pm_of,0) #party member offset

    # sets cursor to a postion equal to:
    # character offset + status offset
    file.seek(st_of, 1) #stat offset

    #generates a bynary value based on the value
    # the user entered, it is little endian
    # size is determined by the stat chosen
    # all stats are one byte, except for HP, MAXHP and EXP, which are words
    bVal = val.to_bytes(data_size, byteorder = 'little', signed = False)

    # writes bynary value to the appropriate location in the file
    file.write(bVal)

    
# function to ensure user input is in proper range    
def getVal(minVal, maxVal):
    print("Value must be in range: ", minVal, " ", maxVal)
    val = input("Enter value: ")
    val = int(val)
    
    while (val > maxVal or val < minVal):
        print("Value must be in range: ", minVal, " ", maxVal)
        val = input("Enter value: ")
        val = int(val)
    
    return val

# function for selecting which character stat user wants to update
def statMenu(pm_of):
    print("Enter stat name you want to modify: STR, INT, DEX, HP,")
    st_sel = input("MAXHP, EXP: ")

    # sets user input to lowercase for easier matching
    st_sel = st_sel.lower()

    if st_sel == "str":
        # gets user to set character stat to custom value
        val = getVal(0, 99)
        # calls updateFile function to update the file with
        # desired values for desired character
        updateFile(pm_of, STR, 1, val)
        
    elif st_sel == "int":
        val = getVal(0, 99)
        updateFile(pm_of, INT, 1, val)

    elif st_sel == "dex":
        val = getVal(0, 99)
        updateFile(pm_of, DEX, 1, val)

    elif st_sel == "hp":
        val = getVal(0, 999)
        updateFile(pm_of, HP, 2, val)

    elif st_sel == "maxhp":
        val = getVal(0, 999)
        updateFile(pm_of, MAX_HP, 2, val)

    elif st_sel == "exp":
        val = getVal(0, 9999)
        updateFile(pm_of, EXP, 2, val)
    
    else:
        print("Invalid value, try again")
        statMenu(pm_of)

# basic functionality that sets all character stats
# to the highest permited value
def maxAll():
    # player data is located at offset 2
    # bytes 0 and 1 are blank for some reason
    of = 2

    # loops through all characters by incrementing
    # current offset value by 32 bits
    # since character data are separated by exactly 32 bits
    while of <= 482:
        # sets cursor to current character offset location
        file.seek(of, 0)
        # sets curor to current character offset location + STR offset
        file.seek(STR, 1)
        # generates binary equivalent for dec 99, little endian, unsigned
        bVal = (99).to_bytes(1, byteorder = 'little', signed = False)
        # writes binary value to current cursor location
        file.write(bVal)

        # reset cursor location to current character offset location
        # then repeat the steps above for all stats
        file.seek(of, 0)
        file.seek(DEX, 1)
        bVal = (99).to_bytes(1, byteorder = 'little', signed = False)
        file.write(bVal)

        file.seek(of, 0)
        file.seek(INT, 1)
        bVal = (99).to_bytes(1, byteorder = 'little', signed = False)
        file.write(bVal)

        file.seek(of, 0)
        file.seek(HP, 1)
        bVal = (999).to_bytes(2, byteorder = 'little', signed = False)
        file.write(bVal)

        file.seek(of, 0)
        file.seek(MAX_HP, 1)
        bVal = (999).to_bytes(2, byteorder = 'little', signed = False)
        file.write(bVal)

        file.seek(of, 0)
        file.seek(EXP, 1)
        bVal = (9999).to_bytes(2, byteorder = 'little', signed = False)
        file.write(bVal)

        # character data sets are always exactly 32 bits apart
        # by incrementing the offset by 32 bits the program can
        # loop through all the characters
        of = of + 32

# sets the requisite items to the required values
def updateItems():

    # generate bynary equivalent of dec 99
    # to be used to set keys, skull keys, and gems
    bVal = (99).to_bytes(1, byteorder = 'little', signed = False)
    # set cursor to location where key data is found
    file.seek(keys,0)
    # write to location
    file.write(bVal)

    file.seek(s_keys,0)
    file.write(bVal)

    file.seek(gems,0)
    file.write(bVal)
    
    bVal = (1).to_bytes(1, byteorder = 'little', signed = False)
    file.seek(b_badge,0)
    file.write(bVal)

    bVal = (2).to_bytes(1, byteorder = 'little', signed = False)
    file.seek(m_carpet,0)
    file.write(bVal)    

    bVal = (10).to_bytes(1, byteorder = 'little', signed = False)
    file.seek(m_axe,0)
    file.write(bVal)

    bVal = (9999).to_bytes(2, byteorder = 'little', signed = False)
    file.seek(gold,0)
    file.write(bVal)

# global menu to select what the user wants to update
def charMenu():
    print("Enter the name of the character you want to modify")
    print("Enter Player for Player character")
    print("Enter list for list of character names")
    print("Enter MAXALL to cheat extra hard")
    print("Enter exit to exit")
    ch_sel = input("Enter Items to max keys, etc\n")

    ch_sel = ch_sel.lower()
    
    if ch_sel == "player":
        statMenu(Player)
        
    elif ch_sel == "shamino":
        statMenu(Shamino)

    elif ch_sel == "iolo":
        statMenu(Iolo)

    elif ch_sel == "mariah":
        statMenu(Mariah)

    elif ch_sel == "geoffrey":
        statMenu(Geoffrey)

    elif ch_sel == "jaana":
        statMenu(Jaana)

    elif ch_sel == "julia":
        statMenu(Julia)

    elif ch_sel == "dupre":
        statMenu(Dupre)

    elif ch_sel == "katrina":
        statMenu(Katrina)

    elif ch_sel == "sentri":
        statMenu(Sentri)

    elif ch_sel == "gwenno":
        statMenu(Gwenno)

    elif ch_sel == "johne":
        statMenu(Johne)

    elif ch_sel == "gorn":
        statMenu(Gorn)

    elif ch_sel == "maxwell":
        statMenu(Maxwell)

    elif ch_sel == "toshi":
        statMenu(Toshi)

    elif ch_sel == "saduj":
        statMenu(Saduj)

    elif ch_sel == "items":
        print("Maxing items")
        updateItems()

    elif ch_sel == "maxall":
        maxAll()

    elif ch_sel == "list":
        print("Shamino, Iolo, Mariah, Geoffrey, Jaana, Julia,")
        print("Dupre, Katrina, Sentri, Gwenno, Johne,")
        print("Gorn, Maxwell, Toshi, Saduj\n")

    elif ch_sel == "exit":
        exit()
    
    else:
        print("Invalid value entered")


# status offsets:
# (note: all status offsets are relative to
# the start of the character data)
STR = 12 #char_offset + 0x0C

DEX = 13 #char_offset + 0x0D

INT = 14 #char_offset + 0x0E

MP = 15 #char_offst + 0x0F

HP = 16 #word, char_offset + 0x10

MAX_HP = 18 #word, char_offset + 0x12

EXP = 20 #word, char_offset + 0x14

LV = 22 #byte, char_offset + 0x16

# character offsets:

Player = 2 #0x02

Shamino = 34 #0x22

Iolo = 66 #0x42

Mariah = 98 #0x62

Geoffrey = 130 #0x82

Jaana = 162 #0xA2

Julia = 194 #0xC2

Dupre = 226 #0xE2

Katrina = 258 #0x102

Sentri = 290 #0x122

Gwenno = 322 #0x142

Johne = 352 #0x162

Gorn = 386 #0x182

Maxwell = 418 #0x1A2

Toshi = 450 #0x1C2

Saduj = 482 #0x1E2

#item offsets

gold = 516 #0x204

keys = 518 #0x206

gems = 519 #0x207

s_keys = 523 #0x20B

b_badge = 536 #0x218

m_carpet = 522 #0x20A

m_axe = 576 #0x240


# main function
# SAVED.GAM must be in the same directory as this file
file = open("SAVED.GAM", 'rb+')

while(1):
    charMenu()

file.close()
