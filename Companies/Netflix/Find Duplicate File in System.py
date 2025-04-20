class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dups = defaultdict(list)

        for path in paths:
            files = path.split(" ")

            for i in range(1, len(files)):
                name, c = files[i].split("(")

                dups[c].append(f"{files[0]}/{name}")

        return [group for group in dups.values() if len(group) > 1]
