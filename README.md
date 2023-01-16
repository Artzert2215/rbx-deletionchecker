# rbx-deletionchecker
Checks to see if games, users, groups and games are deleted or still up.
>Requires python 3.8+ and urllib3

## How to use
To run type `python main.py` in a terminal window in the folder main.py is located (= the repo folder).
- The tool will create an empty urls.txt and deleted.txt file when first ran.
- Paste urls into urls.txt (1 per line) and run the tool.
- It will go over each url, items that are not deleted or couldn't be checked are returned to urls.txt, others go to deleted.txt.

## Checking system
The tool currently uses a very weak system that looks for a specific string in the html of the page.
Report any false positives/negatives via a bug report.

- Group is considered deleted if it is locked
- Game is considered deleted if unplayable
- Item is considered deleted if unpurchasable
- User is considered deleted if description is cleared (so a lot of false reports of still being up)
