# Imports
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QLineEdit, QLabel, QLineEdit, QPushButton, QVBoxLayout)

from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        # different widgets
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        #self.city_input.resize(50,40)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("70℉", self)
        self.emoji_label = QLabel("☀️", self)
        self.description_label = QLabel("Sunny", self)

        self.init_ui()

    def init_ui(self):

        self.setWindowTitle("Weather App")

        # layout manager
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        # aligning ui elements horizontal center
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        #self.get_weather_button.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        
        # Giving UI elements unique names
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # "Stylesheet" for UI elements
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 20px;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 70px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        print("You get Weather")
        pass

    def display_errors(self, message):
        pass

    def display_weather(self, data):
        pass




if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())