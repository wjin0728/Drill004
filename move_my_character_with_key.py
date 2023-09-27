from pico2d import *




TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
idle = []
run = []
idle_frame = [4,4,4,4]
run_frame = [6,6,6,6]

idle.append(load_image('knight_idle_front.png'))
idle.append(load_image('knight_idle_back.png'))
idle.append(load_image('knight_idle_front_right.png'))
idle.append(load_image('knight_idle_front_left.png'))

run.append(load_image('knight_run_front.png'))
run.append(load_image('knight_run_back.png'))
run.append(load_image('knight_run_front_right.png'))
run.append(load_image('knight_run_front_left.png'))

x = 600
y=500
frame = 0
rad = 0
dirX=0
dirY =0
looking =0

running = True

while (running):
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH/2, TUK_HEIGHT/2)
    if dirX ==0 and dirY == 0:
        idle[looking].clip_draw(frame*(int(idle[looking].w/idle_frame[looking])), 0, int(idle[1].w/idle_frame[looking]), idle[looking].h, x, y,int(idle[1].w/idle_frame[looking])*4, idle[looking].h*4)
    else:
        run[looking].clip_draw(frame * (int(run[looking].w / run_frame[looking])), 0,
                                int(run[looking].w / run_frame[looking]), run[looking].h, x, y, int(run[looking].w / run_frame[looking])*4, run[looking].h*4)
    update_canvas()
    if dirX == 0 and dirY == 0:
        frame = (frame+1)%idle_frame[looking]
    else:
        frame = (frame + 1) % run_frame[looking]
    delay(0.05)
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running=False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX=1
                looking = 2
            elif event.key == SDLK_LEFT:
                dirX=-1
                looking = 3
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_UP:
                dirY=1
                looking =1
            elif event.key == SDLK_DOWN:
                dirY=-1
                looking = 0
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX=0
            elif event.key == SDLK_LEFT:
                dirX=0
            elif event.key == SDLK_UP:
                dirY=0
            elif event.key == SDLK_DOWN:
                dirY=-0
    if x+dirX*10 > TUK_WIDTH:
        x = TUK_WIDTH
    elif x+dirX*10 < 0:
        x = 0
    else:
        x+=dirX*10
    if y + dirY * 10 > TUK_HEIGHT:
        y = TUK_HEIGHT
    elif y + dirY * 10 < 0:
        y = 0
    else:
        y += dirY * 10

close_canvas()