"""Entries to populate the jinja templates"""

ENTRIES = [
    {
        "id": 32,
        "title": "Day 32",
        "creation_date":"2017-11-04T17:54:04.376599",
        "body":"Struggle bus with Django"
    },
    {
        "id": 15,
        "title": "Day 15",
        "creation_date":"2017-11-04T17:54:04.376599",
        "body":"Today I learned about templates. Using jinja and setting data to populate the templates is pretty much like handlebars. A weird transition because of the having to end and sort of block, loop, or condition, but still pretty cool."
    },
    {
        "id": 14,
        "title": "Day 14",
        "creation_date":"2017-11-02T22:33:30.620620",
        "body":"Today I learned about graphs. Making Edges/vertices, loops, adding an node to detect loops and that a graph can be 3D."
    },
    {
        "id": 13,
        "title": "Day 13",
        "creation_date": "2017-11-01T20:40:46.984614",
        "body": "Don't push up for access key/route for your database. Reassign in your profile locally so it is hidden, so hacker's can't hack."
    },
    {
        "id": 12,
        "title": "Day 12",
        "creation_date": "2017-11-01T03:10:11.160578",
        "body": "Jinja2 - Whenever you open any sort of functionality you have to end it. {% if %}{% endif %}"
    },
    {
        "id": 11,
        "title": "Day 11",
        "creation_date": "2017-10-30T23:06:37.567997",
        "body": "Pyramid - is a framework for server with the help of cookiecutter. Cookiecutter creates the scaffold. It gives you a goto template that gives you the basic functionality of the server. It builds out the Pyramid application."
    },
    {
        "id": 10,
        "title": "Day 10",
        "creation_date": "2017-10-27T22:03:43.777984",
        "body": "The major thing I learned today was fixtures. We had an intro into them but to see how they were used, how to set up a fixtures was amazing. Pretty much set it up like a function to give you a desired data set and manipulate it however you want. If you want 3 nodes in a list, create a fixture. It is going to save you time and money."
    },
    {
        "id": 9,
        "title": "Day 9",
        "creation_date": "2017-10-26T20:16:52.916439",
        "body": "Python works in a single thread and is a blocked language. Meaning that it reads by one line and if a line doesn't finish executing then it stops the program form reading the next line.\nMulti-threading is using more than 1 line.\nQueues - have 4 methods. enqueue, dequeue, peek, and size. \nQueues work in a FIFO order, meaning First In First Out."
    },
    {
        "id": 8,
        "title": "Day 8",
        "creation_date": "2017-10-25T20:12:08.201383",
        "body": "Doubly Linked List is the same thing as a Singly Linked List but can be read in both direction using the .prev method on the DLL. \nYou can import your pytest into a fixture to automate your testing and not have to write as much.\nStatic Methods are really not required or have no use because we can just set global."
    },
    {
        "id": 7,
        "title": "Day 7",
        "creation_date": "2017-10-24T20:37:57.289614",
        "body": "Learned about Stacks - FILO which is first in last out. I like to think of it like a stack of plates.\nFormat date by importing in email.utils then format the date string using\n 'Date {}'.format(email.utils.formatdate(usegmt=True))\n\\r\\n = This is a carriage returned. It is used to format HTTP responses correctly and fully."
    },
    {
        "id": 6,
        "title": "Day 6",
        "creation_date": "2017-10-23T20:22:36.709793",
        "body": "I know about the OSI model but actually seeing the TCP/IP in the Transport layer was a cool implementation. Setting up server with socket and listening on was different and seemed to have a few extra steps than JS.\nSingly linked list - Head is sole to the head of the list. The .next property points to the following nodes and then finally the last node points to none."
    },
    {
        "id": 5,
        "title": "Day 5",
        "creation_date": "2017-10-21T23:35:25.846072",
        "body": "Sure has been a day of coding so far. Running through all the various katas and trying out different methods really has pushed me to use the notes and google to try to burn basic Python methods in my brain. List, str, index, and [:] have been my most used for today. Starting to feel stronger about Python."
    },
    {
        "id": 4,
        "title": "Day 4 - What I learned",
        "creation_date": "2017-10-20T19:18:10.167461",
        "body": "Today I learned an assortment of things. I watched the so you think you can PDB and learned basic commands and interactions inside the terminal. Like list, you can list lines of code but you have to be explicit.\nTox is a package that allows us to run test in both python2 and python3. After installing tox you create a tox.ini file where you set dependencies. I view it kind of like a package.json file."
    },
    {
        "id": 3,
        "title": "Day 3",
        "creation_date": "2017-10-19T20:50:45.809508",
        "body": "Learning about dictionaries and the specifics. You can't loop through an dict but you can iterate through the keys.\nReaffirming with --- as --- and understand what is going on with the assignment.\nUsing io and os to read/write files."
    },
    {
        "id": 2,
        "title": "Day 2",
        "creation_date": "2017-10-18T15:53:39.084668",
        "body": "<h1>Python Reading Journal</h1>\n<h2>Day 1 - 17 OCT 17</h2>\nReviewing recursion, loops, imports TDD on my own time because I was out of town this day was good for me. I know how it's down in Javsacript and to see that the ideas are the same but the implentation in Python with Python's syntax was very helpful.\nImporting is the most tricky concept today. JS you would just require the component out of the module or the everything. It will take me a little bit to get use to Python's syntax for it."
    },
    {
        "id": 1,
        "title": "Day 1",
        "creation_date": "2017-10-18T15:53:08.620614",
        "body": "I saw the sites in Boston. Well some of them, and when I came back. Was in a nice overview and review of booleans, basics, syntax and so fourth."
    }
]
