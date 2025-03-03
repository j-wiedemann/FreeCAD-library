FreeCAD-library
===============

This repository contains a library of Parts to be used in FreeCAD. It is maintained by the community
of users of FreeCAD and is not part of the FreeCAD project, although it is made with the aim to be
used as a repository of parts by FreeCAD in the future.

Contributing to the library
---------------------------

If you are interested in contributing to this library, please ask for write access to this repository
on this FreeCAD forum thread: http://forum.freecadweb.org/viewtopic.php?f=19&t=4205

Each Part should be correctly named, and placed into subdirectories by family or type. They should also
be available in both .FcStd and .stp formats, and optionally in .stl format (because github lets you
visualize them). They should also be as simple as possible, and parametric
so users can easily change their dimensions. In the file properties of each .FcStd file, the author
should also be mentioned, and the license information if available.

License
-------

All Parts in this repository are licensed under CC-BY 3.0 http://creativecommons.org/licenses/by/3.0/
Each Part is copyrighted by and should be attributed to its respective author(s).
See commit details to find the authors of each Part.

If you are uploading parts to this repository, please make sure you are the author of the model,
or otherwise that you have right to share it here under the CC-BY 3.0 license, and make sure the author
is mentioned in the commit message.

Install
-------

The library is a simple container for FreeCAD (.fcstd) and STEP (.stp) files. You can download it
anywhere and import its files in your FreeCAD projects. Inside the library, there is also a FreeCAD
macro (PartsLibrary.FCMacro) that you can place in your FreeCAD macros folder. That macro creates 
a browser window inside FreeCAD, from which you can easily add the parts by double-clicking them.

Sharing your models
-------------------

The macro also allows gives a couple of other possibilities,such as adding new objects to it, and
sharing your objects with others. To be able to share, you will need the python-git package
installed on your computer, and an online git repository you have permission to write to. The 
easiest way to obtain that is using the "fork" button on top of this github page.

Once you have made your fork, you will get an URL from it, that you can use in the macro's
config dialog. After that, once you have saved your models to the library, you can push them to
your online git repository, and, if you wish, make a pull request on this page to see your
models integrated to the official library.
