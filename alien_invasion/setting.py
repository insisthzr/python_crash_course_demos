#!/usr/local/bin/python3.6


class Setting():
    def __init__(self):
        # global
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.speedup_scale = 2
        self.score_scale = 2
        self.initialize_dynamic_setting()

        # ship
        self.ship_limit = 3

        # bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # alien
        self.fleet_drop_speed = 10

    def initialize_dynamic_setting(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
