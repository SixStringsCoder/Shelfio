

![The Shelf where collectibles are presented](docs/images/custom_collection3.jpeg)

### Capstone Proposal 2017<br>by Steve Hanlon



# Shelfio
###### Alternative product name list
- Clickable Collectibles
- Pack Rat
- Collect-N-spect
- Shelfio or sHelpio
- Amphora
- Decluttero


### Product Overview

- Create <strong>Custom Collections</strong> to showcase comic books, book collections, music collections, stamps, coins, pictures, videos or even data collections!  Share any Collection using a direct link to that stored Collection or embed it in another webpage.

<strong><a name="samp1">Opening Screen to create a new collection or view other collections already created</a></strong>
![Opening Home Screen](docs/images/open_screen2.jpeg)
sample picture 1
<br><br>

- The user creates a Collection's <em>Presentation Window</em> using form fields to enter details about the Collection as well as uploading an "ID" icon connected to a <em>Collectible item</em>.  This <em>Presentation Window</em> will show up as a <em>Modal Window</em> in the browser after the Collectible ID image icon is clicked.

<strong><a name="samp2">UI to build modal Presentation Window template<</a>/strong>
![The template area to build your modal-window presentation](docs/images/build_form4.jpeg)
sample picture 2

<strong><a name="samp3">Here is a sample form template built by a user to enter data and represent the layout in the Modal Window. Click <em>Save Layout</em> button to Save this layout to the Collection.</a></strong>
![A sample of how the template can be shaped using an eBook collection](docs/images/build_form_sample4.jpeg)
sample picture 3
<br><br>

- Each Collectible is represented by a picture ID icon (uploaded by the user) and this icon, inserted in a <em>Styled Background</em> Collection area (see sample picture 6 - e.g. a bookshelf for a book collection, a stamp book for stamp collection, etc.) will act as the link to open the Modal Presentation Window revealing the Collectible's details entered in the form.

<strong><a name="samp4">A sample template using an example of an eBook collection.  After filling out the form and attaching links to the buttons and docs/images, the user clicks "Add to Collection."  
To add or remove form fields/buttons, the user can click the "Edit Layout" arriving back at the editing screen.</a></strong>
![A sample of how the template can be shaped using an eBook collection](docs/images/collectible_entry4.jpeg)
sample picture 4

<strong><a name="samp5">Collectible Added to <em>eBook Collection</em>.  Continue to enter in more Collectibles or use Menu icon in upper corner to view the <em>eBook Collection</em>, go to other collections or to Home Page.</a></strong>
![Success Message message with option to continue adding more or going to other page via menu icon](docs/images/collectible_success1.jpeg)
sample picture 5



<strong><a name="samp6">View of eBook Collection (Display View or Shelf View)</a></strong>
![Here's a view of eBook collection](docs/images/eBook_collection2.jpeg)
sample picture 6
<br><br>

- <strong><a name="samp7">When a picture icon is clicked, Presentation Modal Window opens to display details, linked buttons and related sites.</a></strong>
![Here's a sample of a Presentation Modal Window](docs/images/pres_window.jpeg)
sample picture 7
<br><br>

- <strong><a name="samp8">When the buttons at bottom of a Collection are clicked, they allow this Collection's webpage to be shared or embedded in other websites.</a>
![The buttons on the Collection webpage allow a user to share this collection.](docs/images/eBook_collection_btn.jpeg)
sample picture 8
<br><br>



- <strong><a name="samp9">Share the weblink to this Collection for others to view this webpage or copy the embed code (example below) to display the collection with <em>Styled Background</em> in any webpage.

<strong>Embed code allows this Collection to show up on another website</a></strong>
![Embed code Collection view sample](docs/images/embed.jpeg)
sample picture 9

<br>
<strong><a name="samp10">Same <em>Presentation Window</em> functionality when an icon is clicked.</a></strong>
![Embed code Modal Presentation Window  sample](docs/images/embed_popUp.jpeg)
sample picture 10
<br><br><br><br>


### Site Tree and Specific Functionality

Spend some time drawing out on paper mockups _every_ page of your MVP site.
Annotate _every_ component of the interface _every_ action the user can take.

<strong>Website Tree</strong> (separate webpages bolded and linked to pictures)
- <strong>[Home Page](#samp1)</strong> <em>(sample picture 1)</em> with Simple Full-screen layout
  - two buttons on Home Page to CREATE and VIEW
    - Create a Collection click leads to:
      - <strong>[Presentation Window UI Builder](#samp2)</strong> then to...
      - <strong>[Add to Collection](#samp4) </strong>webpage
    - View saved collections (e.g. <em>All My Collections</em>) click leads to:
      - <strong>[Collection](#samp6) "shelf" webpage</strong> with clickable Collectible icons as well as Share and Embed buttons
        - Icon click shows [Presentation Window](#samp7) revealing a collectible's details. Close this window by clicking "X".
        - [Share button](#samp8) copies webpage URL to clipboard and shows message "Collection link copied to clipboard"
        - [Embed button](#samp8) copies script embed code to clipboard then shows message "Collection embed code copied to clipboard"



### Frontend vs. Background activity
If there is any actions your app needs to take in the background describe _each_ of them and how they change the underlying data your app saves.

- Home Page ['Create a Collection'](#samp1) button when clicked
  1. open a prompt to ask the user to name the new Collection
  2. backend creates a new HTML file and names it the same (from given "blank" HTML template with pre-made <form> nodes)

- Starting off Building a Collection [<em>form/Presentation Window</em>](#samp2),
  1. as the form is being built, HTML input nodes are being appended to the form). ****Maybe Pre-built form will be better to start with.
  2. The <em>Save Layout</em> button saves the Collection's HTML file.

- [Add to Collection button](#samp2) takes the Collectible's form data and stores it as an key/value pair in an array/list.  The picture ID icon is stored in an image folder.

- Share/Embed buttons code copied to clipboard and



### MVP
**Pick the minimum feature set for your product to work.**
Everything else should go in the "further work" section.

##### Models
- 2 table database (Collection and Collectible) ForeignKey

##### Templates
- [Home HTML](https://startbootstrap.com/template-overviews/the-big-picture/)
- [Collectible Form HTML (Editing Presentation Window)](#samp5)
- [Single Collection HTML (with Presentation Modal Window)](#samp6)
- [All Collections HTML](https://startbootstrap.com/template-overviews/thumbnail-gallery/)


Write out a description of _every_ page and component and action!!!!!!


### Data Model

What are the persistent "nouns" you need to save across pages in your project MVP?
What do they represent?

- [Collection](#samp6) ------> Collection Sets (e.g. books,
  stamps, DVDs, music,)
- [collectible (item)](#samp4) ---------> A single item in a Collection


How do you need to _search_ for specific instances of nouns?

### Category
- name (allows for user to make sub-categories expanding on "type" in Collection model

### Collection
- owner (Foreign Key)
- image (user upload)
- name of Collection (e.g. My Paintings from the 70's)
- type of Collection (e.g. visual art - oil on canvas)
- categories (Many to many relationship) (e.g. Jazz, classical)
- created (date)
- status (private or public)

### Collectible/Item
- photo ID/cover art (user upload)
- name
- description
- Author/Composer or Creator
- Artist
- Publisher
- Year Published
- Copyright year
- serial number
- classification (Many to Many Relationship)
- date created
- date last saved

### Link
- name
- link
- collectible (Foreign Key)



### Technical Components
What are the "moving parts" of your MVP?
What are the things like "modules" you're going to write?
How do they talk to each other?





_Make decisions_ here and now.
Do research and prototyping to figure out what libraries and technologies will help you solve your problems.
Write up which ones you'll use.
It's okay if they end up not working and you have to change your plans.

- WSIWYG editor plug-in for user to customize Presentation Window and Collection's Display View

- jQuery UI (use "draggable" and "droppable" interactions https://jqueryui.com/droppable/) for drag and drop feature to make <a name="samp2">form/Presentation Window</a>.  
Also this plug-in for drag and drop jQuery form maker: https://formbuilder.online/

- Bootstrap to help with form presentation and overall website appearance.


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


### Brainstorming Area
