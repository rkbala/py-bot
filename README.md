# py-bot

Messing around with the Python SDK for the Bot Framework.

* main.py => Echo Bot from the Wiki

## Running this code

There's barely anything in this repository, so I'm not sure why you would want to clone and run it just yet, but okay...

### Installation

Make sure you have Python installed (obviously). I recommend the Anaconda distribution, as it comes a lot of the mathematic, data science, and machine learning libraries used for artificial intelligence.

#### Cloning and Virtual Environment

Clone this repository:

    git clone https://github.com/szul/py-bot.git

Python recommends using virtual environments to keep your dependencies coupled to your code rather than polluting the global namespace.

    cd py-bot
    python -mvenv .\

Now you have a virtual environment set up in the `py-bot` directory. Don't do anything with it just yet.

The Python SDK is experimental, so you're going to have to build it from the source.

Clone the `botbuilder-python` repository:

    cd ..\
    git clone https://github.com/Microsoft/botbuilder-python

> Note that I moved outside of the `py-bot` directory. I put the `py-bot` working directory and the `botbuilder-python` directory at the same level in the filesystem to make it easier to navigate and document.

There are couple of things that you'll want to do global, because you're going to need them in your Python workflow anyway. You should already have `pip` installed, since it hopefully came with your distribution of Python. Now you need to install `wheel` and make sure a few other libraries are up-to-date.

    pip install wheel
    python -m pip install --upgrade pip setuptools wheel

> If these utilities are not up-to-date, you make get an error when attempting to install the botbuilder output. The most common error is one that doesn't recognize `bdist_wheel`

Now that your Python environment is up-to-date, you will need to build the botbuilder SDK.

    cd botbuilder-python\libraries\botbuilder-schema
    python setup.py bdist_wheel

    cd ..\botframework-connector
    python setup.py bdist_wheel

    cd ..\botbuilder-core
    python setup.py bdist_wheel

Once built, you can install the botbuilder library, but you will want to do that in the virtual environment.

First, go back to the root of the `py-bot` project, and activate your virtual environment:

    ./Scripts/activate

Then install the botbuilder library:

    pip install ..\botbuilder-python\botbuilder-core\dist\botbuilder_core-4.0.0a0-py3-none-any.whl
