class Spreadsheet:
    def __init__(self, rows: int):
        self.cells: dict[str, int] = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cells.pop(cell, None)

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split("+")
        return (int(a) if a[0].isdigit() else self.cells.get(a, 0)) + (int(b) if b[0].isdigit() else self.cells.get(b, 0))
