# Welcome

This is a lab oriented repository for bite sized python courses.



>[!TIP]
>Remember, if you cloned the repository, you can always revert to the original state 

## Forking the repository
This is a public repository, so you can fork it without any restrictions.
Everything is done in github, so it's assumed you have a github account.

To fork the repository:
1. Navigate to the repository in github (this page)
2. Click the "Fork" button in the top right corner
3. Done!

You just made a `photocopy` of the today's state of the repository in your github account.


## Cloning the repository

To clone the repository:

1. Open a terminal
2. Navigate to the directory where you want to clone the repository
3. Run the following command:

```bash
# Replace `<username>` with your github username.
git clone https://github.com/<username>/simple-echo.git
```
or if you have not forked the repository:

```bash
git clone https://github.com/vesnikos/simple-echo.git
```

## Creating a virtual environment

You should create a virtual environment for each course. 

Virtual environments not only keep your system clean, but also are throwaway. 
If you mess up, you can just delete the virtual environment and start over.

To create a virtual environment:

1. Navigate to the repository directory
2. Run the following command:

```bash
# Replace `<course>` with the course name.
## windows
py -m venv .venv --prompt simple-echo

## MacOS/Linux
python3 -m venv .venv --prompt simple-echo
```

### Activating/Deactivating the virtual environment

To activate the virtual environment:

~~~bash
# Windows
.venv\Scripts\activate
## MacOS/Linux
source .venv/bin/activate
~~~

>[!Note]
>Remember to activate the virtual environment before running any python commands.

### Deactivating the virtual environment
~~~bash
deactivate
~~~

## Install the code to the virtual environment

>[!Warning]
>Remember to activate the virtual environment before running the following commands.

You can install the code to your active python environment:

```bash
py -m pip install -e .
```
>[!Note]
> The `-e` flag installs the code in "editable" mode, so you can modify the code and see the changes immediately.


After the operation is complete, in your system you should have a new command `simple-echo`.

If you see the expected output, you are ready to start the course.

~~~bash
> simple-echo --help
Usage: simple-echo [OPTIONS] COMMAND [ARGS]...

  A simple echo program.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  circle-details     Calculate details of a circle.
  get-average        Print the average of a pandas DataFrame.
  get-random-number  Print a random number.

  (c) 2025 by the simple_echo project
~~~