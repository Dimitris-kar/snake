from turtle import Turtle
from food import Food
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.penup()
        segment.color('white')
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """moves the snake"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE)

    def up(self):
        """turn the snake to go Up(North)"""
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        """turn the snake to go Down(South)"""
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        """turn the snake to go Left(West)"""
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        """turn the snake to go Right(East)"""
        if self.head.heading() != LEFT:
            self.head.setheading(0)
