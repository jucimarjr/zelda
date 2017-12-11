from .abstract_builder import AbstractBuilder
from .planner.hotel import Hotel
from .planner.reservation import Reservation
from .planner.tickets import Tickets
from .planner.special_event import SpecialEvent

class VacationBuilder(AbstractBuilder):
    def __init__(self):
        self.__planner = dict()

    def build_day(self, date):
        if date not in self.__planner:
            self.__planner[date] = []

    def add_hotel(self, date, name):
        if date in self.__planner:
            hotel = Hotel(name)
            self.__planner[date].append(hotel)

    def add_reservation(self, date, name):
        if date in self.__planner:
            reserv = Reservation(name)
            self.__planner[date].append(reserv)

    def add_tickets(self, date, name, quantity = 1):
        if date in self.__planner:
            tickets = Tickets(name, quantity)
            self.__planner[date].append(tickets)
    
    def add_special_event(self, date, name):
        if date in self.__planner:
            event = SpecialEvent(name)
            self.__planner[date].append(event)

    def get_vacation_planner(self):
        return self.__planner