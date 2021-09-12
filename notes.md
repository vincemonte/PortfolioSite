# ***Notes and Checklist***
## **Checklist**:
### General:
- [X] Change colors
- [X] Change Bootstrap Card Padding and Margins
- [X] Add a login for me to update and delete posts
- [X] Use em to make it easier to position things
  - switch percentages to em
- [X] Scale page to when resizing browser (i.e. responsive page)
  - Scale for other devices
- [X] Change the box shadows of the home page posts


### **To be on main layout:**
- [X] Navbar
  - [X] logo
  - [X] Up-down color gradient
  - [X] site links
  - [X] on the right side, add the GitHub logo and link
- [ ] Footer


## **Notes**:
### General:
- If we only had a main and sidebar (div) elements as direct children of our body, and the body's width is set to 100%, we'd expect to be able to allocate the main and sidebar 60% and 40%, respectively, to fit our page perfectly (when they are floated left and right, respectively). However, margins, borders, and paddings of these elements play a role into how they'll filt (i.e. how much pixel size is being used after the fact)
  - This is another reason why we should be using relative sizes (e.g. em)
-

### Jinga and Flask:
- Accessing variables in html: {{ }}
- Code blocks: {% %}
- page headers should be part of the passed in content block
- only allow the about aside on the main page


### Colors:
- Navbar background: #34769C
- Cream: #fffacd
  - use instead of white
- add an outline to the post headings text (h4)
- white ripple background source: https://www.pexels.com/photo/curve-design-futuristic-lines-911738/
  - check if I may use in published site

## Project Icon Authors
- [Code](https://www.flaticon.com/authors/pixel-perfect)
- [Writing](https://creativemarket.com/Becris)
- [Photography](https://www.flaticon.com/authors/good-ware)
- [Update](https://www.freepik.com" title="Freepik")

#Other citations:
- [Text Truncate Techniques](https://codepen.io/srekoble/pen/EgmyxV)
- [Gradients](https://uigradients.com/)
- [Text Shadows for Card Headers](https://www.massmediums.com/blog/134-create-great-looking-pure-css-text-shadows.html)
