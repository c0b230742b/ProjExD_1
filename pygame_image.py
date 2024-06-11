import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img =pg.transform.flip(kk_img, True, False)
    tmr = 0
    width = 0
    while True:
        width += 1
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        width = tmr%3200

        screen.blit(bg_img, [-width, 0])
        screen.blit(bg_img2, [-width+1600, 0])
        screen.blit(bg_img, [-width+3200, 0])
        screen.blit(bg_img2, [-width+4800, 0])
        kk_rect = kk_img.get_rect() #こうかとんRectの抽出
        kk_rect.center = 300, 200
        screen.blit(kk_img, kk_rect) #kk_imgをkk_rectの設定に従って貼り付け
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()