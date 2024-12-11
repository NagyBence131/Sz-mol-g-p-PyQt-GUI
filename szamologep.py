import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout


class Szamologep(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Ablak beállítások
        self.setWindowTitle("Számológép")
        self.setGeometry(100, 100, 300, 400)

        # Layoutok
        self.fo_layout = QVBoxLayout()
        self.setLayout(self.fo_layout)

        # Kijelző
        self.kijelzo = QLineEdit()
        self.kijelzo.setReadOnly(True)
        self.kijelzo.setStyleSheet("font-size: 24px;")
        self.fo_layout.addWidget(self.kijelzo)

        # Gombok
        self.gombok_letrehozasa()

    def gombok_letrehozasa(self):
        racs_layout = QGridLayout()

        gombok = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            '0': (3, 0), '.': (3, 1), '=': (3, 2), '+': (3, 3),
            'Töröl': (4, 0),
        }

        for gomb_szoveg, pozicio in gombok.items():
            gomb = QPushButton(gomb_szoveg)
            gomb.setStyleSheet("font-size: 18px;")
            gomb.clicked.connect(self.gombra_kattintas)
            racs_layout.addWidget(gomb, pozicio[0], pozicio[1])

        self.fo_layout.addLayout(racs_layout)

    def gombra_kattintas(self):
        kuldo = self.sender()
        gomb_szoveg = kuldo.text()

        if gomb_szoveg == "Töröl":
            self.kijelzo.clear()
        elif gomb_szoveg == "=":
            try:
                eredmeny = eval(self.kijelzo.text())
                self.kijelzo.setText(str(eredmeny))
            except Exception:
                self.kijelzo.setText("Hiba")
        else:
            self.kijelzo.setText(self.kijelzo.text() + gomb_szoveg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    szamologep = Szamologep()
    szamologep.show()
    sys.exit(app.exec_())
