# PyQT Tutorials For Software Engineer and Professional
----
## 1.Setup the envirnment:
* Run the following command in command promot with administrator access 
    * ```bash
      pip install PyQt6
      ```
    * ```bash
      pip install PyQt-tools
      ```
## 2. How to use QtDesigner
* Run this command in same folder and it will open designer
  * ```bash
    PyQt5-tools designer
    ```
* Now create a design and save this in the working folder, then run this command
  * ```bash
   pyuic5 -x filename.ui -o filename.py
   ```
* Now fix this generated script and write codes as per your requirement.
