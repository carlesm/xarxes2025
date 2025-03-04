# Practica de Xarxes 2025

Repositori amb exemples per la pràctica de Xarxes 2025 / UdL.



# Developing with poetry

If you have poetry installed on your machine (I recommend using it with pyenv to have recent python versions without affecting the system),
you can get the code (checkout from git or unzip the file).

## Update dependencies

Inside the main directory:

poetry sync 

This will update the dependencies and install the libraries and this package.


## Run python or code

You can run with the virtual environment with poetry:

poetry run <command>

For example:

poetry run python 

Will run a python installment with the libraries you have added (click, loguru, Pillow, etc.)

Or, as it is configured the sample of code:

poetry run xarxes2025

Will run my code. 

If you have to add libraries, you can use:

poetry add <libname>

All libraries you add, ask first.


# Code

You have, in src/*py all the code. 

There you have:

- cli.py  - Code to start server or client. Processes command line arguments with click.
- server.py - Code for the server.
- client.py - Code for the client, includes a minimal UI in TK. 
- udpdatagram.py - Code to create an RTP datagram. Has missing code (gives error). You have to finish it.
- videoprocessor.py - Code to process a videofile and encode it as a frame image. To be used for the project.




# MAC OS/X Special considerations

Weirdly enough, Mac OS/X has a limit for UDP datagrams of:

9216

Solve it with:

sudo sysctl -w net.inet.udp.maxdgram=65535

This is a temporary fix, next reboot, solve it again.
