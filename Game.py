import sys
import time
import pygame
import random
import keyboard
from PyQt5 import Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMainWindow, QComboBox, QLineEdit, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem


go_play = False
pausing = False
running = True
numSkin = '1'
speedHero = 1
nickname = 'user1'


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

        self.CSpeedTab = QLabel('<font color="white">Character speed</font>', self)
        self.CSpeedTab.setFont(Qt.QFont('abc', 9))
        self.CSpeedTab.move(5, 30)

        self.CSpeedBox = QComboBox(self)
        self.CSpeedBox.move(100, 28)
        self.CSpeedBox.addItems(['One', 'Two'])
        self.CSpeedBox.activated.connect(self.check_index_cSpeed)

    def check_index_cSpeed(self):
        self.main.CIndexes.append(self.CSpeedBox.currentIndex() + 1)


class Win4(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)

        self.main = root

        self.setGeometry(1270, 100, 420, 200)
        self.setWindowTitle('Results')

        mass = [i.split() for i in open('results.txt')]
        self.table = QTableWidget(len(mass), 4, self)
        self.table.resize(420, 200)
        self.table.setHorizontalHeaderLabels(['Nick', 'Result', 'Zones reached', 'Time'])
        for i in range(0, len(mass)):
            for j in range(0, 4):
                self.table.setItem(i, j, QTableWidgetItem(mass[i][j]))


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
        global nickname

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

        if nickname != 'user1':
            self.field = QLineEdit(f'{nickname}', self)
            self.field.setPlaceholderText('Enter your nick')
            self.field.move(100, 240)
            self.field.resize(150, 23)
        else:
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
        global go_play, nickname
        if self.field.text():
            nickname = self.field.text()
            go_play = True
            self.close()
        else:
            self.field.setPlaceholderText('ENTER YOUR NICK')


class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(800, 400, 300, 400)
        self.setWindowTitle('Menu')

        self.changeSkin = Win2(self)
        self.changeSettings = Win3(self)
        self.checkResults = Win4(self)
        self.reference = Win5(self)
        self.nick = Win6(self)

        self.numSkin = '1'
        self.speedHero = 1
        self.CIndexes = []
        self.StIndexes = []

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
            speedHero = self.CIndexes[-1]
        except IndexError:
            pass

    def updateResults(self, start_time, result, zones_count):
        global nickname

        end_time = time.time()
        elapsed_time = end_time - start_time
        file_for_results = open('results.txt', mode='a')
        file_for_results.write(f'{nickname} {result} {zones_count} {round(elapsed_time)}sec\n')

    def howToPlay(self):
        pass

    def closee(self):
        global go_play, running
        if go_play:
            self.hide()
            running = True
            GAME().run()
        else:
            pass

    def game_over(self, result, zones_count):
        game_over_window = GameOverWindow(self, result, zones_count)
        game_over_window.exec_()


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Circle(pygame.sprite.Sprite):
    def __init__(self, initial_radius, border_color, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((initial_radius * 2, initial_radius * 2), pygame.SRCALPHA).convert_alpha()
        self.border_color = border_color
        self.radius = initial_radius

        # Рисуем абсолютно прозрачный круг
        pygame.draw.circle(self.image, (0, 0, 0, 70), (initial_radius, initial_radius), initial_radius)

        # Рисуем белый контур круга
        pygame.draw.circle(self.image, border_color, (initial_radius, initial_radius), initial_radius, 2)

        self.rect = self.image.get_rect()
        self.rect.center = location

    def decrease_radius(self, delta_radius=3):
        # Уменьшаем радиус на delta_radius
        self.radius -= delta_radius
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA).convert_alpha()

        # Рисуем абсолютно прозрачный круг
        pygame.draw.circle(self.image, (0, 0, 0, 70), (self.radius, self.radius), self.radius)

        # Рисуем белый контур круга
        pygame.draw.circle(self.image, self.border_color, (self.radius, self.radius), self.radius, 2)

        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center


class GameOverWindow(QtWidgets.QDialog):
    def __init__(self, root, result, count, **kwargs):
        super().__init__(root, **kwargs)

        self.main = root

        self.setGeometry(800, 400, 300, 150)
        self.setWindowTitle('Game Over')

        self.back = QLabel(self)
        self.backY = QPixmap(f'background.png')
        self.back.move(0, 0)
        self.back.resize(400, 150)
        self.back.setPixmap(self.backY)

        self.result_label = QLabel(f'<font color="white">You <b>{result}!</b><br/>'
                                   f'You <b>reached:</b> {count} zones</font>', self)
        self.result_label.setFont(Qt.QFont('abc', 16))
        self.result_label.move(60, 40)

        self.ok_button = QPushButton('OK', self)
        self.ok_button.move(120, 100)
        self.ok_button.clicked.connect(self.closee)

    def closee(self):
        self.close()
        Main().show()
        app.exec()


print(f'Отладка:\nНик - {nickname}\nСкорость персонажа - {speedHero}\nНомер скина - {numSkin}')


class GAME:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('MiniFortnite')

    def run(self):
        global running

        size = width, height = 1920, 1080
        fps = 144
        zones_count = 0

        screen = pygame.display.set_mode(size)
        clock = pygame.time.Clock()
        BackGround = Background('map.png', [0, 0])

        rectangle_width, rectangle_height = 800, 800
        rectangle_left = (width - rectangle_width) // 2
        rectangle_top = (height - rectangle_height) // 2

        circle_radius = 100
        circle_border_color = (255, 255, 255)
        circle_sprite = Circle(circle_radius, circle_border_color,
                               (random.randint(rectangle_left, rectangle_left + rectangle_width),
                                random.randint(rectangle_top, rectangle_top + rectangle_height)))

        if go_play:
            start_time = time.time()
            char_img = pygame.image.load(f'skins/skin{numSkin}.png')
        else:
            raise SystemExit
        char_rect = char_img.get_rect()
        char_rect.center = (random.randint(540, 800), random.randint(80, 800))

        all_sprites = pygame.sprite.Group(circle_sprite)

        WHITE = (255, 255, 255)
        FONT = pygame.font.Font(None, 36)
        initial_time = 7

        if speedHero == 1:
            initial_time = 7
        if speedHero == 2:
            initial_time = 4
        if speedHero == 3:
            initial_time = 3
        if speedHero == 4:
            initial_time = 2.5
        current_time = initial_time
        last_update_time = pygame.time.get_ticks()

        while running:
            dt = clock.tick(fps) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F1:
                        raise SystemExit

            # Пересоздаем окружность в пределах прямоугольника при коллизии
            if char_rect.colliderect(circle_sprite.rect):
                zones_count += 1
                current_time = initial_time
                circle_sprite.decrease_radius()
                if circle_sprite.radius <= 5:
                    result = 'win'
                    Main().game_over(result, zones_count)
                    Main().updateResults(start_time, result, zones_count)
                    zones_count = 0
                    running = False
                circle_sprite.rect.center = (random.randint(rectangle_left, rectangle_left + rectangle_width),
                                             random.randint(rectangle_top, rectangle_top + rectangle_height))

            if keyboard.is_pressed('a'):
                char_rect.x -= speedHero * 5
            if keyboard.is_pressed('d'):
                char_rect.x += speedHero * 5
            if keyboard.is_pressed('w'):
                char_rect.y -= speedHero * 5
            if keyboard.is_pressed('s'):
                char_rect.y += speedHero * 5

            current_ticks = pygame.time.get_ticks()
            if current_ticks - last_update_time >= 1000:
                last_update_time = current_ticks
                current_time -= 1

                # Проверка на окончание времени
                if current_time <= 0:
                    running = False
                    result = 'lost'
                    Main().game_over(result, zones_count)
                    Main().updateResults(start_time, result, zones_count)
                    zones_count = 0

            # Отображение таймера
            timer_text = FONT.render(f'Time left: {round(current_time - 0.01)}', True, WHITE)
            zones_text = FONT.render(f'Zones: {zones_count}', True, WHITE)
            screen.blit(timer_text, (10, 10))
            screen.blit(zones_text, (10, 50))

            pygame.display.update()
            screen.fill('#022027')
            screen.blit(BackGround.image, BackGround.rect)
            screen.blit(char_img, char_rect)

            all_sprites.draw(screen)

            clock.tick(fps)
            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec()
