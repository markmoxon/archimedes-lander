# Fully documented source code for Lander on the Acorn Archimedes

<details>
<summary>Links to my other software archaeology repositories</summary>
<hr>

**Elite sources:** [BBC Micro (cassette)](https://github.com/markmoxon/elite-source-code-bbc-micro-cassette) | [BBC Micro (disc)](https://github.com/markmoxon/elite-source-code-bbc-micro-disc) | [Elite Demonstration Disc](https://github.com/markmoxon/elite-demo-source-code-bbc-micro) | [Acorn Electron](https://github.com/markmoxon/elite-source-code-acorn-electron) | [6502 Second Processor](https://github.com/markmoxon/elite-source-code-6502-second-processor) | [Commodore 64](https://github.com/markmoxon/elite-source-code-commodore-64) | [Apple II](https://github.com/markmoxon/elite-source-code-apple-ii) | [BBC Master](https://github.com/markmoxon/elite-source-code-bbc-master) | [NES](https://github.com/markmoxon/elite-source-code-nes)

**Elite hacks:** [Elite-A](https://github.com/markmoxon/elite-a-source-code-bbc-micro) | [Two-player Elite](https://github.com/markmoxon/elite-two-player-6502-second-processor) | [Teletext Elite](https://github.com/markmoxon/teletext-elite) | [Elite 3D](https://github.com/markmoxon/elite-3d) | [Elite Universe Editor](https://github.com/markmoxon/elite-universe-editor) | [Flicker-free Commodore 64 Elite](https://github.com/markmoxon/c64-elite-flicker-free) | [Elite over Econet](https://github.com/markmoxon/elite-over-econet) | [!EliteNet](https://github.com/markmoxon/elite-over-econet-acorn-archimedes)

**Elite Compendium:** [BBC Master](https://github.com/markmoxon/elite-compendium-bbc-master) | [BBC Micro](https://github.com/markmoxon/elite-compendium-bbc-micro) | [BBC Micro B+](https://github.com/markmoxon/elite-compendium-bbc-micro-b-plus) | [Acorn Electron](https://github.com/markmoxon/elite-compendium-acorn-electron)

**Other sources:** [Aviator (BBC Micro)](https://github.com/markmoxon/aviator-source-code-bbc-micro) | [Revs (BBC Micro)](https://github.com/markmoxon/revs-source-code-bbc-micro) | [The Sentinel (BBC Micro)](https://github.com/markmoxon/the-sentinel-source-code-bbc-micro) | [Lander (Acorn Archimedes)](https://github.com/markmoxon/lander-source-code-acorn-archimedes)

**Other repositories:** [Scripts for generating bbcelite.com](https://github.com/markmoxon/bbcelite-scripts) | [Static content for bbcelite.com](https://github.com/markmoxon/bbcelite-websites) | [Elite source code library](https://github.com/markmoxon/elite-source-code-library) | [Elite Universe Editor library](https://github.com/markmoxon/elite-universe-editor-library) | [Elite over Econet fileserver menu](https://github.com/markmoxon/elite-over-econet-fileserver-menu)

See [my profile](https://github.com/markmoxon) for more repositories to explore.
<hr>
</details>

![Screenshot of Lander on the Acorn Archimedes](https://lander.bbcelite.com/images/github/Lander.png)

This repository contains source code for David Braben's classic game Lander on the Acorn Archimedes, with every single line documented and (for the most part) explained. It has been reconstructed by hand from a disassembly of the original game binaries.

It is a companion to the [lander.bbcelite.com website](https://lander.bbcelite.com).

See the [introduction](#introduction) for more information.

## Contents

* [Introduction](#introduction)

* [Acknowledgements](#acknowledgements)

  * [A note on licences, copyright etc.](#user-content-a-note-on-licences-copyright-etc)

* [Browsing the source in an IDE](#browsing-the-source-in-an-ide)

* [Folder structure](#folder-structure)

* [Extending the landscape with BigLander](#extending-the-landscape-with-biglander)

* [Building Lander from the source](#building-lander-from-the-source)

  * [Requirements](#requirements)
  * [Windows](#windows)
  * [Mac and Linux](#mac-and-linux)
  * [Archimedes](#archimedes)
  * [Verifying the output](#verifying-the-output)
  * [Encryption in the RISC OS variant](#encryption-in-the-risc-os-variant)
  * [Log files](#log-files)

## Introduction

This repository contains source code for Lander on the Acorn Archimedes, with every single line documented and (for the most part) explained.

You can build the fully functioning game from this source. Two variants are currently supported: the Arthur variant, and the RISC OS 2 variant.

It is a companion to the [lander.bbcelite.com website](https://lander.bbcelite.com), which contains all the code from this repository, but laid out in a much more human-friendly fashion.

* If you want to browse the source and read about how Lander works under the hood, you will probably find [the website](https://lander.bbcelite.com) is a better place to start than this repository.

* If you would rather explore the source code in your favourite IDE, then the [annotated source](1-source-files/main-sources/Lander.arm) is what you're looking for. It contains the exact same content as the website, so you won't be missing out (the website is generated from the source files, so they are guaranteed to be identical). You might also like to read the section on [browsing the source in an IDE](#browsing-the-source-in-an-ide) for some tips.

* If you want to build Lander from the source on a modern computer, to produce a working game disc that can be loaded into a Acorn Archimedes or an emulator, then you want the section on [building Lander from the source](#building-lander-from-the-source). You can also build the source on an Archimedes, as described in the the [Archimedes](#archimedes) section.

My hope is that this repository will be useful for those who want to learn more about Lander and what makes it tick. It is provided on an educational and non-profit basis, with the aim of helping people appreciate the magic of David Braben's 32-bit masterpiece, and the first ever game for the ARM platform.

## Acknowledgements

Lander was written by David Braben and is copyright &copy; D.J.Braben 1987.

The code on this site has been reconstructed from a disassembly of the version released on the [application discs for Arthur and RISC OS](http://www.lewisgilbert.co.uk/archiology/osdiscs.html).

The commentary is copyright &copy; Mark Moxon. Any misunderstandings or mistakes in the documentation are entirely my fault.

### A note on licences, copyright etc.

This repository is _not_ provided with a licence, and there is intentionally no `LICENSE` file provided.

According to [GitHub's licensing documentation](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/licensing-a-repository), this means that "the default copyright laws apply, meaning that you retain all rights to your source code and no one may reproduce, distribute, or create derivative works from your work".

The reason for this is that my commentary is intertwined with the original game code for Lander, and the original game is copyright. The whole site is therefore covered by default copyright law, to ensure that this copyright is respected.

Under GitHub's rules, you have the right to read and fork this repository... but that's it. No other use is permitted, I'm afraid.

My hope is that the educational and non-profit intentions of this repository will enable it to stay hosted and available, but the original copyright holders do have the right to ask for it to be taken down, in which case I will comply without hesitation.  I do hope, though, that along with the various other disassemblies and commentaries of Acornsoft's games for the BBC Micro and Archimedes, it will remain viable.

## Browsing the source in an IDE

If you want to browse the source in an IDE, you might find the following useful.

* The most interesting files are in the [main-sources](1-source-files/main-sources) folder:

  * The main game's source code is in the [Lander.arm](1-source-files/main-sources/Lander.arm) file - this is the motherlode and probably contains all the stuff you're interested in. It produces a file called `GameCode` that contains the entire game.

  * The RISC OS application bundles up the game into a `!RunImage`, whose source is in the [RunImage.arm](1-source-files/main-sources/RunImage.arm) file. In the version on the RISC OS application disc the `!RunImage` binary is encrypted, but in this version the game binary is simply wrapped in a relocation routine (though encryption may be added later).

* It's probably worth skimming through the [notes on terminology and notations](https://lander.bbcelite.com/terminology/) on the accompanying website, as this explains a number of terms used in the commentary, without which it might be a bit tricky to follow at times.

* The entry point for the [main game code](1-source-files/main-sources/lander-source.asm) is routine `Entry`, which you can find by searching for `Name: Entry`.

* The source code is designed to be read at an 80-column width and with a monospaced font, just like in the good old days.

I hope you enjoy exploring the inner workings of Lander as much as I have.

## Folder structure

There are five main folders in this repository, which reflect the order of the build process.

* [1-source-files](1-source-files) contains all the different source files, such as the main assembler source files, BASIC loaders, RISC OS application files and so on.

* [2-build-files](2-build-files) contains build-related scripts, such as the crc32 verification scripts and vasm converter script.

* [3-assembled-output](3-assembled-output) contains the output from the assembly process, when the source files are assembled and the results processed by the build files.

* [4-reference-binaries](4-reference-binaries) contains the correct binaries for each release, so we can verify that our assembled output matches the reference.

* [5-compiled-game-discs](5-compiled-game-discs) contains the final output of the build process: folders that contains the compiled game for each variant and which can be run on real hardware or in an emulator, plus zips of those folders for easier deployment. It also contains version of the source code that can be built on an Archimedes; see the [Archimedes](#archimedes) section for information on the latter. The Arthur variant contains the GameCode binary in two formats: as a pair of files (GameCode and GameCode.inf) that is suitable for programs that support inf files, or as a single file (GameCode,8000-A614) that will work with HostFS. Both options contain the load and execution address of the file, and you should choose the one that works for you when copying the game to your emulator or Archimedes.

## Extending the landscape with BigLander

This repository also includes a version of Lander with a much bigger landscape: 64 by 64 tiles, to be precise (as compared to the original 12 by 10 tiles). This version also runs on all versions of RISC OS (the original only works on Arthur and RISC OS 2). The big-landscape code is in a separate branch called `big-landscape`, and apart from the code differences for the landscape size and later versions of RISC OS, this branch is identical to the main branch and the same build process applies.

The landscape size is configurable. The default is 64 by 64 tiles (which equates to TILES_X = 65 and TILES_Z = 65), but you can set your own values by passing x and z parameters to the build. For example, building BigLander like this on Mac or Linux:

```
make x=122 z=122
```

or this on Windows:

```
make.bat x=122 z=122
```

would build BigLander with a landscape size of 121 x 121 tiles (i.e. TILES_X = 122 and TILES_Z = 122). The number of tiles is given in the !Help file of the generated application, along with the build date.

The annotated source files in the `big-landscape` branch contain both the original Lander code and all of the modifications for the bigger landscape, so you can look through the source to see exactly what's changed. Any code that I've removed from the original version is commented out in the source files, so when they are assembled they produce the big-landscape binaries, while still containing details of all the modifications. You can find all the diffs by searching the sources for `Mod:`.

BigLander should work on all versions of RISC OS, but to get it working on a Raspberry Pi, you may need to create a text file in the !Boot.Loader folder called CMDLINE/TXT, containing the word `disable_mode_changes` (reboot after you create this). Make sure you have !ADFFS loaded, and then BigLander should run. You can see a video guide to this process [on YouTube](https://www.youtube.com/watch?v=HpQk1l7Rvu0).

If BigLander on your Pi is blurry, you can change the GPU upscaler method. Edit the CONFIG/TXT in !Boot.Loader and add `scaling_kernel=8` on a new line before rebooting. This will probably make your desktop a bit messy, but BigLander should now look pretty great (and you can remove the line to go back to blurry BigLander and a crisp desktop).

For more information on BigLander, see the [accompanying website](https://lander.bbcelite.com/deep_dives/hacking_the_landscape.html).

## Building Lander from the source

Builds are supported for Windows and Mac/Linux systems. In all cases the build process is defined in the `Makefile` provided.

The build process also creates a version of the source that can be built on [Archimedes](#archimedes) machines.

### Requirements

You will need the following to build Lander from the source:

* vasm, which can be downloaded from the [vasm homepage](http://sun.hasenbraten.de/vasm/).

* Python. The build process has only been tested on 3.x, but 2.7 might work.

* Mac and Linux users may need to install `make` if it isn't already present (for Windows users, `make.exe` is included in this repository).

Let's look at how to build Lander from the source.

### Windows

For Windows users, there is a batch file called `make.bat` that builds the project. Before this will work, you should edit the batch file and change the values of the `VASM` and `PYTHON` variables to point to the locations of your `vasmarm_std.exe` and `python.exe` executables (you need the `vasmarm_std` executable). You also need to change directory to the repository folder (i.e. the same folder as `make.bat`).

All being well, entering the following into a command window:

```
make.bat
```

will produce folders called `arthur` and `riscos` in the `5-compiled-game-discs` folder, which contain the Arthur and RISC OS variants of the game, which you can then load into an emulator, or into a real Acorn Archimedes using a device like a Gotek. It also produces a zip file for each variant, which can be found in the `zip` folder (note that these zips do not contain RISC OS filetype metadata; filetypes are included as filename suffixes, so they will work with HostFS).

### Mac and Linux

The build process uses a standard GNU `Makefile`, so you just need to install `make` if your system doesn't already have it. If vasm or Python are not on your path, then you can either fix this, or you can edit the `Makefile` and change the `VASM` and `PYTHON` variables in the first two lines to point to their locations (you need the `vasmarm_std` executable). You also need to change directory to the repository folder (i.e. the same folder as `Makefile`).

All being well, entering the following into a terminal window:

```
make
```

will produce folders called `arthur` and `riscos` in the `5-compiled-game-discs` folder, which contain the Arthur and RISC OS variants of the game, which you can then load into an emulator, or into a real Acorn Archimedes using a device like a Gotek. It also produces a zip file for each variant, which can be found in the `zip` folder (note that these zips do not contain RISC OS filetype metadata; filetypes are included as filename suffixes, so they will work with HostFS).

### Archimedes

The build process outlined above produces a file called `LanderSrc,fff` in the `5-compiled-game-discs` folder, or `BLanderSrc,fff` if you are building BigLander. These files contain versions of the game source that can be built on an Archimedes.

To build the source on an Archimedes, you first need to convert the BBC BASIC text file into tokenised BBC BASIC. If you have RISC OS 3, then you can use Edit to do this, as follows:

* Download the source as a BBC BASIC text file for [Lander](https://raw.githubusercontent.com/markmoxon/lander-source-code-acorn-archimedes/main/5-compiled-game-discs/LanderSrc%2Cfff) or [BigLander](https://raw.githubusercontent.com/markmoxon/lander-source-code-acorn-archimedes/big-landscape/5-compiled-game-discs/BLanderSrc%2Cfff).

* Copy the file to an Archimedes machine (if you aren't already downloading it in RISC OS).

* If you are using HostFS then the filetype should be set automatically, but if you need to set it manually, it should be a Text file.

* Load the text file into Edit. You should see the fully documented source code appear.

* Click Menu on Edit's icon bar icon, choose "BASIC options > Line number increment" and set the value to 1.

* Click Menu over Edit's window, choose "Misc > Set type" and set the value to BASIC.

* Save the file, which is now a BASIC program.

You now have the Lander source in BBC BASIC, which is how David Braben originally wrote it (though without quite so many comments).

To build the game from this source, simply run the file by double-clicking it. It will assemble the game and save the GameCode file into the current directory, so you may want to set the current directory before doing this. You may need to allocate more memory to the Next slot for the assembly to work: you need at least 832K to build Lander, and at least 904K to build BigLander.

You can play the game by simply double-clicking on the GameCode file. You can run Lander on Arthur, RISC OS 2 or up to RISC OS 3.11, and you can run BigLander on any version of RISC OS. You may need to allocate more memory to the Next slot for the game to run: you need at least 168K to run Lander, and at least 400K to run BigLander.

Note that the main source code in this repository is very close to being in BBC BASIC format, but it isn't exactly the same (which is why the BBC BASIC version is created by the build process rather than actually being the main source). This is because BBC BASIC has some limitations that make it a tricky companion for large commentaries like this. For example, the colon character separates multiple statements in BBC BASIC, but this also applies within comments, so any comments that contain colons will cause runtime errors when used in BASIC. The same applies with unmatched brackets and double-quotes, though these only generate warnings (though they do break the Text to BASIC conversion process). BBC BASIC also doesn't support comma-separated EQU arguments, which makes laying out tables like the object blueprints rather difficult.

As a result the main source code in this repository is an homage to BBC BASIC's assembly language format, but it is not 100% accurate. That's why the build includes a conversion script to convert the Lander.arm source file into a working BBC BASIC source. See the [convert-to-basic.py](2-build-files/convert-to-basic.py) script for details.

### Verifying the output

The build process prints out checksums of all the generated files, along with the checksums of the files from the original sources.

The Python script `crc32.py` in the `2-build-files` folder does the actual verification, and shows the checksums and file sizes of both sets of files, alongside each other, and with a Match column that flags any discrepancies.

The binaries in the `4-reference-binaries` folder are those extracted from the released version of the game, while those in the `3-assembled-output` folder are produced by the build process. For example, if you don't make any changes to the code and build the project with `make`, then this is the output of the verification process:

```
[--originals--]  [---output----]
Checksum   Size  Checksum   Size  Match  Filename
-----------------------------------------------------------
9985364c  39488  9985364c  39488   Yes   !RunImage.bin
aa7f1052  39440  aa7f1052  39440   Yes   GameCode.bin
```

All the compiled binaries match the originals, so we know we are producing the same final game for both the Arthur and RISC OS variants.

### Encryption in the RISC OS variant

The !RunImage file in the RISC OS variant of Lander is encrypted. The [2-build-files/decrypt](2-build-files/decrypt) folder contains a script that decrypts the binary.

It turns out that the decrypted !RunImage is identical to the Arthur variant's GameCode binary, so the RISC OS variant is the exact same game, just encrypted. To prove this, I've written a Python script called [lander-decrypt.py](2-build-files/decrypt/lander-decrypt.py) that decrypts the original !RunImage binary. This Python script is based on the original decryption routine, whose source is in [lander-decrypt.arm](2-build-files/decrypt/lander-decrypt.arm).</p>

The !RunImage produced by the build process doesn't include this encryption, and in its place there's a small routine that simply copies the game code to address &8000, without making any changes (you can see this in the main [RunImage.arm](1-source-files/main-sources/RunImage.arm) source).

### Log files

During compilation, details of every step are output in a file called `compile.txt` in the `3-assembled-output` folder. If you have problems, it might come in handy, and it's a great reference if you need to know the addresses of labels and variables for debugging (or just snooping around).

---

_Mark Moxon_
