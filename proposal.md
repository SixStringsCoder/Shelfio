

![The Shelf where collectibles are presented](images/custom_collection2.jpeg)

### Capstone Proposal 2017<br>by Steve Hanlon



# Custom Collections
###### Alternative product name list
- Clickable Collectibles
- Here's My Case
- Love Set Match
- Pack Rat
- Collect-N-spect


### Product Overview

- Create <strong>Custom Collections</strong> to showcase comic books, book collections, music collections, stamps, coins, pictures, videos or even data collections!  Share any Collection using a direct link to that stored Collection or embed it in another webpage.

<strong>Opening Screen to create a new collection or view other collections already created</strong>
![Opening Home Screen](images/open_screen2.jpeg)
<br><br>

- The user creates a Collection's <em>Presentation Window</em> by using Drag-n-Drop form fields to enter details about the Collection, upload an ID icon plus add audio/video connected to the <em>Collectibles</em>.  This <em>Presentation Window</em> will show up as a <em>Modal Window</em> in the browser after the Collectible image icon is clicked.

<strong>UI to build modal Presentation Window template</strong>
![The template area to build your modal-window presentation](images/build_form3.jpeg)

<strong>Here is a sample Pres. template</strong>
![A sample of how the template can be shaped using an eBook collection](images/build_form_sample2.jpeg)
<br><br>

- Each collectible is represented by a picture ID icon (uploaded by the user) and these icons are gathered in a <em>Styled Background</em> area (e.g. a bookshelf for a book collection, a stamp book for stamp collection, etc.) when user is viewing a given complete Collection.

<strong>A sample template using an eBook collection.  After filling it out and attaching links to buttons, click "Add to Collection".</strong>
![A sample of how the template can be shaped using an eBook collection](images/collectible_entry2.jpeg)

<strong>Collectible Added.  Continue to enter in more Collectibles or use Menu icon in corner to see that eBook Collection, go to other collections or to Home Page.</strong>
![Success Message message with option to continue adding more or going to other page via menu icon](images/build_form_success.jpeg)



<strong>View of eBook Collection</strong>
![Here's a view of eBook collection](images/eBook_collection2.jpeg)
<br><br>

- When a picture is clicked, Presentation modal window opens to display details, linked buttons and related sites.

![Here's a sample of a Presentation Modal Window](images/pres_window.jpeg)
<br><br>

- Share the weblink to this Collection for others to view this webpage or copy the embed code (example below) to display the collection with <em>Styled Background</em> in any webpage.

<strong>Embed code allows this Collection to show up on another website</strong>
![Embed code Collection  view sample](images/embed.jpeg)

<strong>Same <em>Presentation Window</em> functionality when an icon is clicked.</strong>
![Embed code Modal Window  sample](images/embed_popUp.jpeg "Presentation Modal Window")
<br><br><br><br>


### Site Tree and Specific Functionality

Spend some time drawing out on paper mockups _every_ page of your MVP site.
Annotate _every_ component of the interface _every_ action the user can take.

<strong>Website Tree</strong> (separate webpages bolded in white)
- <strong>Home Page</strong> with Simple Full-screen layout
  - two buttons on Home Page to CREATE and VIEW
    - Create a Collection click leads to:
      - <strong><em>Presentation Window</em> UI Builder</strong> then to...
      - <strong><em>Add to Collection</em> </strong>webpage
    - View saved collections (e.g. <em>All My Collections</em>) click leads to:
      - <strong><em>Collection</em> "shelf" webpage</strong> with clickable Collectible icons as well as Share and Embed buttons
        - Icon click shows Presentation Window revealing a collectible's details. Close this window by clicking "X".
        - Share button copies webpage URL to clipboard and shows message "Collection link copied to clipboard"
        - Embed button copies script embed code to clipboard then shows message "Collection embed code copied to clipboard"




If there is any actions your app needs to take in the background describe _each_ of them and how they change the underlying data your app saves.s

**Pick the minimum feature set for your product to work.**
Everything else should go in the "further work" section.

You don't have to submit the mockup drawings, but do write out a description of _every_ page and component and action.
I literally mean _every_.

### Data Model

What are the persistent "nouns" you need to save across pages in your project MVP?
What do they represent?

We'll be using a relational database which models things like a spreadsheet.
There are fixed fields and every instance

How do you need to _search_ for specific instances of nouns?

### Technical Components

What are the "moving parts" of your MVP?
What are the things like "modules" you're going to write?
How do they talk to each other?

_Make decisions_ here and now.
Do research and prototyping to figure out what libraries and technologies will help you solve your problems.
Write up which ones you'll use.
It's okay if they end up not working and you have to change your plans.

This is _more specific_ than "Django backend, CSS style, etc."
Please specify what specific technical problems you'll have to solve and a guess at the solution.

### Schedule

Write out the order in which you will tackle your technical components of your MVP.

What are the easy parts?
What are the hard parts?
Can you guess how long you'll take for each?

Work on the tough and crucial parts first.

### Further Work

All of the above parts are _just addressing your MVP_.
Here you should outline other features you'd like to implement if you get "done" early.
Order them by importance towards your high-level goal and what order you'll work on them later.

Don't work on any of these features until **all of MVP is complete**.

## Submission

Create a _new_ git repo based on your project name [in GitHub](https://github.com/new).
Init that repository with a readme.
Write up your proposal as `proposal.md` and link to it from the readme.
I don't care that you learn all of the fancy parts of [writing Markdown documentation](https://help.github.com/articles/basic-writing-and-formatting-syntax/), but just get some basic sections that follow the rubric above.

Email me the URL to your capstone repo on GitHub before the proposal is due.
