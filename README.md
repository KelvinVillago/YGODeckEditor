# Yu-Gi-Oh Flask Application
This application creates the database for the Deck Editor app to use. The API is hosted using Render.com which allows for anyone to access the database
* https://ygo-deck-editor.onrender.com - The Flask application hosted on Render.com. 

### Description
This application allows for the database to have API routes to help the deck editor application. These routes allow access to parts of the database to store both User and Deck information.

The User table stores this information: 
* First Name
* Last Name
* Email 
* Encrypted password
* Authentication token 
* Token expiration date

The Deck table stores this information:
* Deck name
* Main deck
* Extra Deck
* Side Deck
* Date Created
* Reference to User table as creator of deck
#### Note: The main, extra, and side decks are stored as a string that includes comma seperated id's. This allows for the deck editor app to download the decks into a text file

### Routes
* '/token' - Needs a login. Returns the logged in user's token and token expiration
* '/users' - Returns all users in the form of a dictionary. Allows for POST and GET methods
* '/decks' - Returns all decks in the forms of a dictionary. Allows for POST and GET methods
* '/decks/<num_id>' - Return the deck with that id as a dictionary. Allows for GET, PUT, and DELETE Methods
* '/users/me' - Gets current user from token. Allowws for GET, DELETE and PUT methods

