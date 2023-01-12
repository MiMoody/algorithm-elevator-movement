from enum import Enum, auto
import time
import uuid


class ElevatorState(Enum):
    MOVING = auto()
    WAIT = auto()


class ElevatorDirection(Enum):
    UP = auto()
    DOWN = auto()
    STAND = auto()


class Elevator():
    
    def __init__(self,):
        
        self._id = uuid.uuid1()
        self._current_floor = 0
        self._state = ElevatorState.WAIT
        self._direction = ElevatorDirection.STAND
        self._queue_floor = []
    
    @property
    def direction(self):
        return self._direction

    @property
    def current_floor(self):
        return self._current_floor
    
    def _move_up(self):
        """ Движение лифта вверх """
        
        self._direction = ElevatorDirection.UP
        self._current_floor +=1
        print(f"[{self._id}] Лифт поднимается на {self._current_floor} этаж")
        time.sleep(1)
    
    def _move_down(self):
        """ Движение лифта вниз """
        
        self._direction = ElevatorDirection.DOWN
        self._current_floor -=1
        print(f"[{self._id}] Лифт спускается на {self._current_floor} этаж")
        time.sleep(1)
        
    def call(self, floor :int):
        """ Функция для вызова лифта на определенный этаж """
        
        if floor not in self._queue_floor:
            self._queue_floor.append(floor)
        if self._state == ElevatorState.WAIT:
            self._start()
            
    def _stop(self, floor :int):
        """ Остановка лифта на этаже """
        
        print(f"[{self._id}] Лифт остановился на этаже {floor}")
        if floor in self._queue_floor:
            self._queue_floor.remove(floor)
        time.sleep(1)
    
    def _start(self):
        """ Запуск лифта """
        
        while  self._queue_floor:
            self._state = ElevatorState.MOVING
            call_floor = self._queue_floor.pop(0)
            while call_floor != self._current_floor:
                if self._current_floor in self._queue_floor:
                    self._stop(self._current_floor)
                self._move_up() if self._current_floor < call_floor else self._move_down()
            self._stop(call_floor)
        self._state = ElevatorState.WAIT
            
elevator = Elevator()
elevator.call(3)
elevator.call(6)
elevator.call(4)
elevator.call(0)
elevator.call(1)


                    
            
            