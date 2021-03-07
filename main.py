import random
import things

from ursina import *


app = Ursina()

# window setting
window.title = "asterobit"
window.size = (600, 500)
window.borderless = False
window.exit_button.enabled = False

# create entity
player = things.Player()
enemy = things.Enemy()
powerful_enemy = things.PowerfulEnemy()

# first append
enemy_entity = []
enemy_entity.append(enemy)
enemy_entity.append(powerful_enemy)

def update():
    global enemy
    global powerful_enemy

    player.movement()

    for entity in enemy_entity:
        entity.movement()

        player.collid(entity)
    
    line_appeared_enemy = random.randint(-4, -1)
    if enemy.y <= line_appeared_enemy or powerful_enemy.y <= line_appeared_enemy:
        enemy = enemy.generate()
        powerful_enemy = powerful_enemy.generate()

        powerful_enemy.transformation()

        enemy_entity.append(enemy)
        enemy_entity.append(powerful_enemy)

    # if powerful_enemy.y <= line_appeared_enemy:
    #     powerful_enemy = powerful_enemy.generate()
    #     powerful_enemy.transformation()
    #     enemy_entity.append(powerful_enemy)

app.run()