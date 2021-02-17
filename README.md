# test-data-gen

Repository to capture best practice tooling for Python based developments.

## Installation

To install this package in an existing Python project:

`pip install 

## Python development set up

The following steps are required to setup a suitable Python environment from first principles.

### Install Python

Install Python, the latest version can be downloaded from [python.org](https://www.python.org/downloads/)

Note - during the installation process choose the "Add Python X.X to PATH" option.

Check the installation by opening a terminal and running the following command:

`python --version`

### Install Git

Download and install Git from [the official Git web site](https://git-scm.com/downloads).

Check the installation of Git by running the following command:

`git --version`

There are some steps you need to take to [get started with Git](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

The core ones being setting your git user and email address, this is required for pushing changes to a remote repository:

`git config --global user.name "John Doe"`
`git config --global user.email johndoe@example.com`

### Install Visual Studio Code

If not already installed on your machine, download Visual Studio Code (VS Code) from the [Microsoft web site](https://code.visualstudio.com/download).

### Set up repository

The first step is to clone the GitHub project into which you want to import this this package.

From the local directory where we you want to host your repos, such as `cd %HOMEPATH%\repos` run the following command:

`git clone <GitHub URL for repository>`

### Launch Visual Studio Code

If not already installed on your machine, download Visual Studio Code (VS Code) from the [Microsoft web site](https://code.visualstudio.com/download).

Change directory to the repo cloned above.  Launch VS Code from this directory:

`code .`

Once VS Code launches, open a terminal and following steps.

#### Set up environment

Use 'pip' (pacakge installer for Python) to upgrade to the latest version of pip:

`python -m pip install --upgrade pip`

Now install 'pipenv':

`pip install pipenv`

Now lauch 'pipenv' shell - this will auotmatically create virtual environment:

`pipenv shell`

Now install dependencies using the `--dev` extensions so that development packages such as pytest, flake8 and the packaing tools are included.

`pipenv install --dev`

The following commands are useful to visualise the packages that are installed and the dependencies between them:

`pipenv graph`
`pipend graph --reverse`

## End notes

The following files were added to the vanilla repo to set it up as a Python package:

- **setup.py** - contains the meta data required to package up the modules as a Python package;
- **setup.cfg** - configures tools such as pytest and flake8;
