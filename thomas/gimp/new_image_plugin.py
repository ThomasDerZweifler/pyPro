#!/usr/bin/env python
# -*- coding: utf-8 -*-

import py_compile
py_compile.compile('./new_image_plugin.py')

from gimpfu import *

# https://www.gimp.org/docs/python/index.html#INTRODUCTION

# GIMP procedural database (PDB) Doku:
# http://oldhome.schmorp.de/marc/pdb/index.html

# https://wiki.python.org/moin/PythonMagick

# plugins location on Max OSX:
# /Applications/GIMP-2.10.app/Contents/Resources/lib/gimp/2.0/plug-ins

def erstelle_neues_image(image, ebene):
    width  = 600
    height = 400

    # Ein neues Image erzeugen.
    image = pdb.gimp_image_new(width, height, RGB)
    # Für das Image mindestens eine Ebene erzeugen und die Ebene hinzufügen.
    ebene = pdb.gimp_layer_new(
            image, width, height, RGB, "ebenen-name", 100, NORMAL_MODE)
    pdb.gimp_image_insert_layer(image, ebene, None, 1)
    # Eine Hintergrundfarbe auswählen und das Image damit füllen.
    pdb.gimp_context_set_background((255,138,0))
    pdb.gimp_drawable_fill(ebene, BACKGROUND_FILL)
    # Das neu erzeugte Image anzeigen.
    pdb.gimp_display_new(image)


register(
    "erstelle_neues_image",                       # Plugin Name
    "Neues Image erstellen",                      # Kurzbeschreibung
    "Ein neues Image erstellen",                  # Längere Beschreibung
    "Mele Melewo",                                # Plugin Autor
    "MIT-Lizenz",                                 # Angaben zur Lizenz
    "2017",                                       # Jahr der Veröffentlichung
    "<Image>/Filters/Neues Image",         # Position im Menü mit Label
    "*",                                          # Akzeptierte Image-Typen
    [],                                           # Input Parameter
    [],                                           # Output Resultate
    erstelle_neues_image                          # Name der Funktion
    )

main()