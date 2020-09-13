/**
  * @file client.c
  * @author Tejas Pidkalwar 
  * @date 27th August 2020
  * @file This file contains the TCP/IP client code implemented using 
  *         Linux/unix socket libraries.
  */


#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

// The server IP in the string format
#define SERVER_IP "94.142.241.111"
// Port number to use particular protocol application. In current case,
// port 23 signifies Telnet applciation
#define PORT_NO 23

int main()
{
   int socket_fd = 0, valRead;
   struct sockaddr_in serv_addr;
   char buffer[255] = {0};
   
   // Create the socket for TCP communication and get the corresponding file
   //  descriptor.
   // AF_INET parameter indicates IPv4 address family. 
   // SOCK_STREAM indicates TCP communication protocol.
   // 0 paramter is default for TCP
   if((socket_fd = socket(AF_INET, SOCK_STREAM, 0)) <= 0)
   {
      perror("Socket Failed");
      exit(1);
   }
   
   // update the socket address parameters
   serv_addr.sin_family = AF_INET;
   serv_addr.sin_port = htons(PORT_NO);
   
   // Convert string format ip address to binary format in IPv4 formatting  
   if(inet_pton(AF_INET, SERVER_IP, &serv_addr.sin_addr) <= 0)
   {
      perror("Invalid Address and not supported");
      exit(1);
   }
   
   // Attempt to make connection with given server address
   if(connect(socket_fd, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) < 0)
   {
      perror("Connection Failed");
      exit(1);
   }
   
   // Read the input from server untill we get updates from server.
   while(1)
   {
      bzero(buffer, 1024);
      valRead = read(socket_fd, buffer, 255);
      // If failed to read, exit from the read loop
      if(valRead < 0)
      {
         perror("Error Reading");
         break;
      }         
      printf("%s", buffer);
   }
   
   //close the socket connection
   close(socket_fd);
}

