# vididgen
Experimental YouTube video URL generation program, written in Python. Very ineffective unless someone handles reverse engineering the IDs somehow

# Why is vididgen ineffective?
Simple, the address space of a YouTube video's ID can include any of 73,786,976,294,838,206,464 videos, and obviously, there are not 73,786,976,294,838,206,464 videos. Trying to reverse engineer video IDs led me nowhere; I thought there was perhaps some sort of pattern in another encoding scheme, or the data itself can be represented as a sequential number you can just convert to special Base64, but that will not work. Also, I have not integrated GPU acceleration or GPU cluster support for you to rapidly generate such URLs, you're running at a theoretical rate of 2 per second.

# What is vididgen for?

It's experimental more than anything. I shared it on GitHub for people to criticize my Yandare Sim code and maybe actually make it functional through people committing shit, made it when I was bored. If I had more money and I actually cared about it at all, I'd probably set up a domain or something that it sends valid YouTube IDs it generated to a site for some sort of rainbow-table type stuff or maybe just random gen blacklisting on the client side, not really sure how that'd work.

# How to use vididgen?

On all operating systems, it is pretty simple, simply clone or download the code and:

  On Windows: In CMD, navigate to vididgen directory, type `python -m pip install -r requirements.txt` and then double click on `YouTube URL Gen.py`
  On Linux (Debian based): Make and activate a venv (which you'll need to use every time you start vididgen) using `python3 -m venv venv` and `source venv/bin/activate`, and then `pip3 install -r requirements.txt` and `python3 YouTube*`.
  On MacOS: (Unknown, needs testing)

Happy internet spelunking, I suppose this could be adapted to other things, although with much more ease (like a random AliExpress numeric product URL generator)
