from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from ApiHandler import ApiHandler


class GuiWindow(QMainWindow):
    def __init__(self):
        super(GuiWindow, self).__init__()
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Weather Check")
        self.initUI()

    def initUI(self):
        self.labelTemp = QtWidgets.QLabel(self)
        self.labelTemp.setText("Temp: ")
        self.labelTemp.move(50, 150)

        self.labelTempShow = QtWidgets.QLabel(self)
        self.labelTempShow.move(100, 150)

        self.labelTempMin = QtWidgets.QLabel(self)
        self.labelTempMin.setText("Temp min: ")
        self.labelTempMin.move(50, 200)

        self.labelTempMinShow = QtWidgets.QLabel(self)
        self.labelTempMinShow.move(100, 200)

        self.labelTempMax = QtWidgets.QLabel(self)
        self.labelTempMax.setText("Temp max: ")
        self.labelTempMax.move(50, 250)

        self.labelTempMaxShow = QtWidgets.QLabel(self)
        self.labelTempMaxShow.move(100, 250)

        self.labelWeatherDescription = QtWidgets.QLabel(self)
        self.labelWeatherDescription.setText("Warunki pogodowe: ")
        self.labelWeatherDescription.move(150, 150)

        self.labelWeatherDescriptionShow = QtWidgets.QLabel(self)
        self.labelWeatherDescriptionShow.move(250, 150)

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Sprawdz")
        self.button.move(200, 100)
        self.button.clicked.connect(self.clicked)

        self.inputCity = QtWidgets.QLineEdit(self)
        self.inputCity.move(50, 100)

    def clicked(self):
        halo2 = self.inputCity.text()
        halo = ApiHandler(str(halo2))
        halo.request()
        self.labelTempShow.setText(str(round(halo.temp - 273.15)))
        self.labelTempMinShow.setText(str(round(halo.tempMin - 273.15)))
        self.labelTempMaxShow.setText(str(round(halo.tempMax - 273.15)))
        self.labelWeatherDescriptionShow.setText(str(halo.weatherDescription))

