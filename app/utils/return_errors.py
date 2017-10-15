from flask import flash

def return_errors(form):
    lista=[]
    for field, errors in form.errors.items():
        for error in errors:
            lista.append("%s"%(error))
    return lista
