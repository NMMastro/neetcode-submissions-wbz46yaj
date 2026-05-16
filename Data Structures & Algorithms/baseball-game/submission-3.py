class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for o in operations:
            if o == "+":
                record.append(record[-1] + record[-2])
            elif o == "C":
                record.pop()
            elif o == "D":
                record.append(record[-1] * 2)

            try:
                int(o)
                record.append(int(o)) 
            except ValueError:
                continue
        return sum(record)
