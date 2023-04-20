import pygame
import random
import sys
import tkinter as tk

# Obtener la resolución de la pantalla del dispositivo
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Establecer las variables en un 40% del tamaño de la pantalla
screen_width = int(screen_width * 0.4)
screen_height = int(screen_height * 0.4)


def ball_animation(ball, ball_speed_x, ball_speed_y, player, opponent, player_score, opponent_score, score_time, pong_sound, score_sound):
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1

    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        collision_diff = ball.centery - player.centery
        if abs(collision_diff) < 10:
            ball_speed_x *= -1
        elif collision_diff < 0 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif collision_diff > 0 and ball_speed_y < 0:
            ball_speed_y *= -1

    if ball.colliderect(opponent) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        collision_diff = ball.centery - opponent.centery
        if abs(collision_diff) < 10:
            ball_speed_x *= -1
        elif collision_diff < 0 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif collision_diff > 0 and ball_speed_y < 0:
            ball_speed_y *= -1

    return ball, ball_speed_x, ball_speed_y, player_score, opponent_score, score_time


def opponent_animation(ball, opponent, opponent_speed):
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

    return opponent


def player_animation(player, player_speed):
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

    return player


def ball_restart(ball, ball_speed_x, ball_speed_y, screen_width, screen_height, game_font, light_grey, score_time):
    current_time = pygame
