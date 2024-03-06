#!/usr/bin/env python
#
# ******************************************************************************
#
# EXPORT SYMBOLS FROM VASM
#
# Written by Mark Moxon
#
# This script extracts symbol values from the vasm output so they can be
# included in the !RunImage source, and it creates a GameCode.inf file for
# Arthur that contains the correct file size, load and execution addresses.
#
# ******************************************************************************

import re
import math
import shutil


def convert(input_file, output_file, inf_file, run_file):

    export_section_reached = False
    exec_address = ""
    file_size = ""

    for line in input_file:

        if "Symbols by value:" in line:
            export_section_reached = True

        # Export variables
        if export_section_reached:
            exported_variable = re.search(r"^([0-9A-F]{8}) (\w+)$", line)
            if exported_variable:
                export = ".set " + exported_variable.group(2) + ", 0x" + exported_variable.group(1) + "\n"
                output_file.write(export)
                if exported_variable.group(2) == 'Entry':
                    exec_address = exported_variable.group(1)[-6:]
                if exported_variable.group(2) == 'endCode':
                    end_code = exported_variable.group(1)
                    file_size = hex(int(end_code, 16) - 0x8000).replace("0x", "00000000")
                if exported_variable.group(2) == 'buffer':
                    buffer = int(exported_variable.group(1), 16)
                if exported_variable.group(2) == 'BUFFER_SIZE':
                    buffer_size = int(exported_variable.group(1), 16)

    inf = "$.Gamecode        008000 " + exec_address[-6:].upper() + " " + file_size[-6:].upper()
    inf_file.write(inf)

    shutil.copy("5-compiled-game-discs/arthur/Game/GameCode", "5-compiled-game-discs/arthur/Game/GameCode,8000-" + exec_address[-4:].upper())

    wimp_slot = math.ceil((buffer - 0x8000 - buffer_size) / 1024)
    if (wimp_slot // 8) != (wimp_slot / 8):
        wimp_slot = ((wimp_slot // 8) + 1) * 8
    run_file.write("| !Run file for !BigLander (see lander.bbcelite.com)\n")
    run_file.write("WimpSlot -min {0}K -max {0}K\n".format(wimp_slot))
    run_file.write("Run <Obey$Dir>.!RunImage\n")


print("Extracting exported variables from 1-source-files/Lander.arm")

compile_file = open("3-assembled-output/compile.txt", "r")
vasm_file = open("3-assembled-output/exports.arm", "w")
inf_file = open("3-assembled-output/GameCode.inf", "w")
run_file = open("3-assembled-output/!Run,feb", "w")
convert(compile_file, vasm_file, inf_file, run_file)
inf_file.close()
compile_file.close()
vasm_file.close()

print("Variables extracted")
