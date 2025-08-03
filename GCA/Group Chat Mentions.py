from collections import defaultdict

def solution(members: list, messages: list):
    member_set = set(members)
    freq_hash = defaultdict(set)
    res = []

    for i, message in enumerate(messages):
        words = message.split(" ")

        for word in words:
            if len(word) and word[0] == "@":
                ids = word[1:].split(",")

                for iden in ids:
                    if len(iden) and iden in member_set:
                        freq_hash[iden].add(i)
    
    members.sort(key=lambda x: (-len(freq_hash[x]), x))

    for member in members:
        res.append(f"{member}={len(freq_hash[member])}")
    
    return res

import unittest

class TestMentionCounter(unittest.TestCase):
    def test_basic_mention_once(self):
        members = ["id1", "id2"]
        messages = ["@id1 Hello!", "Hi @id2"]
        expected = ["id1=1", "id2=1"]
        self.assertEqual(solution(members, messages), expected)

    def test_multiple_mentions_one_message(self):
        members = ["id1", "id2", "id3"]
        messages = ["@id1,id2,id1,id3 Hello!"]
        expected = ["id1=1", "id2=1", "id3=1"]
        self.assertEqual(solution(members, messages), expected)

    def test_no_mentions(self):
        members = ["id10", "id20"]
        messages = ["Hello world", "Nothing to see here"]
        expected = ["id10=0", "id20=0"]
        self.assertEqual(solution(members, messages), expected)

    def test_mentions_with_invalid_ids(self):
        members = ["id1", "id2"]
        messages = ["@id3,id1 @id2", "@id4"]
        expected = ["id1=1", "id2=1"]
        self.assertEqual(solution(members, messages), expected)

    def test_lexicographical_tiebreaker(self):
        members = ["id2", "id1"]
        messages = ["@id1", "@id2"]
        expected = ["id1=1", "id2=1"]
        self.assertEqual(solution(members, messages), expected)

    def test_edge_mentions(self):
        members = ["id9", "id10"]
        messages = ["@id9 is here", "I saw him @id10"]
        expected = ["id10=1", "id9=1"]
        self.assertEqual(solution(members, messages), expected)

    def test_empty_inputs(self):
        members = []
        messages = ["@id1,id2"]
        expected = []
        self.assertEqual(solution(members, messages), expected)

if __name__ == "__main__":
    unittest.main()

