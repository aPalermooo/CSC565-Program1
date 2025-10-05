# Socket Programming Assignment 1
*Xander Palermo : ajp2s@missouristate.edu*

CSC565 Computer Networking

__6 October 2025__


## Table of Contents
- [File Description](#file-description)
- [Compilation and Execution](#compilation-and-execution)
- [Protocol Description](#protocol-description)
- [Limitations](#limitations)

## File Description

### Share
 
These files are contained separately as they contain logic that is shared between UDP and
TCP implementations of clients and servers.

#### Share/Message

A dataclass that encapsulates all information needed for the functionality of the custom Protocol used by client and servers to communicate.

More information about this is located in [Protocol Description](#protocol-description)

#### Share/ClientFunction

Contains all working logic that is used by Client.
The functions contained within this file are used for validating user input, and logging information to the console.

#### Share/ServerFunction

Contains the function that processes the conversion of units that the server performs.
The function is able to break down a message and create a new one to return to the client based on the query requested.

The server assumes that the input is always clean from clients, since the 
validation checks are performed by the client before it creates a query. Therefore, the server has few checks to handle errors if someone one where to arise.

### UDP 

#### UDPClient

Creates a shell environment that parses commands and interprets them to send to the corresponding UDP server.
When the server responds, the Client will relay the server output back to the user
The following command is supported in the shell

> (env) $ Convert \<server-IP\> \<value> \<units> \<conversion>

The user is continuously prompted to enter a command until they enter the terminate command

> (env) $ exit

If the server cannot be reached, the user is prompted to check the server's status and try again.

Inputs are validated by the client before they are sent to the server. If an input is invalid or does not make logical sense (such as a negative distance)
the query will be rejected and the user must enter their query again.

#### UDPServer

Applies conversion rates to user provided queries and returns message back to use with the updated value.
Packets received and process will have their contents and their sender's IP logged to console output

### TCP

#### TCPClient

Creates a shell environment that parses commands and interprets them to send to the corresponding TCP server.
When the server responds, the Client will relay the server output back to the user
The following command is supported in the shell

> (env) $ Convert \<server-IP\> \<value> \<units> \<conversion>

The user is continuously prompted to enter a command until they enter the terminate command

> (env) $ exit

If the server cannot be reached, the user is prompted to check the server's status and try again.

Inputs are validated by the client before they are sent to the server. If an input is invalid or does not make logical sense (such as a negative distance)
the query will be rejected and the user must enter their query again.

### TCPServer

Applies conversion rates to user provided queries and returns message back to use with the updated value.
Packets received and process will have their contents and their sender's IP logged to console output

## Compilation and Execution

### Required Files

All required files are contained within the submitted .zip file. The program can also be installed by the command:

> git clone https://github.com/aPalermooo/CSC565-Program1

Servers can be initiated by calling their file name using the python3 interpreter

### Initiating Client and Server

> python3 UDPServer.py
> 
or
>python3 TCPServer.py
> 
The custom client shell can be accessed using a similar command on the client python files
>python3 UDPClient.py
> 
or
>python3 TCPClient.py
> 
For correct functionality, only connect UDP client with a UDP server, and a TCP client with a TCP server.

### Usage

The command to issue a query to the server from the client for both UDP and TCP versions is

> (env) $ Convert \<server-IP\> \<value> \<units> \<conversion>
>
> ex: Convert 122.0.0.1 100 C F
> 
localhost can be used in place of an IPv4 if the client and server are both being run on the same system

>ex: Convert localhost 100 C F
> 
### Exiting

#### Exit client

To exit the client, just send the terminate command to the shell

> exit
> 
#### Exit Server
To exit the server, you must send a manual keyboard interrupt (Ctrl+C) or kill the process using a command such as kill -9

## Sample Output

Sample input and output are contained in the sample directory

These sample inputs and outputs were generated using localhost on the Missouri State University lovelace server

## Protocol Description

The custom protocol designed to facilitate the data transfer between client and server is contained in the Message.py file in the share folder
The message contains 2 fields for a header, and a body of one data type

```
+-------------------+-------------------+-------------------+
|   "Header":                           |   "Destination"   |
|    [ Conversion_type, in_Metric ]     |                   |
+-------------------+-------------------+-------------------+
|                  "Content" (Value)                        |
+-----------------------------------------------------------+
```

To transfer the protocol from client to server and vice versa, the pickle library is used to encode and decode the message object, so it can be sent as a bytestream.

### Header

The header contains all the data that is required for the identification of what the packet contains for the server.
The packet also contains routing information for the location of the server that the client will attempt to content.

#### Header Field

This field contains a description of what the message is holding. It contains an integer representation of what type of conversion the user
wants to perform in the first field. The table of this representation is below:

- 1 : Distance ( km <--> mi )
- 2 : Weight (kg <--> lb)
- 3 : Temperature ( Celsius <--> Fahrenheit)

The second field describes if the value contained in the content field is in the metric form of the unit (as in km, kg, or degrees C)

#### Destination

This field is only used by the client. Since the server will always send the message back to the system that sent it. (This field will be unchanged by the server in its modifed version of the message)

It contains the IPv4 address of the server, or "localhost" is the server is located on the same system as the host.

### Content 

This contains a float that represents 1 of 2 things.

When the server receives a message, it will interpret the content field as the value to perform the conversion on. The manipulated value will then be placed in a new message object and returned to the client.

When the client receives a message, it will be interpreted as the converted value.

## Limitations

All files were tested for functionality using localhost on the missouri state lovelace servers.

### Server Location Limitations

In the current state of the program, the program can only accept
IPv4 addresses and the keyword "localhost" (which sets the ip address to the computer that is executing the script).
This means that hostnames such as "myserver.mynet.com" are considered invalid by the program. This is because the regex that validates the server name
will only check for 4 clusters of 1-3 digits followed by a dots ( ex "255.255.255.255" or "1.1.1.1" )

### Code Formatting Limitations

Another Limitation is there is more work to be done refactoring code. 
There is more functionality that is shared between Clients and Servers that can be refactored to their own files for better future maintainability of the codebase
(An example being the custom shell that prompts users for the **Convert** command).

If given more time, I would also update the message headers so that the destination is handled better in the Message, or is just handled independently by server and client and removed from the message.

### Security Liabilities

This program uses pickling to encode and decode objects sent over TCP and UDP traffic. This traffic is not encrypted and not checked. This brings in security risks such as interception of the message, as it is very easy to encode back into the message protocol.
This form also could allow malicious attacks on the server, as an attacker could create a pickle encoding that could crash or cause undeterministic behavior in the server.