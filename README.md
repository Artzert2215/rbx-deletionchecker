# rbx-deletionchecker
Checks to see if games, users, groups and games are deleted or still up.
>Requires python 3.8+

## How to use
To run type `python main.py` in a terminal window in the folder main.py is located (= the repo folder).
- The tool will create an empty urls.txt and deleted.txt file when first ran.
- Paste urls into urls.txt (1 per line) and run the tool.
- It will go over each url, items that are not deleted or couldn't be checked are returned to urls.txt, others go to deleted.txt.

## Checking system
The tool currently uses a very weak system that looks for a specific string in the html of the page.
Report any false positives/negatives via a bug report.

Below is the current code, keep in mind it is very barebones.
```
    if type == "GROUP":
        if "This group has been locked</p>" in html:
            return "DELETED"
        else:
            return "UP"
    elif type == "GAME":
        if "under review. Try again later.</span>" in html:
            return "DELETED"
        else:
            return "UP"
    elif type == "USER":
        if "[ Content Deleted ]</span>" in html:
            return "DELETED"
        else:
            return "UP"
    elif type == "CATALOG":
        if "This item is not currently for sale.</div>" in html:
            return "DELETED"
        else:
            return "UP"
```
