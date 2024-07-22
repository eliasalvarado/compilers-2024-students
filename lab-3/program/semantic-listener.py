import sys
import datetime
from antlr4 import *
from ConfRoomSchedulerLexer import ConfRoomSchedulerLexer
from ConfRoomSchedulerParser import ConfRoomSchedulerParser
from ConfRoomSchedulerListener import ConfRoomSchedulerListener

class ConfRoomSchedulerSemanticChecker(ConfRoomSchedulerListener):
    def __init__(self):
        self.reservations = []

    def enterReserveStat(self, ctx):
        reservation = self.extractReservation(ctx)
        if self.is_overlapping(reservation):
            print(f"Error: Reserva solapada para {reservation['id']} en {reservation['date']} de {reservation['start']} a {reservation['end']}")
        else:
            self.reservations.append(reservation)
            print(f"Reserva válida: {reservation}")

    def extractReservation(self, ctx):
        reservation = {
            'id': ctx.ID().getText(),
            'date': ctx.DATE().getText(),
            'start': datetime.datetime.strptime(ctx.TIME(0).getText(), '%H:%M'),
            'end': datetime.datetime.strptime(ctx.TIME(1).getText(), '%H:%M')
        }
        return reservation

    def is_overlapping(self, new_reservation):
        for existing_reservation in self.reservations:
            if (existing_reservation['id'] == new_reservation['id'] and 
                existing_reservation['date'] == new_reservation['date'] and 
                not (new_reservation['end'] <= existing_reservation['start'] or 
                     new_reservation['start'] >= existing_reservation['end'])):
                return True
        return False

def main():
    input_stream = FileStream(sys.argv[1])
    lexer = ConfRoomSchedulerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ConfRoomSchedulerParser(stream)
    tree = parser.prog()
    
    semantic_checker = ConfRoomSchedulerSemanticChecker()
    walker = ParseTreeWalker()
    walker.walk(semantic_checker, tree)

if __name__ == '__main__':
    main()
