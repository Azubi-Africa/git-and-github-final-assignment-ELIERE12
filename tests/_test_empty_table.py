# importation of the solution function to test
import os
from tests.test_readme_table import read_table

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
empty_json_table = {
    "Project's Name": {1: "eliere individual project", 2: "group8_Eliere week7 peer project", 3: "week5peerproject"},
    "Description": {1: "project1", 2: "project2", 3: "project3"},
    "GitHub's Link": {1: "https://github.com/ELIERE12/eliere-individual-project.git", 2: "https://github.com/ELIERE12/group8_Eliere-week7-peer-project.git", 3: "https://github.com/ELIERE12/week5peerproject.git"},
}


def test_empty_table():
    """This is the test for the implemented solution passing
    valid inputs"""

    df = read_table()

    assert (
        df.replace("-", "").replace("https://", "").replace(" ", "").to_dict()
        == empty_json_table
    )

    print("[Info] Empty table")
