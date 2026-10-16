import os
import subprocess
from solid2 import *


#if you want to cut by hands, you can use https://materlogic.com/en/dxf-viewer to mesure each segment of the dxf file (only work with dxf export)


file_format = ".dxf"
previs = False
openscad_path = "C:\Program Files\OpenSCAD\openscad.exe"

# All measurements are in mm
film_height = 51
film_length = 169
wall_thickness = 10
sheet_thickness = 3
lens_plate_hole_diameter = 40
bypass_hole_too_big = False
# Margins are on each side
margin_film = 5
tolerance_between_parts = 1
tolerance_fine = 0.25

#custom front standard size

#pre calculation
wall_thickness += wall_thickness
margin_film += margin_film
tolerance_between_parts += tolerance_between_parts
tolerance_fine += tolerance_fine
lens_plate_hole_diameter = lens_plate_hole_diameter/2

if lens_plate_hole_diameter*2 > film_height + margin_film + wall_thickness and bypass_hole_too_big == False:
    print("hole too big")
    hole_too_big = True
else:
   hole_too_big = False




        #FILM HOLDER


#FH1, bas
FH_1_path = "./export/Film_Holder"
FH_1_file = "/Film_holder_1"
FH_1 = (
square(film_length + margin_film + wall_thickness + wall_thickness - tolerance_between_parts , film_height + margin_film + wall_thickness + wall_thickness - tolerance_between_parts, center=True ) 
#slide lock 
- square(film_length + margin_film + wall_thickness + (wall_thickness/2), sheet_thickness + tolerance_fine, center=True).forward((film_height + margin_film + (wall_thickness/2)-(tolerance_between_parts/2))/2)
+ square(film_length + margin_film + (wall_thickness/2) - tolerance_between_parts,sheet_thickness + (wall_thickness/8), center=True)
.forward((film_height + margin_film + (wall_thickness/2)-(tolerance_between_parts/2))/2)
)

#FH2, spacer 
FH_2_path = "./export/Film_Holder"
FH_2_file = "/Film_holder_2"
FH_2 = (
  square(film_length + margin_film + wall_thickness + wall_thickness - tolerance_between_parts , film_height + margin_film + wall_thickness + wall_thickness - tolerance_between_parts, center=True ) 
- square(film_length + margin_film, film_height + margin_film, center=True) 
#slide lock
- square(film_length + margin_film + wall_thickness + (wall_thickness/2), sheet_thickness + tolerance_fine, center=True).forward((film_height + margin_film + (wall_thickness/2)-(tolerance_between_parts/2))/2)
+ square(film_length + margin_film + (wall_thickness/2) - tolerance_between_parts,sheet_thickness + (wall_thickness/8), center=True)
.forward((film_height + margin_film + (wall_thickness/2)-(tolerance_between_parts/2))/2)
).up(1)

#FH3, enclosure dark slide
FH_3_path = "./export/Film_Holder"
FH_3_file = "/Film_holder_3"
FH_3 = (square(film_length + margin_film + wall_thickness + wall_thickness - tolerance_between_parts , film_height + margin_film + wall_thickness + wall_thickness - tolerance_between_parts, center=True )
- square(film_length + margin_film + wall_thickness, film_height + margin_film + wall_thickness + wall_thickness, center=True).forward(wall_thickness/2)
#slide lock
- square(film_length + margin_film + wall_thickness + (wall_thickness/2), sheet_thickness + tolerance_fine, center=True).forward((film_height + margin_film + (wall_thickness/2)-(tolerance_between_parts/2))/2)
).up(2)

#FH4, top
FH_4_path = "./export/Film_Holder"
FH_4_file = "/Film_holder_4"
FH_4 = (
  square(film_length + margin_film + wall_thickness + wall_thickness - tolerance_between_parts , film_height + margin_film + wall_thickness + wall_thickness - tolerance_between_parts, center=True ) 
- square(film_length + margin_film, film_height + margin_film, center=True)
    #slide lock
- square(film_length + margin_film + wall_thickness + (wall_thickness/2), sheet_thickness + tolerance_fine, center=True).forward((film_height + margin_film + (wall_thickness/2)-(tolerance_between_parts/2))/2)
+ square(film_length + margin_film + (wall_thickness/2) - tolerance_between_parts,sheet_thickness + (wall_thickness/8), center=True)
.forward((film_height + margin_film + (wall_thickness/2)-(tolerance_between_parts/2))/2)
).up(3)

#FH5, joint
FH_5_path = "./export/Film_Holder"
FH_5_file = "/Film_holder_5"
FH_5 = (square(film_length + margin_film + wall_thickness - tolerance_between_parts , film_height + margin_film + wall_thickness - tolerance_between_parts, center=True ) -
square(film_length + margin_film, film_height + margin_film, center=True)).up(4)

#FH6 dark slide
FH_6_path = "./export/Film_Holder"
FH_6_file = "/Dark_slide"
FH_6 = ( 
square(film_length + margin_film + wall_thickness - tolerance_fine, film_height + margin_film + wall_thickness - tolerance_fine + 30)
.left((film_length + margin_film + wall_thickness - tolerance_fine)/2).back((film_height + margin_film + wall_thickness - tolerance_fine)/2)
    #slide lock
- square(film_length + margin_film + wall_thickness + (wall_thickness/2), sheet_thickness + tolerance_fine, center=True).back((film_height + margin_film + (wall_thickness/2)-(tolerance_fine/2))/2)
- square(film_length + margin_film + wall_thickness + (wall_thickness/2), sheet_thickness + tolerance_fine, center=True).forward((film_height + margin_film + (wall_thickness/2)-(tolerance_between_parts/2))/2)
+ square(film_length + margin_film + (wall_thickness/2) - tolerance_between_parts, film_height + margin_film + wall_thickness - tolerance_fine + 30)
.left((film_length + margin_film + (wall_thickness/2) - tolerance_between_parts)/2).back((film_height + margin_film + wall_thickness - tolerance_fine)/2)
).up(2)

#FH7 slide lock
FH_7_path = "./export/Film_Holder"
FH_7_file = "/Slide_lock_1"
FH_7 = (
  square(film_length + margin_film + wall_thickness + (wall_thickness/2) - tolerance_between_parts, (sheet_thickness*6))
 .left((film_length + margin_film + wall_thickness + (wall_thickness/2) - tolerance_between_parts)/2)
- square(film_length + margin_film + (wall_thickness/2) , (sheet_thickness*5))
 .left((film_length + margin_film + (wall_thickness/2))/2).back(sheet_thickness)
).up(3).forward(film_height*1.5)

#FH8 slide lock handle
FH_8_path = "./export/Film_Holder"
FH_8_file = "/Slide_lock_2"
FH_8 = (
  square(film_length + margin_film + wall_thickness + (wall_thickness/2) - tolerance_between_parts, (sheet_thickness*2))
 .left((film_length + margin_film + wall_thickness + (wall_thickness/2) - tolerance_between_parts)/2).forward(sheet_thickness*4)
).up(4).forward(film_height*1.5)



        #REAR STANDARD


#RS1 bas
RS_1_path = "./export/Rear_Standard"
RS_1_file = "/Rear_Standard_1"
RS_1 = (
  square(film_length + margin_film + (wall_thickness*3), film_height + margin_film + (wall_thickness*3), center=True)
- square(film_length + margin_film + (wall_thickness*2), film_height + margin_film + (wall_thickness*2), center=True)
- square(film_length + margin_film + wall_thickness + tolerance_between_parts, wall_thickness, center=True).forward((film_height + margin_film + (wall_thickness*2.5))/2)
).down(2)

#RS2_a slot lige
RS_2_a_path = "./export/Rear_Standard"
RS_2_a_file = "/Rear_Standard_2_a"
RS_2_a = (
  square(film_length + margin_film + (wall_thickness*3), wall_thickness/2, center=True).back((film_height + margin_film + (wall_thickness*2.5))/2)
).down(1)

#RS2_b slot lige
RS_2_b_path = "./export/Rear_Standard"
RS_2_b_file = "/Rear_Standard_2_b"
RS_2_b = (
  square(wall_thickness/2, film_height + margin_film + wall_thickness - tolerance_between_parts, center=True).left((film_length + margin_film + (wall_thickness*2.5))/2)
).down(1)

#RS2_c slot lige
RS_2_c_path = "./export/Rear_Standard"
RS_2_c_file = "/Rear_Standard_2_c"
RS_2_c = (
  square(wall_thickness/2, film_height + margin_film + wall_thickness - tolerance_between_parts, center=True).right((film_length + margin_film + (wall_thickness*2.5))/2)
).down(1)

#RS2_d slot lige
RS_2_d_path = "./export/Rear_Standard"
RS_2_d_file = "/Rear_Standard_2_d"
RS_2_d = (
  square(film_length + margin_film + (wall_thickness*3), wall_thickness/2, center=True).forward((film_height + margin_film + (wall_thickness*2.5))/2)
-   square(film_length + margin_film + (wall_thickness*3), wall_thickness, center=True).forward((film_height + margin_film + (wall_thickness*2.5))/2).left(wall_thickness - (tolerance_between_parts)/2)
).down(1)

#RS2_e slot lige
RS_2_e_path = "./export/Rear_Standard"
RS_2_e_file = "/Rear_Standard_2_e"
RS_2_e = (
  square(film_length + margin_film + (wall_thickness*3), wall_thickness/2, center=True).forward((film_height + margin_film + (wall_thickness*2.5))/2)
-   square(film_length + margin_film + (wall_thickness*3), wall_thickness, center=True).forward((film_height + margin_film + (wall_thickness*2.5))/2).right(wall_thickness - (tolerance_between_parts)/2)
).down(1)

#RS3
RS_3_path = "./export/Rear_Standard"
RS_3_file = "/Rear_Standard_3"
RS_3 = RS_1.up(2)

#RS4
RS_4_path = "./export/Rear_Standard"
RS_4_file = "/Rear_Standard_4"
RS_4 = RS_1.up(3)

#RS5
RS_5_path = "./export/Rear_Standard"
RS_5_file = "/Rear_Standard_5"
RS_5 = RS_1.up(4)

#RS6
RS_6_path = "./export/Rear_Standard"
RS_6_file = "/Rear_Standard_6"
RS_6 = (
  square(film_length + margin_film + (wall_thickness*3), film_height + margin_film + (wall_thickness*3), center=True)
- square(film_length + margin_film + (wall_thickness*2), film_height + margin_film + (wall_thickness*2), center=True)
).up(3)

#RS7
RS_7_path = "./export/Rear_Standard"
RS_7_file = "/Rear_Standard_7"
RS_7 = (
  square(film_length + margin_film + (wall_thickness*3), film_height + margin_film + (wall_thickness*3), center=True)
- square(film_length + margin_film + (wall_thickness), film_height + margin_film + (wall_thickness), center=True)
).up(4)

#RS8
RS_8_path = "./export/Rear_Standard"
RS_8_file = "/Rear_Standard_8"
RS_8 = (
  square(film_length + margin_film + (wall_thickness*3), film_height + margin_film + (wall_thickness*3), center=True)
- square(film_length + margin_film , film_height + margin_film, center=True)
).up(5)

#RS9_a tige
RS_9_a_path = "./export/Rear_Standard"
RS_9_a_file = "/Rod_Lock_1_a"
RS_9_a = (
  square(film_length + margin_film + (wall_thickness*3) + (wall_thickness/2), wall_thickness/2, center=True)
  .forward((film_height + margin_film + (wall_thickness*1.5)-(tolerance_between_parts/2))/2).left(wall_thickness/4)
).down(1)

#RS9_b tige
RS_9_b_path = "./export/Rear_Standard"
RS_9_b_file = "/Rod_Lock_1_b"
RS_9_b = RS_9_a.back((film_height + margin_film + (wall_thickness*1.5)-(tolerance_between_parts/2)))

#RS10_a tige handle 
RS_10_a_path = "./export/Rear_Standard"
RS_10_a_file = "/Rod_Lock_2_a"
RS_10_a = (
  square(wall_thickness/2, wall_thickness/2, center=True)
.left((film_length + margin_film + (wall_thickness*3) + (wall_thickness/2))/2)
.forward((film_height + margin_film + (wall_thickness*1.5)-(tolerance_between_parts/2))/2)
)

#RS10_b tige handle
RS_10_b_path = "./export/Rear_Standard"
RS_10_b_file = "/Rod_Lock_2_b"
RS_10_b = RS_10_a.back((film_height + margin_film + (wall_thickness*1.5)-(tolerance_between_parts/2)))




        #FRONT STANDARD


#FS_1
FS_1_path = "./export/Front_Standard"
FS_1_file = "/Front_Standard_1"
FS_1 = (
  square(film_height + margin_film + (wall_thickness*3), center=True)
- square(film_height + margin_film + wall_thickness, center=True)
).up(50)

#FS_2
FS_2_path = "./export/Front_Standard"
FS_2_file = "/Front_Standard_2"
FS_2 = (
  square(film_height + margin_film + (wall_thickness*3), center=True)
- square(film_height + margin_film + (wall_thickness*2), center=True)
).up(51)

#FS_3_a slot lige
FS_3_a_path = "./export/Front_Standard"
FS_3_a_file = "/Front_Standard_3_a"
FS_3_a = (
  square(film_height + margin_film + (wall_thickness*3), wall_thickness/2, center=True).back((film_height + margin_film + (wall_thickness*2.5))/2)
).up(52)

#RS3_b slot lige
FS_3_b_path = "./export/Front_Standard"
FS_3_b_file = "/Front_Standard_3_b"
FS_3_b = (
  square(wall_thickness/2, film_height + margin_film + wall_thickness - tolerance_between_parts, center=True).left((film_height + margin_film + (wall_thickness*2.5))/2)
).up(52)

#RS3_c slot lige
FS_3_c_path = "./export/Front_Standard"
FS_3_c_file = "/Front_Standard_3_c"
FS_3_c = (
  square(wall_thickness/2, film_height + margin_film + wall_thickness - tolerance_between_parts, center=True).right((film_height + margin_film + (wall_thickness*2.5))/2)
).up(52)

#RS3_d slot lige
FS_3_d_path = "./export/Front_Standard"
FS_3_d_file = "/Front_Standard_3_d"
FS_3_d = (
  square(film_height + margin_film + (wall_thickness*3), wall_thickness/2, center=True).forward((film_height + margin_film + (wall_thickness*2.5))/2)
).up(52)

#FS4
FS_4_path = "./export/Front_Standard"
FS_4_file = "/Front_Standard_4"
FS_4 = (
  square(film_height + margin_film + (wall_thickness*3), center=True)
- square(film_height + margin_film + (wall_thickness*2), center=True)
).up(53)

#FS5
FS_5_path = "./export/Front_Standard"
FS_5_file = "/Front_Standard_5"
FS_5 = (
  square(film_height + margin_film + (wall_thickness*3), wall_thickness/2, center=True).back((film_height + margin_film + (wall_thickness*2.5))/2)
).up(54)

#FS6
FS_6_path = "./export/Front_Standard"
FS_6_file = "/Front_Standard_6"
FS_6 = (
  square(film_height + margin_film + (wall_thickness*3), wall_thickness/2, center=True).back((film_height + margin_film + (wall_thickness*2.5))/2)
).up(55)

#FS7_a tige
FS_7_a_path = "./export/Front_Standard"
FS_7_a_file = "/Rod_Lock_1_a"
FS_7_a = (
  square(film_height + margin_film + (wall_thickness*3) + (wall_thickness/2), wall_thickness/2, center=True)
  .forward((film_height + margin_film + (wall_thickness*1.5)-(tolerance_between_parts/2))/2).left(wall_thickness/4)
).up(52)

#FS7_b tige
FS_7_b_path = "./export/Front_Standard"
FS_7_b_file = "/Rod_Lock_1_b"
FS_7_b = FS_7_a.back((film_height + margin_film + (wall_thickness*1.5)-(tolerance_between_parts/2)))

#FS8_a tige handle 
FS_8_a_path = "./export/Front_Standard"
FS_8_a_file = "/Rod_Lock_2_a"
FS_8_a = (
  square(wall_thickness/2, wall_thickness/2, center=True)
.left((film_height + margin_film + (wall_thickness*3) + (wall_thickness/2))/2)
.forward((film_height + margin_film + (wall_thickness*1.5)-(tolerance_between_parts/2))/2)
).up(53)

#FS_8_b tige handle
FS_8_b_path = "./export/Front_Standard"
FS_8_b_file = "/Rod_Lock_2_b"
FS_8_b = FS_8_a.back((film_height + margin_film + (wall_thickness*1.5)-(tolerance_between_parts/2)))

#FS_9 lens plate
FS_9_path = "./export/Front_Standard"
FS_9_file = "/lens plate"
if hole_too_big != True:
  FS_9 = (  
     square(film_height + margin_film + (wall_thickness*2) - tolerance_between_parts, center=True)
     -circle(lens_plate_hole_diameter)
  ).up(51)
else:
  FS_9 = (  
  square(film_height + margin_film + (wall_thickness*2) - tolerance_between_parts, center=True)
  -text(text= "hole too big",size=film_height/8, halign="center", valign="center")
  ).up(51)

    




# Gound Glass

#GG 1 
GG_1_path = "./export/Ground_Glass"
GG_1_file = "/Ground_Glass_1"
GG_1 = ( 
  square(film_length + margin_film + wall_thickness + wall_thickness - tolerance_between_parts , film_height + margin_film + wall_thickness + wall_thickness - tolerance_between_parts, center=True ) 
- square(film_length + margin_film + wall_thickness, film_height + margin_film + wall_thickness, center=True ) 
)

#GG 2 
GG_2_path = "./export/Ground_Glass"
GG_2_file = "/Ground_Glass_2"
GG_2 = ( 
  square(film_length + margin_film + wall_thickness + wall_thickness - tolerance_between_parts , film_height + margin_film + wall_thickness + wall_thickness - tolerance_between_parts, center=True ) 
- square(film_length + margin_film, film_height + margin_film, center=True ) 
).up(1)

#GG 3 
GG_3_a_path = "./export/Ground_Glass"
GG_3_a_file = "/Ground_Glass_3_a"
GG_3_a = ( 
   square(film_length + margin_film , wall_thickness/2, center=True)
).up(2).back((film_height + margin_film + wall_thickness)/2)

#GG 3_a 
GG_3_b_path = "./export/Ground_Glass"
GG_3_b_file = "/Ground_Glass_3_b"
GG_3_b = ( 
   square(film_length + margin_film , wall_thickness/2, center=True)
).up(2).forward((film_height + margin_film + wall_thickness)/2)

#GG 4 
GG_4_a_path = "./export/Ground_Glass"
GG_4_a_file = "/Ground_Glass_4_a"
GG_4_a = ( 
   GG_3_a
).up(1)

#GG 4_b 
GG_4_b_path = "./export/Ground_Glass"
GG_4_b_file = "/Ground_Glass_4_b"
GG_4_b = ( 
   GG_3_b
).up(1)

#GG 5 
GG_5_path = "./export/Ground_Glass"
GG_5_file = "/Glass_size"
GG_5 = ( 
   square(film_length + margin_film + wall_thickness - tolerance_between_parts, film_height + margin_film + wall_thickness - tolerance_between_parts, center=True ) 
)

liste_des_formes = [
                    #film holder
                    {"path": FH_1_path, "nom": FH_1_file, "geometrie": FH_1},
                    {"path": FH_2_path, "nom": FH_2_file, "geometrie": FH_2},
                    {"path": FH_3_path, "nom": FH_3_file, "geometrie": FH_3},
                    {"path": FH_4_path, "nom": FH_4_file, "geometrie": FH_4},
                    {"path": FH_5_path, "nom": FH_5_file, "geometrie": FH_5},
                    {"path": FH_6_path, "nom": FH_6_file, "geometrie": FH_6},
                    {"path": FH_7_path, "nom": FH_7_file, "geometrie": FH_7},
                    {"path": FH_8_path, "nom": FH_8_file, "geometrie": FH_8},

                    #rear standard 
                    {"path": RS_1_path, "nom": RS_1_file, "geometrie": RS_1},
                    {"path": RS_2_a_path, "nom": RS_2_a_file, "geometrie": RS_2_a},
                    {"path": RS_2_b_path, "nom": RS_2_b_file, "geometrie": RS_2_b},
                    {"path": RS_2_c_path, "nom": RS_2_c_file, "geometrie": RS_2_c},
                    {"path": RS_2_d_path, "nom": RS_2_d_file, "geometrie": RS_2_d},
                    {"path": RS_2_e_path, "nom": RS_2_e_file, "geometrie": RS_2_e},
                    {"path": RS_3_path, "nom": RS_3_file, "geometrie": RS_3},
                    {"path": RS_4_path, "nom": RS_4_file, "geometrie": RS_4},
                    {"path": RS_5_path, "nom": RS_5_file, "geometrie": RS_5},
                    {"path": RS_6_path, "nom": RS_6_file, "geometrie": RS_6},
                    {"path": RS_7_path, "nom": RS_7_file, "geometrie": RS_7},
                    {"path": RS_8_path, "nom": RS_8_file, "geometrie": RS_8},
                    {"path": RS_9_a_path, "nom": RS_9_a_file, "geometrie": RS_9_a},
                    {"path": RS_9_b_path, "nom": RS_9_b_file, "geometrie": RS_9_b},
                    {"path": RS_10_a_path, "nom": RS_10_a_file, "geometrie": RS_10_a},
                    {"path": RS_10_b_path, "nom": RS_10_b_file, "geometrie": RS_10_b},

                    #front standard 
                    {"path": FS_1_path, "nom": FS_1_file, "geometrie": FS_1},
                    {"path": FS_2_path, "nom": FS_2_file, "geometrie": FS_2},
                    {"path": FS_3_a_path, "nom": FS_3_a_file, "geometrie": FS_3_a},
                    {"path": FS_3_b_path, "nom": FS_3_b_file, "geometrie": FS_3_b},
                    {"path": FS_3_c_path, "nom": FS_3_c_file, "geometrie": FS_3_c},
                    {"path": FS_3_d_path, "nom": FS_3_d_file, "geometrie": FS_3_d},
                    {"path": FS_4_path, "nom": FS_4_file, "geometrie": FS_4},
                    {"path": FS_5_path, "nom": FS_5_file, "geometrie": FS_5},
                    {"path": FS_6_path, "nom": FS_6_file, "geometrie": FS_6},
                    {"path": FS_7_a_path, "nom": FS_7_a_file, "geometrie": FS_7_a},
                    {"path": FS_7_b_path, "nom": FS_7_b_file, "geometrie": FS_7_b},
                    {"path": FS_8_a_path, "nom": FS_8_a_file, "geometrie": FS_8_a},
                    {"path": FS_8_b_path, "nom": FS_8_b_file, "geometrie": FS_8_b},
                    {"path": FS_9_path, "nom": FS_9_file, "geometrie": FS_9},



                    ]



if previs == False:
    for i in liste_des_formes:


        scad_render_to_file(i["geometrie"], 'tempo.scad')
        print("fichier tempo cree")

        os.makedirs(i["path"], exist_ok = True)
        print("dossier cree")

        subprocess.run([openscad_path, "-o", i["path"] + i["nom"]+ file_format, "tempo.scad"])
        print("exporter bien")

        os.remove("tempo.scad")
        print("fichier tempo retirer")

else:
   geometrie_previs = (
   #le cube vide c est pour pouvoir metre les # et cacher des trucs 
 
    cube(0)

    #film holder
    +FH_1.color("#b734d8ff")  #bas (film plane)
    +FH_2.color("#da74f3ff")  #spacer 
    +FH_3.color("#b734d8ff")  #enclosure dark slide
    +FH_4.color("#da74f3ff")  #top
    +FH_5.color("#b734d8ff")  #joint 
    +FH_6.color("#3234ccff")  #dark slide
    +FH_7.color("#b734d8ff")  #slide lock
    +FH_8.color("#da74f3ff")  #slide lock handle  

    #rear stadandard 
    #+RS_1.color("#c3e93aff")  #bas
    #+RS_2_a.color("#90a546ff")  #slot tige
    #+RS_2_b.color("#90a546ff")
    #+RS_2_c.color("#90a546ff") 
    #+RS_2_d.color("#90a546ff")
    #+RS_2_e.color("#90a546ff")
    #+RS_3.color("#c3e93aff")
    #+RS_4.color("#90a546ff")
    #+RS_5.color("#c3e93aff")
    #+RS_6.color("#90a546ff")
    #+RS_7.color("#c3e93aff")
    #+RS_8.color("#90a546ff")  #interface bellow
    #+RS_9_a.color("#657235ff") #tige
    #+RS_9_b.color("#657235ff")
    #+RS_10_a.color("#7f8b50ff")
    #+RS_10_b.color("#7f8b50ff")

    #front standard 

    +FS_1.color("#be5f3aff")    #back
    +FS_2.color("#db8360ff")
    +FS_3_a.color("#be5f3aff")  #slot tige
    +FS_3_b.color("#be5f3aff")
    +FS_3_c.color("#be5f3aff")
    +FS_3_d.color("#be5f3aff")
    +FS_4.color("#db8360ff")     #top
    +FS_5.color("#be5f3aff")     #thikkener
    +FS_6.color("#db8360ff")     #thikkener 
    +FS_7_a.color("#657235ff")   #tiges
    +FS_7_b.color("#657235ff")
    +FS_8_a.color("#7f8b50ff")
    +FS_8_b.color("#7f8b50ff")
    +FS_9.color("#2a37adff")     # lens plate


    #Ground Glass   

    #+GG_1.color("#2aad33ff") #ground glass side
    #+GG_2.color("#1f5a23ff") 
    #+GG_3_a.color("#2aad33ff")
    #+GG_3_b.color("#2aad33ff")
    #+GG_4_a.color("#1f5a23ff") #top
    #+GG_4_b.color("#1f5a23ff") #top
    #+GG_5.color("#2a37adff") #glass size
    

                        )




   scad_render_to_file(geometrie_previs, "previs.scad")


print("finito")