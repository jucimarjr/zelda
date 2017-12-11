from .vacation_builder import VacationBuilder

def print_planner(planner):
    for day in planner:
        print("Plans for day " + day)
        for item in planner[day]:
            print("- ", end='')
            item.print()
        print()

builder = VacationBuilder()

date = "11/12/2017"
builder.build_day(date)
builder.add_hotel(date, "Escola Superior de Tecnologia")
builder.add_tickets(date, "Carteira de Identificação Estudantil", 1)

date = "12/12/2017"
builder.build_day(date)
builder.add_hotel(date,"Sala do LUDUS")
builder.add_reservation(date,"Cadeira na frente")
builder.add_special_event(date,"Final de MPS 2017/2")

planner = builder.get_vacation_planner()
print_planner(planner)