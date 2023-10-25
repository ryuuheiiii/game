import pygame
import sys

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("ipaexg.ttf", size)

def main_menu():
    while True:
        screen.blit(skyimg, (0, 0))

        menumousepos = pygame.mouse.get_pos()

        menutext = get_font(100).render("ベジタバトル", True, "green")
        menurect = menutext.get_rect(center=(640, 100))

        playbutton = Button(pygame.image.load("box.png"), pos=(640, 250), text_input="play", font=get_font(75), base_color="white", hovering_color="black")
        quitbutton = Button(pygame.image.load("box.png"), pos=(640, 550), text_input="exit", font=get_font(75), base_color="white", hovering_color="black")

        screen.blit(menutext, menurect)

        for button in [playbutton, quitbutton]:
            button.changeColor(menumousepos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playbutton.checkForInput(menumousepos):
                    choice()
                if quitbutton.checkForInput(menumousepos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def choice():
    while True:
        screen.blit(skyimg, (0, 0))
        pygame.display.set_caption("choice")
        choicemousepos = pygame.mouse.get_pos()

        choicetext = get_font(45).render("育てる野菜を選択", True, "White")
        choicerect = choicetext.get_rect(center=(640, 50))
        screen.blit(choicetext, choicerect)

        ninzinbutton = Button(image=pygame.image.load("box.png"), pos=(300, 250), text_input="人参", font=get_font(50), base_color="white", hovering_color="red")
        kyuuributtton = Button(image=pygame.image.load("box.png"), pos=(950, 250), text_input="きゅうり", font=get_font(50), base_color="white", hovering_color="green")
        applebutton = Button(image=pygame.image.load("box.png"), pos=(300, 500), text_input="りんご", font=get_font(50), base_color="white", hovering_color="red")
        grapebutton = Button(image=pygame.image.load("box.png"), pos=(950, 500), text_input="ブドウ", font=get_font(50), base_color="white", hovering_color="purple")        
        ninzinbutton.update(screen)
        kyuuributtton.update(screen)
        applebutton.update(screen)
        grapebutton.update(screen)
        for button in [ninzinbutton, kyuuributtton, applebutton, grapebutton]:
            button.changeColor(choicemousepos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if ninzinbutton.checkForInput(choicemousepos):
                        screen.blit(skyimg, (0, 0))                  
                        ninzintext = get_font(45).render("人参でいいですか？", True, "black")
                        ninzinrect = ninzintext.get_rect(center=(800, 300))
                        screen.blit(ninzintext, ninzinrect)
                        screen.blit(ninzinimg, (300,250))
                        choice2()                        
                    if kyuuributtton.checkForInput(choicemousepos):                       
                        screen.blit(skyimg, (0, 0))                                          
                        kyuuritext = get_font(45).render("きゅうりでいいですか？", True, "black")
                        kyuurirect = kyuuritext.get_rect(center=(830, 300))
                        screen.blit(kyuuritext, kyuurirect)
                        screen.blit(kyuuriimg, (300,250))
                        choice2()
                    if applebutton.checkForInput(choicemousepos):
                        screen.blit(skyimg, (0, 0))                  
                        appletext = get_font(45).render("りんごでいいですか？", True, "black")
                        applerect = appletext.get_rect(center=(800, 300))
                        screen.blit(appletext, applerect)
                        screen.blit(appleimg, (300,250))                        
                        choice2()
                    if grapebutton.checkForInput(choicemousepos):
                        screen.blit(skyimg, (0, 0))
                        grapetext = get_font(45).render("ぶどうでいいですか？", True, "black")
                        graperect = grapetext.get_rect(center=(800, 300))
                        screen.blit(grapetext, graperect)
                        screen.blit(grapeimg, (300,250))
                        choice2()
            pygame.display.update()
                

def choice2():
    while True:
        pygame.display.set_caption("choice2")
        choice2mousepos = pygame.mouse.get_pos()
        yesbutton = Button(image=pygame.image.load("box.png"), pos=(300, 500), text_input="はい", font=get_font(50), base_color="white", hovering_color="black")
        nobutton = Button(image=pygame.image.load("box.png"), pos=(950, 500), text_input="もどる", font=get_font(50), base_color="white", hovering_color="black")
        yesbutton.update(screen)
        nobutton.update(screen)
        for button in [yesbutton, nobutton]:
            button.changeColor(choice2mousepos)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yesbutton.checkForInput(choice2mousepos):
                    play()
                if nobutton.checkForInput(choice2mousepos):
                    choice()
        pygame.display.update()

def play():
    while True:
        pygame.display.set_caption("play")
        screen.blit(skyimg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()



def main():
    main_menu()






pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

skyimg = pygame.transform.rotozoom(pygame.image.load('sky.png'), 0, 2)
ninzinimg = pygame.image.load('ninzin.jpg')
kyuuriimg = pygame.image.load('kyuuri.jpg')
appleimg = pygame.image.load('apple.jpg')
grapeimg = pygame.image.load('grape.jpg')



main()
