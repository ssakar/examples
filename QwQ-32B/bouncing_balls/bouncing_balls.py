import tkinter as tk
import math
import numpy as np
from dataclasses import dataclass
from typing import List, Tuple

color_list = [
    '#f8b862', '#f6ad49', '#f39800', '#f08300', '#ec6d51', '#ee7948', '#ed6d3d', '#ec6800',
    '#ec6800', '#ee7800', '#eb6238', '#ea5506', '#ea5506', '#eb6101', '#e49e61', '#e45e32',
    '#e17b34', '#dd7a56', '#db8449', '#d66a35'
]

@dataclass
class Ball:
    x: float
    y: float
    vx: float
    vy: float
    radius: float
    color: str
    number: int

    def update(self, gravity: float, friction: float):
        self.vy += gravity
        self.vx *= friction
        self.vy *= friction
        self.x += self.vx
        self.y += self.vy

    def draw(self, canvas: tk.Canvas):
        canvas.create_oval(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
            fill=self.color,
            outline='black'
        )
        canvas.create_text(
            self.x,
            self.y,
            text=str(self.number),
            fill='black',
            font=('Arial', int(self.radius * 1.5))
        )
        if (self.vx**2 + self.vy**2) > 0.1:
            angle = math.atan2(self.vy, self.vx)
            length = self.radius * 0.3
            dx = length * math.cos(angle)
            dy = length * math.sin(angle)
            canvas.create_line(
                self.x,
                self.y,
                self.x + dx,
                self.y + dy,
                fill='black',
                arrow=tk.LAST
            )

@dataclass
class Heptagon:
    center_x: float
    center_y: float
    radius: float
    rotation_angle: float
    vertices: List[Tuple[float, float]] = None

    def update_rotation(self, delta_angle: float):
        self.rotation_angle += delta_angle
        self.rotation_angle %= (2 * math.pi)
        self.vertices = []
        for i in range(7):
            angle = self.rotation_angle + (2 * math.pi / 7) * i
            x = self.center_x + self.radius * math.cos(angle)
            y = self.center_y + self.radius * math.sin(angle)
            self.vertices.append((x, y))

    def compute_edges(self) -> List[Tuple[Tuple[float, float], Tuple[float, float]]]:
        edges = []
        for i in range(7):
            v1 = self.vertices[i]
            v2 = self.vertices[(i + 1) % 7]
            edges.append((v1, v2))
        return edges

    def draw(self, canvas: tk.Canvas):
        coords = []
        for (x, y) in self.vertices:
            coords.extend([x, y])
        canvas.create_polygon(coords, outline='black', fill='', width=2)

def main():
    root = tk.Tk()
    root.title("Bouncing Balls in Spinning Heptagon")
    canvas_width = 800
    canvas_height = 800
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
    canvas.pack()

    center_x = canvas_width / 2
    center_y = canvas_height / 2
    heptagon_radius = 300
    ball_radius = 10

    balls = []
    for i in range(20):
        color = color_list[i]
        x = center_x
        y = center_y
        vx = np.random.uniform(-0.5, 0.5)
        vy = np.random.uniform(-0.5, 0.5)
        ball = Ball(x, y, vx, vy, ball_radius, color, i + 1)
        balls.append(ball)

    heptagon = Heptagon(center_x, center_y, heptagon_radius, 0.0)

    gravity = 0.3
    friction = 0.99
    restitution_wall = 0.8

    rotation_speed_deg_per_sec = 72
    rotation_speed_rad_per_sec = rotation_speed_deg_per_sec * math.pi / 180
    delta_t = 1 / 60
    delta_angle = rotation_speed_rad_per_sec * delta_t

    def animate():
        canvas.delete("all")

        heptagon.update_rotation(delta_angle)
        edges = heptagon.compute_edges()

        for ball in balls:
            ball.update(gravity, friction)

        for ball in balls:
            for edge in edges:
                v1, v2 = edge
                dx_edge = v2[0] - v1[0]
                dy_edge = v2[1] - v1[1]
                length = math.hypot(dx_edge, dy_edge)
                if length == 0:
                    continue

                normal_x = -dy_edge / length
                normal_y = dx_edge / length

                cross = dx_edge * (ball.y - v1[1]) - dy_edge * (ball.x - v1[0])
                distance = abs(cross) / length

                if distance < ball.radius:
                    displacement_x = normal_x * (ball.radius - distance)
                    displacement_y = normal_y * (ball.radius - distance)
                    ball.x += displacement_x
                    ball.y += displacement_y

                    dot_product = ball.vx * normal_x + ball.vy * normal_y
                    factor = (1 + restitution_wall) * dot_product
                    ball.vx -= factor * normal_x
                    ball.vy -= factor * normal_y

        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                ball1 = balls[i]
                ball2 = balls[j]
                dx = ball2.x - ball1.x
                dy = ball2.y - ball1.y
                distance_sq = dx**2 + dy**2
                if distance_sq < (2 * ball_radius)**2:
                    distance = math.sqrt(distance_sq)
                    n_x = dx / distance
                    n_y = dy / distance

                    v_rel_x = ball1.vx - ball2.vx
                    v_rel_y = ball1.vy - ball2.vy
                    dot = v_rel_x * n_x + v_rel_y * n_y

                    delta_v1 = dot * n_x
                    delta_v2 = dot * n_y

                    ball1.vx -= delta_v1
                    ball1.vy -= delta_v2
                    ball2.vx += delta_v1
                    ball2.vy += delta_v2

                    overlap = (2 * ball_radius - distance) / 2
                    ball1.x -= n_x * overlap
                    ball1.y -= n_y * overlap
                    ball2.x += n_x * overlap
                    ball2.y += n_y * overlap

        heptagon.draw(canvas)
        for ball in balls:
            ball.draw(canvas)

        canvas.after(16, animate)

    animate()
    root.mainloop()

if __name__ == "__main__":
    main()