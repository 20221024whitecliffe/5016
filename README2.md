# Help Desk Ticketing System
<!--- This file includes software manual, the development status, licence, versions, installation and maintenance information --->
This Help Desk Ticketing System is developed for xxx to be used for internal help desk ticket registration and management. It allows service desk employees to manage service tickets, staffs to fetch new password and register their problems into service tickets. 

## Prerequisites
Before you start using the system, ensure you have met the following requirements:
<!--- These may not be a full list, enquire your service desk if you are unsure --->
* You have installed the latest version of python
* You have a Windows/Linux/Mac machine. Supported operation system are Windows 11, MacOS.
* You have read this file.

## Installing Help Desk Ticketing System
To install Help Desk Ticketing System, follow these steps:

```
Linux and macOS:
```
* Go to directory workstation/xxx/helpdesk
* Drag helpdesk.dmg into your directory desktop
* Double click after it is copied to your machine
* Use default setting to install

```
Windows:
```
* Go to directory workstation/xxx/helpdesk
* Drag helpdesk.exe into your directory desktop
* Double click after it is copied to your machine
* Use default setting to install
```
## Using Help Desk Ticketing System
To use Help Desk Ticketing System, follow these steps:
```
* Double click the icon to start the software
* Choose your answer in displayed menu
>Select from the following choices:
>0: Exit
>1: Submit helpdesk ticket
>2: Show all tickets
>3: Respond to ticket by number
>4: Re-open resolved ticket
>5: Display ticket stats
* When you choose 0, the software will be closed
* When you choose 1, you will need to input information of 
>your name
>your staff id
>your email address
>description of the problem
* With all the information provided, the software will automatically register the ticket and assign a ticket number
* If your want to change your password, type "Password change" in description of the problem. It is not case sensitive, 
but you do need to follow the format to type space in between the two words.
* Password change is an automatic function, and it is created from your staff id and your name
* When you choose 2, all the tickets will be displayed.
* When you choose 3, it will ask you to type ticket number to access the ticket to update responses
* When you choose 4, it will display the list of resolved tickets and allow you to change the ticket status back to open
* When you choose 5, it will generate a stats of all the tickets.
```
## Data types
<!--- The data types gives an indication on required user input that should be made. Invalid data input may interrupt the software functionality--->
To clarify required user input type, refer to this list:
* choice numbers: 0 to 5 integers
* name: strings, numbers, space, signs are accepted, while strings are preferred. no requirement on length
* staff id: strings, numbers, space, signs are accepted, while 4 digits integer numbers are preffered
* email address: strings, numbers, space, signs are all accepted, please follow format of email address using "@" 
* description of problem: brief description is prefered. strings, numbers, space, sign are all accepted.
when password change is required, please type "Password change".

## Maintenance
Please enquire your service team for maintenance

## Development Status
Publishing date: 5. 12. 2022```
The software is under trial use stage. Feedback is welcomed. ```
Report problems and bugs to ```
20221024@mywhitecliffe.com

## Version control
Help Desk Ticking System 1.0

## Contributors
Thanks to the following people who have contributed to this project:
* Whitecliff.com
* Asra Khalid
* Lucia Chen and the family

## Contact
WhiteCliff.com```
Lucia Chen```
Phone: 021111111```
Email: 20221024@mywhitecliffe.com```