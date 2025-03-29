# filepath: /workspaces/Estructuras_Datos/practicaColas/functions.py
def add_queue(ticket, ticket_types):
    controller = ticket_types.get(ticket.tipo.lower())
    if controller:
        controller.enqueue(ticket)
    else:
        raise ValueError("Tipo de ticket no válido")