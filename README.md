# Grey-slice  
# REPO NOTE FINISHED, NOT READY YET 
A highly accessible, parametric, DIY medium/large format field camera who can be built with basic tools, stacked grey cardboard, and paper.
And can easily be modified/adapted and built with different material (like laser cut acrylic panels)


---


##  Features & Design

### Build Principle
To keep things accessible, the camera body is  built entirely from stacked layers of grey cardboard glued together with wood glue(but other material could be used). The core design is parametric, meaning it can be scaled to any size (My first prototype was 8x20 inches).
And because the desing is simple it can be easely modified/adapted.

### Paper Bellows
Using a DIY bellows provides full lens movements and the ability to change focal lengths. While made of paper, it is inexpensive, easy to fold, and simple to patch/reinforce with black tape.

### Modular Focusing System
The front and rear standards are independent and modular. They rely on simple tripode hole to attache on existing gear you might already have:
*   Basic setup: Two tripods (or one tripod and a flash plate) holding the front and rear standards separately.
*   My setup : One tripod holding the rear standard with macro focusing rail bewin, with a magic arm attached to the front standard. This allows for precise focusing and movement.

### Film Back
The film back features a simple dark slide locking mechanism consisting of two bars loxking on the side of the dark slide, to improve light tightnesse, the dark-slide is never fully remove from the back, it is lock on the top edge edge. By default the slit is on top (to avoid putting mass on the side) but you can invert x and y mesurment to put it on the side.
As for the film monting, it is ment to be held by weak double sided tape (who is quite nice for paper) but feel free to do you own holding machanisme

### Interchangeable Lens Boards
The lens board is extremely simple: a square of grey cardboard with a hole cut in the center. 

### Shutter
Currently, exposures are made using a simple lens cap (relying in verry low iso or/and nd filter) but a guillotine-style shutter is in development. 

### material
The camera can be built with multiple kind of material, but the easier and most accessible are : grey cardboard for the body and paper for the bellow,

but other material could be used if you have the tools or will order cutter part online, like opaque plastic plate laser cutted, hard wood sheet, leather/fabric for the bellow...

---

##  Materials & Tools

### Raw Materials
- grey cardboard sheets (3mm preference)
- Black Canson paper (160-200g)
- 2x 1/4"-20 tripod mounting plates 
- Tracing paper or plexiglass + fine grinding powder
- Wood glue

### Tools & Consumables
- Metal ruler (Mandatory for cutting with craft knife)
- T-square or set square
- utility knif
- precision craft knife
- Précise pénil
- somes flat heavy objects (books) or clamps
- paintbrush for glue

---

##  Getting the plan

The camera's parts are generated using a parametric Python script based on SolidPython (an OpenSCAD translator). By inputting your desired dimensions, the program exports every part into ordered folders.

**Prerequisites:**
1. Install [Python](https://www.python.org/)
2. Install [SolidPython](https://github.com/SolidCode/SolidPython)
3. Install [OpenSCAD](https://openscad.org/)
4. Install [VScode](https://code.visualstudio.com/)
5. Install python and openscad addon on vscode


**Running the program:**
1. Open the script with vs code and open the programme folder inside vscode, modify the variables for your desired camera size and other parameter :
   -file_format: Can be `".dxf"`, `".svg"` or `".pdf"`
   -previs = `False` will outpout the files in ordered folder, `True` will generate a .scad to vew in openSCAD
   -openscad_path = put the path to the openscad .exe like `"D:\Programmes\openscad\openscad.exe"`
   -film_height = height of the film in mm (like any other value) you can intervert height and lenght to put the film holder slit on the side
   -film_length = 
   -wall_thickness = wall thikness is the thiknesse of the wall, "light joint" and locking bars
   -sheet_thickness = is the thikness of your grey cardboard 
   -lens_plate_hole_diameter = is the diamiter of the hole to fit your lens 
   -bypass_hole_too_big = if the hole is too big and would colide with other part(like lens plate locking rode) it will show an arror message directely on the lens plate, but if you know what your doing you can change the parameter from False to True 
   -margin_film = is the margine betwine the side of the film and the wall 
   -tolerance_between_parts = is the tolerences bewine front standard-lens plate and back standard and film holder 
   -tolerance_fine = is the tolerences of the locking mechanisme
   
3. Run the script.
4. The program will output in the program location organized folders containing SVG/DXF files for each slice.

**Understanding the file nomenclature:**
Files are named using the following logic: `PartName_SliceHeight_PieceIndex.svg`
*(Example: `Front_Standard_3_c.svg`)*
*   `Front Standard`: The name of the assembly.
*   `3`: The layer number, counting from the back of the camera to the front (this is the 3rd layer).
*   `c`: The 3rd piece of this specific layer.

*(Note: I will at some point include a web app to generate these files online without any installation.)*

---

## Build Instructions

### 1. Tracing the Panels
If cutting by hand,you can upload the DXF files to a free viewer like [Materlogic](https://materlogic.com/en/dxf-viewer) to get the exact dimensions. Use a pencil and a set-square to trace each piece onto your cardboard, ensuring the corners are perfectly square and parallel.
you can also print all pieces on paper and glue (with a light glue spray) the paper on grey cardboard to see where to cut directly 

### 2. Cutting the Cardboard
**Safety first:** Always use a metal ruler. A plastic ruler will catch the blade and cut your fingers. 
*   Do not try to cut through the 3mm cardboard in one pass. Make multiple light passes.
*   You cane use a utility-knife straight lines (don't forget to snap off or replace blades frequently to get cleaner result).
*   And an X-Acto knife for detailed edges and precise corners.


you can also , if you have one, laser cut everyching, or order them 

### 3. Gluing the Assembly
Wood glue (PVA) is cheap and works perfectly for grey cardboard. 
1. Paint the glue onto the surface using a brush for an even coat.
2. Align the layers carefully.
3. Place a heavy book on top or use clamps to hold it flat. **Do not apply too much pressure**, as this can warp the cardboard and make harder the fit of the parts. 
*(Optional: You can dye the wood glue black before applying to ensure perfect light-tightness, though this is is overkill).*

<img width="320" alt="Gluing the panels" src="https://github.com/user-attachments/assets/be3dbe97-3e83-4071-aa85-ba86a561b4f0" />

### 4. Making the Bellows
The bellows are made from thick black Canson paper.(160-200g)

1. Generate your bellows pattern. (I used the calculator at [apenasimagens.com](https://apenasimagens.com/en/bellows-project-tailor-made-for-you/) — it costs 25,00 BRL (≈4€50) but provides a custom pattern).
2. Slice the pattern into multiple A4 sheet, print them, and tape them together.
3. Tape the pattern over your black paper and trace the folding lines using a ballpoint pen. **Press lightly** just enough to score the paper without tearing it.(If the pattern is larger than your paper, glue multiple sheets together).
4. Cut out the exterior shape. 
5. Glue the ends of the sheet to form a tube, and begin carefully folding the ridges along your scored lines.

<img width="320" alt="Bellows Fold 1" src="https://github.com/user-attachments/assets/d04dfdb4-7f54-479c-83d7-7134e84f29da" />
<img width="320" alt="Bellows Fold 2" src="https://github.com/user-attachments/assets/81d1dc75-0875-4903-abc1-2bacbd592b56" />
<img width="320" alt="Bellows Fold 3" src="https://github.com/user-attachments/assets/1f74921d-ef1e-4af6-b975-9e20e117f207" />
<img width="320" alt="Bellows Fold 4" src="https://github.com/user-attachments/assets/f5979992-e605-4bed-87a2-29f09e293fdb" />
<img width="240" alt="Bellows Fold 5" src="https://github.com/user-attachments/assets/fdc94b3f-2c9c-4fbc-a48e-b73334c7fc3e" />

---

## Using Grey-slice

### Durability & Storage
Because the camera is made of paper and cardboard, it is not weather-sealed and must be stored in a relatively dry environment. However, its material makes it easy to repair, patch, or reglue if damaged.

###Transport 
The bellow make the camera relatively compact when folded and with mini tripod, everything can fit in a small camera bag,
event and ULF vertion, like 8/20 inch,can fit in a bag, with the tripod on the side, and other accessories in a small bag.




### Film Recommendations
Because the camera currently relies on a lens cap instead of a mechanical shutter (for now), exposure times need to be long. So a verry low iso is helpful.

I mostly use photo paper developed in reversal chemistry, (permanganates potatium + sulfuric acide bleach) this give a verry nice way to present and encadre the pictur who where directely in the camera.



---

To Do

-add eather a print bellow specification or .txt with calculations 

-Allow front standard size to be independent from the back in size (for now it is equal to rear standard height).

-Integrate a bellows pattern generator directly into the Python script. (for now, paid online generator )

-include diy lens plans using standard achromatic lenses (in a general section about lenses) and do a housing disinge practical to hand cut (not too mutch round peces)

-Design and integrate a guillotine shutter with parametric variables for different shutter speed.

-Host a web-based version of the generator so users don't have to install OpenSCAD/Python.

-add variable for laser with compensation 

-do grand variable to make creating new part faster and easier to make? (like "fW_m_w1_w2_T" pour filmwith+margined+2wall-tolerences) or better nomenclature:
_film
_first_wall
_second_wall(-tolerence)
_third_wall(-tolerence) 


-do a film back who use 120 film (only using 2 part (sandwiches using back locking barr?))


-message the guy form the online bellow calculator to see if if I can put the pattern for the 6/17.8 freely on the repo (and pre cut it in multiple A4 easy to align with alignment lines)

-make a pdf who name every measurement and make the programme create a txt with every measurement 

- different side finish ? like whave patern? 

---
