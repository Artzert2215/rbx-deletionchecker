# This is a sample Python script.
import math
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import urllib.request


def read_urls(array):
    # write file if not present
    file = open("urls.txt", 'a')
    file.close()

    print("Reading in urls..")
    file = open("urls.txt", 'r')
    urls = file.readlines()
    url_count = 0
    for url in urls:
        url_count += 1
        url = url.strip()
        start_index = url.find('http://')
        slice_begin_index = 7
        if start_index < 0:
            start_index = url.find('https://')
            slice_begin_index = 8
        if start_index < 0:
            pass
        else:
            url = url[slice_begin_index::]
        print(str(url_count) + ": read", url, end='\r')
        array.append(url)
    file.close()

    # checks on urls
    count = len(array)
    array = set(array)
    count2 = len(array)
    print("Removed", count - count2, "duplicates")
    array = list(array)

    # write updated file
    file = open("urls.txt", 'w')
    for url in array:
        file.write("https://" + url + "\n")
    file.close()


def get_html(html_url, timeout=5, decode='utf-8', maxtries=2):
    for tries in range(maxtries):
        try:
            with urllib.request.urlopen(html_url, None, timeout) as response:
                return response.read().decode(decode)
        except Exception as e:
            if "308" or "404" in str(e):
                return "DELETED"
            print("Error:", e)
            if tries < (maxtries - 1):
                continue
            else:
                return None


TYPE_DICT = {
    "USER": "roblox.com/users",
    "GAME": "roblox.com/games",
    "CATALOG": "roblox.com/catalog",
    "GROUP": "roblox.com/groups",
}


def get_url_type(url):
    for type in TYPE_DICT.keys():
        if TYPE_DICT[type] in url:
            return type


def check_page(url):
    type = get_url_type(url)
    if type is None:
        return None
    html = get_html("https://" + url)
    if html is None:
        return None
    if html == "DELETED":
        return "DELETED"
    # print(html)
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
    else:
        print("Could not identify url type.")
        return None


def run_checks(array):
    todo = len(array)
    print("Checking {0} urls..".format(todo))
    count = 0
    fails = []
    up = []
    down = []
    for url in array:
        count += 1
        cc = check_page(url)
        if cc is not None:
            print("{0}% ({1}/{2}) [{3}]              ".format(math.floor((count / todo) * 100), count, todo, cc),
                  end='\r')
            if cc == "DELETED":
                down.append(url)
            else:
                up.append(url)
        else:
            print("{0}: failed to fetch {1}".format(count, url))
            fails.append(url)

    # summary
    print("Finished check!              ")
    print("Total checked:", count)
    print("Failed:", len(fails))
    print("Deleted:", len(down))
    print("Up:", len(up))

    return down, up, fails


def dump_results(deleted, up, failed):
    # create file if not present
    file = open("deleted.txt", 'a')
    file.close()

    print("Saving results..")

    print("Failed / up >> urls.txt")
    file = open("urls.txt", 'w')
    for url in up + failed:
        file.write("https://" + url + "\n")
    file.close()

    print("Deleted >> deleted.txt")
    file = open("deleted.txt", 'w')
    for url in deleted:
        file.write("https://" + url + "\n")
    file.close()


def main():
    url_array = []
    read_urls(url_array)
    deleted, up, failed = run_checks(url_array)
    dump_results(deleted, up, failed)
    input("Press Enter to exit...")


main()
