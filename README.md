# Grey-slice
> A highly accessible, parametric, DIY medium/large format field camera built with basic tools, stacked grey cardboard, and paper. 

Grey-slice is designed to make large format photography accessible. By using a parametric design and stacked 3mm cardboard layers, this camera can be built with minimal equipment—either cut by hand or with a laser cutter. 

---

## 📋 Table of Contents
- [Features & Design](#features--design)
- [Materials & Tools](#materials--tools)
- [Getting the Files](#getting-the-files)
- [Build Instructions](#build-instructions)
- [Shooting with Grey-slice](#shooting-with-grey-slice)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](https://github.com/labodugo/Grey-slice/edit/main/README.md#-license)

---

## ✨ Features & Design

### Build Principle
To keep things accessible, the camera body is built entirely from stacked layers of 3mm grey cardboard glued together with wood glue. The core design is parametric, meaning it can be scaled to any size (the prototype is 8x20 inches) by adjusting variables in the code.

### Paper Bellows
Using a DIY bellows provides full lens movements and the ability to change focal lengths. While made of paper (which can wear over time), it is inexpensive, easy to fold, and simple to patch with black tape. *(Tip: Pre-taping the edges can prevent pinholes from forming.)*

### Modular Focusing System
The front and rear standards are independent and modular. They rely on existing gear you might already have:
*   **Basic setup:** Two tripods (or one tripod and a flash bracket) holding the front and rear standards separately.
*   **Advanced setup (Recommended):** One tripod holding the rear standard, with a magic arm and a macro focusing rail attached to the front standard. This allows for precise focusing, full range of movements, and easy macro work.

### Film Back
The film back features a simple, highly effective dark slide locking mechanism consisting of two rods on the side. 
*   **Top-loading:** The dark slide is pulled from the top to prevent bending the camera or throwing it off level (though the parametric design allows you to change this to a side-pull if desired).
*   **Light-proofing:** The dark slide remains partially in the camera during exposure to maintain light tightness.
*   **Film mounting:** Film or photo paper is held perfectly flat using weak double-sided tape. This makes the back highly adaptable for different mediums, including objects coated in photo emulsion.

### Interchangeable Lens Boards
The lens board is extremely simple: a square of grey cardboard with a hole cut in the center. 
*   **Lens options:** A simple pinhole, a single-element lens, cheap achromatic lenses (for better aberration control), or a DIY "rapid rectilinear" lens built using two achromatic lenses mounted facing each other.

### Shutter (Obturator)
Currently, exposures are made using a simple lens cap. A guillotine-style shutter is in development. 

---

## 🛠 Materials & Tools

### Raw Materials
- 3mm grey cardboard sheets
- Black Canson paper *(Thickness used: [Insert thickness, e.g., 160g/m²])*
- 2x 1/4"-20 tripod mounting plates 
- Tracing paper or frosted plexiglass (for the ground glass/focusing screen)
- Wood glue (PVA / white glue)
- Weak double-sided tape (for holding film)

### Tools & Consumables
- Metal ruler **(Mandatory for safety when cutting!)**
- T-square or set square
- Heavy-duty utility knife (box cutter) with fresh blades
- X-Acto / precision craft knife
- Mechanical pencil
- Assorted heavy objects (books) or clamps to use as weights
- Small paintbrush for glue

---

## 💻 Getting the Files

The camera's parts are generated using a parametric Python script based on SolidPython (an OpenSCAD translator). By inputting your desired dimensions, the program exports every part into ordered folders.

**Prerequisites:**
1. Install [Python](https://www.python.org/)
2. Install [SolidPython](https://github.com/SolidCode/SolidPython)
3. Install [OpenSCAD](https://openscad.org/)

**Running the program:**
1. Open the script and modify the variables for your desired camera size.
2. Run the script.
3. The program will output organized folders containing SVG/DXF files for each slice.

**Understanding the file nomenclature:**
Files are named using the following logic: `PartName_SliceHeight_PieceIndex.svg`
*(Example: `Front_Standard_3_c.svg`)*
*   **Front Standard:** The name of the assembly.
*   **3:** The layer number, counting from the back of the camera to the front (this is the 3rd layer).
*   **c:** The 3rd piece of this specific layer.

*(Note: A future update will include a web app to generate these files online without any installation.)*

---

## 🔨 Build Instructions

### 1. Tracing the Panels
If cutting by hand, upload the DXF files to a free viewer like [Materlogic](https://materlogic.com/en/dxf-viewer) to get the exact dimensions. Use a mechanical pencil and a T-square to trace each piece onto your cardboard, ensuring the corners are perfectly square.

### 2. Cutting the Cardboard
**Safety first:** Always use a metal ruler. A plastic ruler will catch the blade and cause severe injury. 
*   Do not try to cut through the 3mm cardboard in one pass. Make multiple light passes.
*   Use a heavy-duty box cutter for long, straight lines (snap off or replace blades frequently).
*   Use an X-Acto knife for detailed edges and precise corners.

### 3. Gluing the Assembly
Wood glue (PVA) is cheap and works perfectly for grey cardboard. 
1. Paint the glue onto the surface using a brush for an even coat.
2. Align the layers carefully.
3. Place a heavy book on top or use clamps to hold it flat. **Do not apply too much pressure**, as this can warp the cardboard and ruin the fit of the parts. 
*(Optional: You can dye the wood glue black before applying to ensure perfect light-tightness, though this is usually overkill).*

<img width="320" alt="Gluing the panels" src="https://github.com/user-attachments/assets/be3dbe97-3e83-4071-aa85-ba86a561b4f0" />

### 4. Making the Bellows
The bellows are made from thick black Canson paper. 

1. Generate your bellows pattern. (I used the calculator at [apenasimagens.com](https://apenasimagens.com/en/bellows-project-tailor-made-for-you/) — it costs ~€3 but provides a custom pattern).
2. Slice the pattern into A4 sizes, print them, and tape them together.
3. Place the pattern over your black paper and trace the folding lines using a ballpoint pen. **Press lightly**—just enough to score the paper without tearing it.
4. Cut out the exterior shape. (If the pattern is larger than your paper, glue multiple sheets together).
5. Glue the ends of the sheet to form a tube, and begin carefully folding the ridges along your scored lines.

<img width="320" alt="Bellows Fold 1" src="https://github.com/user-attachments/assets/d04dfdb4-7f54-479c-83d7-7134e84f29da" />
<img width="320" alt="Bellows Fold 2" src="https://github.com/user-attachments/assets/81d1dc75-0875-4903-abc1-2bacbd592b56" />
<img width="320" alt="Bellows Fold 3" src="https://github.com/user-attachments/assets/1f74921d-ef1e-4af6-b975-9e20e117f207" />
<img width="320" alt="Bellows Fold 4" src="https://github.com/user-attachments/assets/f5979992-e605-4bed-87a2-29f09e293fdb" />
<img width="240" alt="Bellows Fold 5" src="https://github.com/user-attachments/assets/fdc94b3f-2c9c-4fbc-a48e-b73334c7fc3e" />

---

## 📷 Shooting with Grey-slice

### Durability & Storage
Because the camera is made of paper and cardboard, it is not weather-sealed and must be stored in a dry environment. However, its material makes it incredibly easy to repair, patch, or reglue if damaged.

### Film Recommendations
Because the camera currently relies on a lens cap instead of a mechanical shutter, exposure times will be long. 
*   **Direct Positive/Negative Photo Paper:** Standard B&W darkroom paper is highly recommended (ISO 1-6). 
*   **Reversal Processing:** You can shoot on standard photo paper and develop it as a positive using a potassium permanganate bleach process.

---

## 🚀 Roadmap (To Do)
- [ ] Allow front standard size to be independent in the code (constrained only by the rear standard size).
- [ ] Integrate a bellows specification/pattern generator directly into the Python script.
- [ ] Design an integrated guillotine drop-shutter triggered by a cable release. 
- [ ] Add parametric variables for shutter slit sizes (e.g., inputting `shutter_speed = 200` to automatically calculate the slit width).
- [ ] Host a web-based version of the generator so users don't have to install OpenSCAD/Python.

---

## 🤝 Contributing
Contributions, modifications, and forks are highly encouraged! If you build your own Grey-slice or design an add-on (like a shutter mechanism or a new film back), feel free to open a Pull Request or share your build in the Issues tab.

## 📄 License
[Insert your chosen license here, e.g., MIT License, Creative Commons Attribution-NonCommercial (CC BY-NC), etc.]
