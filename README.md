# Welcome to the BRASA Payment Microservice!

## Important Links
- Notion - https://marble-swordfish-9e2.notion.site/BRASA-App-3507314462cd48a6ade0cf3594514195
- GitHub - https://github.com/UCF-BRASA/BRASA-Payment-Microservice

# Setup

## (Disclaimer)
All the commands below should be be ran on a GIT BASH terminal. I recommend using the terminal of your favorite IDE.
Here's an example of where you can find on Visual Studio Code on a Windows OS:

![terminal sc](https://user-images.githubusercontent.com/73730027/174506986-063e3d0f-c611-4172-af77-deeef4603e6a.png)


## 1. Install Python
Please install the most recent version of Python here: https://www.python.org/downloads/

## 2. Clone this repository
```
git clone https://github.com/UCF-BRASA/BRASA-Payment-Microservice.git
```

## 2. Run the setup script (in a Git terminal)
- For Windows (go to ):
  ```
  bash RUN_ME_IN_GIT.sh
  ```

- For Linux/Mac OS: <br>
  (if it's not working, please contact Fachetti or Duda)

<hr>

* TO PREVENT BUGS, PLEASE RUN THE FOLLOWING COMMAND
  ```
  pip install pipenv
  ```


## 3. Activate the environment (in any terminal)
```
python -m pipenv shell
```

## 4. Use Python interpreter from the local virtual environment (if this step is too confusing, please reach out to us!)
1. To find your virtual environment, run the following command:
    ```
    pipenv --venv
    ```

2. Add virtual environments path to IDE settings (VSC example):
    - `Ctrl + ,` to access Settings
    - Search for `python.venvFolders` setting
    - Add the path up until `./.virtualenvs` (like in the screenshot below)


	![interpreter sc](https://user-images.githubusercontent.com/73730027/220026762-c33726cb-7517-48dd-8196-c63abb8c8337.png)

3. Change the Python interpreter (so your code knows where to find the packages you installed)
   - Ctlr + Shift + P
   - Select the options 'Python: Select Interpreter'
   - Select 'Enter interpreter path'
   - Select 'Find...'
   - Choose `.../<weird-virtual-environment-name>/Scripts/python.exe` as your interpreter
   
		![path sc](https://user-images.githubusercontent.com/73730027/220030895-87a600d9-4dc1-4685-8dac-91be2b41509e.png)

# Start server
On development mode: <br>
(make sure to check if the virtual environment is activated)
```
python -m app
```

On production mode: 

  (working on a command for this one)


# Pushing your code
After the setup is complete, go to the `development` branch and create a new branch to develop new features.

Everyone will ALWAYS merge the branches into `development`, never straight to `main`.

Feel free to fork the repo and make a Pull Request as well :)


