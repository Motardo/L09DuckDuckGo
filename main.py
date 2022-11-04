import requests

url_ddg = "https://api.duckduckgo.com"
search = "presidents+of+the+united+states"
presidents = [
"Adams",
"Arthur",
"Biden",
"Buchanan",
"Bush",
"Carter",
"Cleveland",
"Clinton",
"Coolidge",
"Eisenhower",
"Fillmore",
"Ford",
"Garfield",
"Grant",
"Harding",
"Harrison",
"Hayes",
"Hoover",
"Jackson",
"Jefferson",
"Johnson",
"Johnson",
"Kennedy",
"Lincoln",
"Madison",
"McKinley",
"Monroe",
"Nixon",
"Obama",
"Pierce",
"Polk",
"Reagan",
"Roosevelt",
"Taft",
"Taylor",
"Truman",
"Trump",
"Tyler",
"Van Buren",
"Washington",
"Wilson",
]

def test_ddg_presidents():
    resp = requests.get(url_ddg + "/?q=" + search + "&format=json")
    rsp_data = resp.json()

    # extract RelatedTopics field from response
    related_topics = rsp_data["RelatedTopics"]
    assert len(related_topics) >= 45

    # extract Text field from RelatedTopics
    texts = list(map(lambda topic: topic["Text"], related_topics))
    assert len(texts) >= 45

    for president in presidents:
        # search for each president in any of the Text fields
        assert any(president in text for text in texts)



# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
