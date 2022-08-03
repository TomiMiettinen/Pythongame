import pygame
import random

class OmaPeli:
    def __init__(self):
        pygame.init()

        self.uusi_peli()

        self.robo = pygame.image.load("robo.png")
        self.kolikko = pygame.image.load("kolikko.png")
        self.hirvio = pygame.image.load("hirvio.png")
        self.ovi = pygame.image.load("ovi.png")

        self.korkeus = 600
        self.leveys = 800
        self.robo_x = self.leveys/2 - self.robo.get_width()
        self.robo_y = self.korkeus/2 - self.robo.get_height()
        self.kolikko_x_max = self.leveys - self.kolikko.get_width()
        self.kolikko_y_max = self.korkeus - self.kolikko.get_height() - 20
        self.kolikko_x = random.randint(0, self.kolikko_x_max)
        self.kolikko_y = random.randint(0, self.kolikko_y_max)
        self.ovi_y = self.korkeus - self.ovi.get_height() - 10
        self.ovi_x = self.leveys - self.ovi.get_width()
        self.hirvio_kohde_x = random.randint(0, self.kolikko_x_max)
        self.hirvio_kohde_y = random.randint(0, self.kolikko_y_max)
        self.hirvio_x = self.ovi_x
        self.hirvio_y = self.ovi_y
        

        self.kello = pygame.time.Clock()
        
        self.naytto = pygame.display.set_mode((self.leveys, self.korkeus + 10))

        self.fontti = pygame.font.SysFont("Arial", 24)
        pygame.display.set_caption("Ei tästä tule mitään")
        self.silmukka()

    def uusi_peli(self):

        self.tappio = False
        self.oikea = False
        self.vasen = False
        self.ylos = False
        self.alas = False
        self.pisteet = 0
        self.hirvio_vauhti = 0

    def silmukka(self):
        while True:
            self.tutki_tapahtumat()
            self.piirra_naytto()

    def tutki_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasen = True
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikea = True
                if tapahtuma.key == pygame.K_UP:
                    self.ylos = True
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas = True
                if tapahtuma.key == pygame.K_RETURN:
                    self.uusi_peli()

            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasen = False
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikea = False
                if tapahtuma.key == pygame.K_UP:
                    self.ylos = False
                if tapahtuma.key == pygame.K_DOWN:
                    self.alas = False
                
                if tapahtuma.key == pygame.K_ESCAPE:
                    exit()
            if tapahtuma.type == pygame.QUIT:
                exit()

        if self.oikea and self.robo_x <= self.leveys - self.robo.get_width():
            self.robo_x += 4
        if self.vasen and self.robo_x >= 0:
            self.robo_x -= 4
        if self.ylos and self.robo_y >= 0:
            self.robo_y -= 4
        if self.alas and self.robo_y <= self.korkeus - self.robo.get_height() - 20:
            self.robo_y += 4

        self.kolikot()
        self.hirviotmethod()

    def piirra_naytto(self):
        self.naytto.fill((0, 155, 50))
        if not self.tappio:
            self.naytto.blit(self.robo, (self.robo_x, self.robo_y))
            self.naytto.blit(self.kolikko, (self.kolikko_x, self.kolikko_y))
            self.naytto.blit(self.hirvio, (self.hirvio_x, self.hirvio_y))
        self.naytto.blit(self.ovi, (self.ovi_x, self.ovi_y))
        
        
        teksti = self.fontti.render("Coins: " + str(self.pisteet), True, (255, 0, 0))
        pygame.draw.rect(self.naytto, (115,147,179), rect=(0,self.korkeus-5-teksti.get_height()//2,self.leveys,teksti.get_height()))
        self.naytto.blit(teksti, (25, self.korkeus - 20))
        teksti = self.fontti.render("Enter = New game", True, (255, 0, 0))
        self.naytto.blit(teksti, (200, self.korkeus - 20))
        teksti = self.fontti.render("Esc = Exit", True, (255, 0, 0))
        self.naytto.blit(teksti, (400, self.korkeus - 20))

        if self.tappio:
            teksti = self.fontti.render("You lose. Pisteet:" + str(self.pisteet), True, (255, 0, 0))
            teksti_x = self.leveys / 2 - teksti.get_width() / 2
            teksti_y = self.korkeus / 2 - teksti.get_height() / 2
            pygame.draw.rect(self.naytto, (0, 0, 0), (teksti_x, teksti_y, teksti.get_width(), teksti.get_height()))
            self.naytto.blit(teksti, (teksti_x, teksti_y))
            self.hirvio_x = self.ovi_x
            self.hirvio_y = self.ovi_y
        self.kello.tick(60)
        pygame.display.flip()

    def kolikot(self):
        self.robo_keski = self.robo_x + self.robo.get_width()/2
        self.kolikko_keski = self.kolikko_x + self.kolikko.get_width()/2
        self.robo_keski_y = self.robo_y + self.robo.get_height()/2
        self.kolikko_keski_y = self.kolikko_y + self.kolikko.get_height()/2
        if abs(self.robo_keski - self.kolikko_keski) <= (self.robo.get_width() + self.kolikko.get_width())/2 and abs(self.robo_keski_y - self.kolikko_keski_y) <= (self.robo.get_height() + self.kolikko.get_height())/2:
            self.kolikko_x = random.randint(0, self.kolikko_x_max)
            self.kolikko_y = random.randint(0, self.kolikko_y_max)
            self.pisteet += 1

    def hirviotmethod(self):
        if self.pisteet % 5 == 0 and self.pisteet > 0:
            self.hirvio_vauhti = random.randint(1, 6)

        if self.hirvio_x in range(self.hirvio_kohde_x - 10, self.hirvio_kohde_x + 10) and self.hirvio_y in range (self.hirvio_kohde_y - 10, self.hirvio_kohde_y + 10):
            self.hirvio_kohde_x = random.randint(0, self.kolikko_x_max)
            self.hirvio_kohde_y = random.randint(0, self.kolikko_y_max)
        
        if self.hirvio_x < self.hirvio_kohde_x:
            self.hirvio_x += self.hirvio_vauhti

        if self.hirvio_x > self.hirvio_kohde_x:
            self.hirvio_x -= self.hirvio_vauhti

        if self.hirvio_y < self.hirvio_kohde_y:
            self.hirvio_y += self.hirvio_vauhti

        if self.hirvio_y > self.hirvio_kohde_y:
            self.hirvio_y -= self.hirvio_vauhti
            
        self.robo_keski = self.robo_x + self.robo.get_width()/2
        self.hirvio_keski = self.hirvio_x + self.hirvio.get_width()/2
        self.robo_keski_y = self.robo_y + self.robo.get_height()/2
        self.hirvio_keski_y = self.hirvio_y + self.hirvio.get_height()/2
        if abs(self.robo_keski - self.hirvio_keski) <= (self.robo.get_width() + self.hirvio.get_width())/2 and abs(self.robo_keski_y - self.hirvio_keski_y) <= (self.robo.get_height() + self.hirvio.get_height())/2:
            self.tappio = True

if __name__ == "__main__":
    OmaPeli()