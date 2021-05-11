
from typing_extensions import runtime_checkable
import cv2
import numpy as np
import threading

from terminal_font import TerminalFont



class CvWindows():
    def __init__(self):
        self.name = 'origin'
        self.is_shown = True
        self.pos_x = 40
        self.pos_y = 30
        self.__showing_windows = {'origin':[True,40,30], 
                          'candy':[True,400,30], 
                          'chessboard':[False,40,300]
                          }

    def from_name(self, window_name):
        self.name = window_name
        self.is_shown = self.__showing_windows[window_name][0]
        self.pos_x = self.__showing_windows[window_name][1]
        self.pos_y = self.__showing_windows[window_name][2]
        return self

    def get_window(self,window_name):
        target = CvWindows()
        target.name = window_name
        target.is_shown = self.__showing_windows[window_name][0]
        target.pos_x = self.__showing_windows[window_name][1]
        target.pos_y = self.__showing_windows[window_name][2]
        return target

    def get_all_windows(self):
        return self.__showing_windows


class WarehouseRobot():

    def __init__(self):
        self.__mark_scanner = MarkScanner()
        self.__board_scanner = BoardScanner()
        self.__layout_scanner = LayoutScanner()
        self.__capture_device = cv2.VideoCapture(app.robot_eye.camera_index)

        self.windows={'original':'original','candy':'candy','chessboard':'chessboard'}
        self.__cvWindow = CvWindows()
        self.__thread_eyes = {}

        self.__target_x_position = 100
        self.__target_y_position = 30

        self.__FC_YELLOW = TerminalFont.Color.Fore.yellow
        self.__FC_RESET = TerminalFont.Color.Control.reset
        self.__MARK_STABLE_DEPTH = config.robot_eye.mark_scanner.stable_depth
        self.__LAYOUT_STABLE_DEPTH = config.robot_eye.layout_scanner.stable_depth


    def move_stone(self, relative_x, relative_y):
        x_dir = HIGH
        if relative_x < 0:
            x_dir = LOW
            relative_x = - relative_x
        set_gpio((x_dir_pin, x_dir)

        y_dir = HIGH
        if relative_y < 0:
            y_dir = LOW
            relative_y = - relative_y
        set_gpio(y_dir_pin,y_dir)


        max_step = max(relative_x,relative_y)
        for i in range(0,max_step):
            # send a step pluse
            if relative_x > 0:
                set_gpio(x_step_pin, HIGH)
                relative_x -= 1
            if relative_y > 0:
                set_gpio(y_step_pin, HIGH)
                relative_y -= 1
            delay_us(100)
            set_gpio(x_step_pin, LOW)
            set_gpio(y_step_pin, LOW)
            delay_us(100)

            

    def spin_once(self):
        # Take a picture from camera
        img = cv2.take_picture()
        
        # Get corners position from detecting aruco marks
        aruco_mark = cv2.detect_aruco(img)

        # Get perspective views the plane
        perspective_img = cv2.get_perspective_image(img, aruco_mark)
        
        # Get the stone position, will store the position to where? 
        x, y = get_stone_pistion(perspective_img, BLACK) 

        # How far is the stone to the target position?
        dx = self.__target_x_position - x_dir
        dy = self.__target_y_position - y_dir 

        # Control the plane motor to drive the stone move
        self.move_stone(dx, dy)
        
        

if __name__ == '__main__':
    # How can show two video window,  from one threads?
    # myrobotEye.start_show('candy')
    myrobot = WarehouseRobot()
    while True:
        myrotot.spin_once()