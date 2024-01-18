import sys
import pygame
import random
import keyboard
from PyQt5 import Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QComboBox, QLineEdit


go_play = False
numSkin = '1'
speedHero = 1
nickname = 'user'


class Win2(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.main = root

        self.setGeometry(100, 100, 1720, 880)
        self.setWindowTitle('Pick the Skin')

        self.nameSkins = ['Evie', 'Scarlet Commander', 'Break Point', 'Laguna',
                          'Galaxy', 'Crown', 'Nog Ops', 'Crusher', 'Aura', 'Focus']
        self.nameSkinss = {'Evie': 1, 'Scarlet Commander': 2, 'Break Point': 3, 'Laguna': 4,
                           'Galaxy': 5, 'Crown': 6, 'Nog Ops': 7, 'Crusher': 8, 'Aura': 9, 'Focus': 10}

        self.skins = []
        for n in range(1, 11):
            self.skins.append(QPixmap(f'SkinsPreview/skin{str(n)}.png'))

        self.back = QLabel(self)
        self.backY = QPixmap('background.png')
        self.back.move(0, 0)
        self.back.resize(1720, 880)
        self.back.setPixmap(self.backY)

        self.icon1 = QLabel(self)
        self.icon1.move(79, 126)
        self.icon1.resize(250, 250)
        self.icon1.setPixmap(self.skins[0])

        self.icon2 = QLabel(self)
        self.icon2.move(407, 126)
        self.icon2.resize(250, 250)
        self.icon2.setPixmap(self.skins[1])

        self.icon3 = QLabel(self)
        self.icon3.move(735, 126)
        self.icon3.resize(250, 250)
        self.icon3.setPixmap(self.skins[2])

        self.icon4 = QLabel(self)
        self.icon4.move(1143, 126)
        self.icon4.resize(250, 250)
        self.icon4.setPixmap(self.skins[3])

        self.icon5 = QLabel(self)
        self.icon5.move(1391, 126)
        self.icon5.resize(250, 250)
        self.icon5.setPixmap(self.skins[4])

        self.icon6 = QLabel(self)
        self.icon6.move(79, 502)
        self.icon6.resize(250, 250)
        self.icon6.setPixmap(self.skins[5])

        self.icon7 = QLabel(self)
        self.icon7.move(407, 502)
        self.icon7.resize(250, 250)
        self.icon7.setPixmap(self.skins[6])

        self.icon8 = QLabel(self)
        self.icon8.move(735, 502)
        self.icon8.resize(250, 250)
        self.icon8.setPixmap(self.skins[7])

        self.icon9 = QLabel(self)
        self.icon9.move(1103, 502)
        self.icon9.resize(250, 250)
        self.icon9.setPixmap(self.skins[8])

        self.icon10 = QLabel(self)
        self.icon10.move(1391, 502)
        self.icon10.resize(250, 250)
        self.icon10.setPixmap(self.skins[9])

        self.btn1 = QPushButton(self.nameSkins[0], self)
        self.btn1.move(148, 390)
        self.btn1.resize(129, 23)
        self.btn1.clicked.connect(self.ok)

        self.btn2 = QPushButton(self.nameSkins[1], self)
        self.btn2.move(470, 390)
        self.btn2.resize(129, 23)
        self.btn2.clicked.connect(self.ok)

        self.btn3 = QPushButton(self.nameSkins[2], self)
        self.btn3.move(785, 390)
        self.btn3.resize(129, 23)
        self.btn3.clicked.connect(self.ok)

        self.btn4 = QPushButton(self.nameSkins[3], self)
        self.btn4.move(1135, 390)
        self.btn4.resize(129, 23)
        self.btn4.clicked.connect(self.ok)

        self.btn5 = QPushButton(self.nameSkins[4], self)
        self.btn5.move(1450, 390)
        self.btn5.resize(129, 23)
        self.btn5.clicked.connect(self.ok)

        self.btn6 = QPushButton(self.nameSkins[5], self)
        self.btn6.move(148, 765)
        self.btn6.resize(129, 23)
        self.btn6.clicked.connect(self.ok)

        self.btn7 = QPushButton(self.nameSkins[6], self)
        self.btn7.move(470, 765)
        self.btn7.resize(129, 23)
        self.btn7.clicked.connect(self.ok)

        self.btn8 = QPushButton(self.nameSkins[7], self)
        self.btn8.move(785, 765)
        self.btn8.resize(129, 23)
        self.btn8.clicked.connect(self.ok)

        self.btn9 = QPushButton(self.nameSkins[8], self)
        self.btn9.move(1135, 765)
        self.btn9.resize(129, 23)
        self.btn9.clicked.connect(self.ok)

        self.btn10 = QPushButton(self.nameSkins[9], self)
        self.btn10.move(1450, 765)
        self.btn10.resize(129, 23)
        self.btn10.clicked.connect(self.ok)

    def ok(self):
        if self.nameSkinss[self.sender().sender().text()]:
            self.main.numSkin = self.nameSkinss[self.sender().sender().text()]

        self.close()


class Win3(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.main = root

        self.setGeometry(875, 270, 150, 85)
        self.setWindowTitle('Settings')

        self.back = QLabel(self)
        self.backY = QPixmap('background.png')
        self.back.move(0, 0)
        self.back.resize(400, 400)
        self.back.setPixmap(self.backY)

        self.speedTab = QLabel('<font color="white">Speed</font>', self)
        self.speedTab.setFont(Qt.QFont('abc', 11))
        self.speedTab.move(10, 10)

        self.speedBox = QComboBox(self)
        self.speedBox.move(90, 10)
        self.speedBox.addItems(['One', 'Two', 'Three', 'Four'])
        self.speedBox.activated.connect(self.check_index)

    def check_index(self):
        self.main.indexes.append(self.speedBox.currentIndex() + 1)


class Win4(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.main = root

        self.setGeometry(1470, 100, 350, 200)
        self.setWindowTitle('Results')

        self.back = QLabel(self)
        self.backY = QPixmap('background.png')
        self.back.move(0, 0)
        self.back.resize(400, 400)
        self.back.setPixmap(self.backY)


class Win5(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.main = root

        self.setGeometry(100, 100, 350, 200)
        self.setWindowTitle('How to play?')

        self.back = QLabel(self)
        self.backY = QPixmap('background.png')
        self.back.move(0, 0)
        self.back.resize(400, 400)
        self.back.setPixmap(self.backY)


class Win6(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.main = root

        self.setGeometry(840, 450, 350, 330)
        self.setWindowTitle('Enter your nick')

        self.back = QLabel(self)
        self.backY = QPixmap('background.png')
        self.back.move(0, 0)
        self.back.resize(500, 500)
        self.back.setPixmap(self.backY)

        self.icon = QLabel(self)
        self.iconY = QPixmap('preview.png')
        self.icon.move(0, 0)
        self.icon.resize(500, 250)
        self.icon.setPixmap(self.iconY)

        self.field = QLineEdit(self)
        self.field.setPlaceholderText('Enter your nick')
        self.field.move(100, 240)
        self.field.resize(150, 23)

        self.btnRan = QPushButton('Random', self)
        self.btnRan.move(260, 240)
        self.btnRan.resize(50, 23)
        self.btnRan.clicked.connect(self.random)

        self.btnSave = QPushButton('Let`s go!', self)
        self.btnSave.move(137, 270)
        self.btnSave.clicked.connect(self.go)

    def random(self):
        global nickname
        nickname = f'user{random.randint(10 ** 6, 10 ** 7)}'

        self.field.setText(nickname)

    def go(self):
        global go_play
        go_play = True
        self.close()


class Main(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.setGeometry(800, 400, 300, 400)
        self.setWindowTitle('Menu')

        self.changeSkin = Win2(self)
        self.changeSettings = Win3(self)
        self.checkResults = Win4(self)
        self.reference = Win5(self)
        self.nick = Win6(self)

        self.numSkin = '1'
        self.speedHero = 1
        self.indexes = []

        self.back = QLabel(self)
        self.backY = QPixmap(f'background.png')
        self.back.move(0, 0)
        self.back.resize(400, 400)
        self.back.setPixmap(self.backY)

        self.logo = QLabel(self)
        self.logoY = QPixmap(f'logo.png')
        self.logo.move(10, 10)
        self.logo.resize(280, 140)
        self.logo.setPixmap(self.logoY)

        self.logoMini = QLabel(self)
        self.logoMiniY = QPixmap(f'mini.png')
        self.logoMini.move(213, 77)
        self.logoMini.resize(70, 50)
        self.logoMini.setPixmap(self.logoMiniY)

        self.btnPlay = QPushButton('Play', self)
        self.btnPlay.move(20, 234)
        self.btnPlay.resize(260, 26)
        self.btnPlay.clicked.connect(self.nick.exec)
        self.btnPlay.clicked.connect(self.closee)

        self.btnChangeSkin = QPushButton('Change the skin', self)
        self.btnChangeSkin.move(20, 264)
        self.btnChangeSkin.resize(260, 26)
        self.btnChangeSkin.clicked.connect(self.changeSkin.exec)
        self.btnChangeSkin.clicked.connect(self.updateNumSkin)

        self.btnCheckResults = QPushButton('Check the results', self)
        self.btnCheckResults.move(20, 294)
        self.btnCheckResults.resize(260, 26)
        self.btnCheckResults.clicked.connect(self.checkResults.exec)
        self.btnCheckResults.clicked.connect(self.updateResults)

        self.btnSettings = QPushButton('Settings', self)
        self.btnSettings.move(20, 324)
        self.btnSettings.resize(260, 26)
        self.btnSettings.clicked.connect(self.changeSettings.exec)
        self.btnSettings.clicked.connect(self.updateSettings)

        self.btnHowToPlay = QPushButton('How to play?', self)
        self.btnHowToPlay.move(20, 354)
        self.btnHowToPlay.resize(260, 26)
        self.btnHowToPlay.clicked.connect(self.reference.exec)
        self.btnHowToPlay.clicked.connect(self.howToPlay)

    def updateNumSkin(self):
        global numSkin
        numSkin = self.numSkin

    def updateSettings(self):
        global speedHero
        try:
            speedHero = self.indexes[-1]
        except IndexError:
            pass

    def updateResults(self):
        pass

    def howToPlay(self):
        pass

    def closee(self):
        global go_play
        if go_play:
            self.close()
        else:
            pass


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec()

    pygame.init()
    pygame.display.set_caption('MiniFortnite')

    size = width, height = 1920, 1080
    fps = 144
    running = True

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    BackGround = Background('map.png', [0, 0])

    if go_play:
        char_img = pygame.image.load(f'skins/skin{numSkin}.png')
    else:
        raise SystemExit
    char_rect = char_img.get_rect()
    char_rect.center = (random.randint(540, 1500), random.randint(80, 1000))

    while running:
        dt = clock.tick(fps) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    raise SystemExit

        if keyboard.is_pressed('a'):
            char_rect.x -= speedHero
        if keyboard.is_pressed('d'):
            char_rect.x += speedHero
        if keyboard.is_pressed('w'):
            char_rect.y -= speedHero
        if keyboard.is_pressed('s'):
            char_rect.y += speedHero

        screen.fill('#022027')
        screen.blit(BackGround.image, BackGround.rect)
        screen.blit(char_img, char_rect)

        clock.tick(fps)
        pygame.display.update()
    pygame.quit()
