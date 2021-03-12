import sys
import random

from ursina import *
from ursina.prefabs.health_bar import HealthBar


class Player(Entity):
    def __init__(
        self,
        model="cube",
        scale=(1.5, 0.9, 0),
        color=color.black,
        position=(0, -6, 0),
        collider="box",
    ):
        super().__init__()
        self.model = model
        self.scale = scale
        self.color = color
        self.position = position
        self.collider = collider
        self.health = HealthBar(roundness=.5, value=50)

    def collid(self, other):
        hit_info = self.intersects()
        if hit_info.hit:
            if hit_info.entity == other:
                self.health.value -= 10

                if self.health.value == 0:
                    self.enabled = False
    
    def update(self):
        if held_keys["up arrow"]:
            self.y += 0.08
        elif held_keys["down arrow"]:
            self.y -= 0.08
        elif held_keys["right arrow"]:
            self.x += 0.08
        elif held_keys["left arrow"]:
            self.x -= 0.08


class Enemy(Entity):
    def __init__(
        self,
        model="cube",
        scale=(1.5, 0.9, 0),
        color=color.white,
        position=(0, 6, 0),
        collider="box",
    ):
        super().__init__()
        self.model = model
        self.scale = scale
        self.color = color
        self.position = position
        self.collider = collider

    def generate(self):
        spawn_rate_pos = (random.randint(-6, 5), 6)
        other = duplicate(self, position=spawn_rate_pos)

        return other
    
    def update(self):
        self.y -= 0.08


class PowerfulEnemy(Enemy):
    def __init__(
        self,
        model="circle",
        scale=(2.5, 1.9, 0),
        color=color.red,
        position=(0, 4, 0),
        collider="box",
    ):
        super().__init__(
            model=model, scale=scale, color=color, position=position, collider=collider
        )
    
    def transformation(self):
        shape = ["circle", "cube"]
        choice_shape = random.choice(shape)
        
        self.model = choice_shape