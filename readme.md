# Xiao Ming

## Web based Patient Database

Stack:
 * python
 * Flask
 * MySQL
 * Bootstrap
 * HTML
 * CSS
 * [NodesJS](https://nodejs.org/en/)

### Quick Tutorial of Python Virtual Environment `virtualenv`
`pip3` provides a simple way of adding new functionality to your projects by downloading packages and install them on your computer, which we can them `import` in python scripts. However, one package may need other packages to be able to work, so `pip3` will also install extra packages that the `import`ed package is dependent on.

 Sometimes two packages will depened on the same parent package but one may need a different version to the other. This can cause problems because newer version will override older version. One package may end up with errors at runtime. We need a way to isolate packages and their dependencies.

 `virtualenv` is created for this purpose.
 Install with command:

    sudo pip3 install virtualenv

`virtualenv` works by creating a local folder with a copy of the python installation we have on the machine. When we run `pip3 install`, the packages will be installed in the local folder. We can create an environment for each python project, each project will have its own environment to execute python code from.

Step 0: make a folder which will contain our project

    mkdir project-name
    cd project-name

Step 1: Create an environment 

    virtualenv -p python3 .

Step 2: activate the environment

    source bin/activate

The terminal prompt will change to (project-name) when you activate a `virtualenv`

Step 3: install packages

    pip3 install nose2 flask sqlalchemy

**Notice** you don't put `sudo` before `pip3 install`

Last step: Deactiave the environment 

    deactivate

Deactiving restores python environment to system python. The terminal prompt will no longer have (project-name). Or you can close the terminal.


## Getting started with Python and Flask for Web Development

### Local Machine Setup

Before we can begin develop on a local machine, we need to make sure all the required software are installed.

* Python 3.x
* Latest Browser: Chrome/Firefox/Edge
* MySQL
* python package: `virtualenv`
* Code Editor: Visual Studio Code (recommended)
* NodeJS 

**Special notes for MacOS users:** [homebrew](https://brew.sh/) is highly recommended as package manager on MacOS.

To install homebrew, execute the following bash command:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"


If you already have homebrew you can install python3 and MySQL by executing:

    brew install mysql python

### Step up database (MySQL)

For development, a local SQLite database is sufficient

## Frontend
To keep it simple, we will start with Bootstrap and jQuery. If more dynamic features are needed, we will migrate to ReactJS.


## Setup Server Side Development Environment

step 1: Make a folder and create a new `virtualenv`

    mkdir xiao-ming-project
    cd xiao-ming-project
    virtualenv -p python3 .
    source bin/activate

step 2: check out code from source control

    git clone https://github.com/xiao-ming-team/xiao-ming

step 3: Install dependencies

    cd xiao-ming
    pip3 install -r requirements.txt

## Setup Client Side Development Environment

TBC