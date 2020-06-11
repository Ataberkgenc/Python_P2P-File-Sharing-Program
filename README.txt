This is a simple file sharing program written in Python 3. Program works with HAMACHI, you can easily re edit the code for using in the Local Area Network.

The program can run on all different OS's.

GENERAL REQUIREMENTS:

1) Python 3 must be installed before running the program.

===================================================================================================================================

The program runs in all different OS's (eg. Windows, Mac, Linux.)

===================================================================================================================================

YOU NEED TO RE EDİT THE CODE.
YOU NEED TO ENTER YOUR OWN HAMACHİ IPv4 ADDRESSES TO THE STATED FİELDS
FİELDS ARE STATED İN CODE. 

===================================================================================================================================

TO RUN THE PROGRAM:

1) Put the file that you want to share to the same directory with the program files.

2) Run P2P_Server. It will ask you to enter which file you want to share. Enter your file's name correctly then press enter. 
   If you are about to share a text file called 1, you need to enter "1.txt". With different words, you need to enter the 
   file name and it's an extension. 
   (eg. A jpg formatted picture called photo must be entered as you see => Enter file path: photo.jpg )

3) Run the Service_listener. No other things needed.

4) Run the Service_announcer. It will ask you to enter a username. Enter a username that you want. It's all up to you.

5) When you have started the Service_announcer go to service listener and wait until a successful connection.
   If you see => Received Username - "Your peer's username" This is a successful connection, you can run the P2P_Server. 
   If you can't see the Received Username wait until you get that message. The announcer will announce itself in 60 second periods.
   Just wait for the next announcements until you get the message.

6) Run the P2P_Client. It will show you the files that owned by every IP addresses like this
   IP Address: "Your peer's IP address" File Name: "Your peer's file name"
   Then, it will ask you to enter the file name that you want to download in this way: Enter File Name = 
   You need to enter the file name that you want to download as you have entered in P2P_Server.
   (eg. If you want to download a jpg formatted picture called a photo, you must enter like => Enter File Name: "photo.jpg" )
   P2P_Client will warn you if there was an error.

7)  If there is no error, you can find the downloaded file in the Program's folder as under the downloads file folder.


Extras:

You can see users in users.txt file in the same directory. 
server_success.txt and server_files folder show the successful announcements of your file.
client_success.txt shows the successful announcements of your peer's files.
