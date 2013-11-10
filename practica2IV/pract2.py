#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
from web import form
from web.contrib.template import render_mako
import dbm

# Para poder usar sesiones con web.py
web.config.debug = False
        
urls = (
    '/hello', 'hello',
    '/imagen', 'imagen',
    '/formulario' , 'index',
    '/formulario3', 'fomulprac3',
    '/template', 'templ',
    '/inicio', 'inicio',
    '/logout', 'logout',
    '/insercion', 'insercion',
    '/datos', 'datos',
    '/modifica', 'modifica',
    '/guarda', 'guarda',
    '/(.*)', 'error'
)

app = web.application(urls, globals())
plantilla = web.template.render('./templates/')


####################################################

session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'usuario':''})

# Templates de mako
render = render_mako (
	directories = ['templates'],
	input_encoding = 'utf-8',
	output_encoding = 'utf-8')


login_form = form.Form (
	form.Textbox ('username', form.notnull, description='Usuario:'),
	form.Password ('password', form.notnull, description=u'Contraseña:'),
	form.Button ('Login'),
)


def password_correcto_de (usuario):
	return usuario	+'3'         # concateno un '3' al nombre de usuario
    # En la realidad habría que guardar los
    # passwords de cada usuario en una base de datos


def comprueba_identificacion (): 
	usuario = session.usuario   # Devuelve '' cuando no está identificado
	return usuario              # que es el usuario inicial 
                                  


class logout:
	def GET(self):
		usuario = session.usuario
		session.kill()
		return 'adios ' + usuario



# Comprueba que el usuario esté identificado
# sino se lo pide
class inicio:
	def GET(self):
		usuario = comprueba_identificacion () 
		if usuario:
			return web.seeother('/template') # render.inicio (usuario = usuario)
		else:
			form = login_form ()
			return render.login(form=form, usuario=usuario)  
	def POST(self):

		form = login_form ()
		if not form.validates ():
			return render.login (form=form, usuario='', mensaje = '')

		i = web.input()
		usuario  = i.username
		password = i.password
		if password == password_correcto_de (usuario):
			session.usuario = usuario
			return web.seeother('/template')   # Redirige al formulario
		else:
			form = login_form ()
			return render.login (form=form, usuario='', 
                                 mensaje = u'[ERROR] - El password correcto que sería ' +
                                           password_correcto_de (usuario))




###################################################

formu = form.Form(
	form.Textbox("nombre", form.notnull),
	form.Textbox("otro", form.notnull),
   form.Button("Enviar")
)


form_pract3 = form.Form(
	form.Textbox("Nombre", form.notnull),
	form.Textbox("Apellidos", form.notnull),
	form.Textbox("DNI", form.notnull, form.regexp('^([0-9]{8}[A-Z])$', "Formato de DNI no valido")),
	form.Textbox("email", form.notnull, form.regexp('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$', "Formato de correo incorrecto")), 
	form.Textbox("VISA", form.notnull, form.regexp('^([0-9]{4}) ([0-9]{4}) ([0-9]{4}) ([0-9]{4})|([0-9]{4})-([0-9]{4})-([0-9]{4})-([0-9]{4})$', "Formato de tarjeta VISA no valido")),
	form.Dropdown("dia",[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31], description="Día de nacimiento"),
	form.Dropdown("mes",[1,2,3,4,5,6,7,8,9,10,11,12], description="Mes de nacimiento"),
	form.Dropdown("anio",[1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014], description="Año de nacimiento"),
	form.Textarea("Direccion", form.notnull),
	form.Password("Contrasenia", form.notnull, post = "Su contraseña debe de tener mas de 7 caracteres"),
	form.Password("Verificacion", form.notnull, pre= "Repita su contraseña"),
	form.Radio("pago", ['Contra reembolso', 'VISA'],form.notnull),
	form.Checkbox("clausulas",form.Validator("Debes aceptar las cláusulas de la protección de datos", lambda i: "clausulas" not in i), description="Acepta las clausulas"),
	form.Button("Enviar"),
	validators = [form.Validator("No coinciden las contraseñas", lambda i: i.Contrasenia == i.Verificacion), form.Validator("Longitud de contraseña", lambda i: len(i.Contrasenia)>=7), form.Validator("Fecha de nacimiento no válida.", lambda i: (((int(i.mes) == 2) and ((int(i.dia) <= 28) and ((int(i.anio) % 4) != 0) or (int(i.dia) <= 29) and ((int(i.anio) % 4) == 0))) or ((int(i.dia) <= 30) and ((int(i.mes) == 4) or (int(i.mes) == 6) or (int(i.mes) == 9) or (int(i.mes) == 11)))))]	
)

form_pract4 = form.Form(
    form.Textbox("DNI", form.notnull, description='Inserte el usuario'),
    form.Button("Enviar")
)

form_pract5 = form.Form(
	form.Textbox("Nombre", form.notnull),
	form.Textbox("Apellidos", form.notnull),
	form.Textbox("DNI", form.notnull, form.regexp('^([0-9]{8}[A-Z])$', "Formato de DNI no valido")),
	form.Textbox("email", form.notnull, form.regexp('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$', "Formato de correo incorrecto")), 
	form.Textbox("VISA", form.notnull, form.regexp('^([0-9]{4}) ([0-9]{4}) ([0-9]{4}) ([0-9]{4})|([0-9]{4})-([0-9]{4})-([0-9]{4})-([0-9]{4})$', "Formato de tarjeta VISA no valido")),
	form.Dropdown("dia",[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31], description="Día de nacimiento"),
	form.Dropdown("mes",[1,2,3,4,5,6,7,8,9,10,11,12], description="Mes de nacimiento"),
	form.Dropdown("anio",[1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014], description="Año de nacimiento"),
	form.Textarea("Direccion", form.notnull),
	form.Password("Contrasenia", form.notnull, post = "Su contraseña debe de tener mas de 7 caracteres"),
	form.Password("Verificacion", form.notnull, pre= "Repita su contraseña"),
	form.Radio("pago", ['Contra reembolso', 'VISA'],form.notnull),
	form.Checkbox("clausulas",form.Validator("Debes aceptar las cláusulas de la protección de datos", lambda i: "clausulas" not in i), description="Acepta las clausulas"),
	form.Button("Enviar"),
	validators = [form.Validator("No coinciden las contraseñas", lambda i: i.Contrasenia == i.Verificacion), form.Validator("Longitud de contraseña", lambda i: len(i.Contrasenia)>=7), form.Validator("Fecha de nacimiento no válida.", lambda i: (((int(i.mes) == 2) and ((int(i.dia) <= 28) and ((int(i.anio) % 4) != 0) or (int(i.dia) <= 29) and ((int(i.anio) % 4) == 0))) or ((int(i.dia) <= 30) and ((int(i.mes) == 4) or (int(i.mes) == 6) or (int(i.mes) == 9) or (int(i.mes) == 11)))))]	
)

class hello:
	def GET(self):
		name = 'Desarrollo de app para internet'
		return 'Practica 2 -' + name


class imagen:        
   def GET(self):
   	return '<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>practica2</title></head><body><img src="static/images/etsiit.jpg" alt="imagen1"/><img src="static/images/logougr.jpg" alt="imagen"/></body></html>' 

class index:
	def GET(self):
		form = formu()
		return plantilla.formulario(form)

	def POST(self):
		form = formu()
		if not form.validates():
			return plantilla.formulario(form)
		else:
			return "Mensaje enviado correctamente %s %s" % (form.d.nombre, form.d.otro)

#Practica 3
class fomulprac3:
	def GET(self):
		form = form_pract3()
		return plantilla.formulario(form)

	def POST(self):
		form = form_pract3()
		if not form.validates():
			return plantilla.formulario(form)
		else:
			return "Formulario practica 3 enviado correctamente" #%s %s" % (form.d.nombre, form.d.otro)	


class templ:
	def GET(self):
		usuario = comprueba_identificacion () 
		form = form_pract3()
		if usuario:
			return render.inicio (usuario = usuario, form = form, mensaje='')
		else:
			form = login_form ()
			return render.login(form=form, usuario=usuario)
	def POST(self):
	    return web.seeother('/insercion')
	
		 
class insercion:
    def GET(self):
	usuario = comprueba_identificacion () 
	form = form_pract3()
	return render.insercion (usuario = usuario, form = form)
    def POST(self):
	usuario = comprueba_identificacion () 
	form = form_pract3()
	if not form.validates():
	    return render.insercion (usuario = usuario, form = form)
	else:
	    db=dbm.open(form.d.DNI, 'c')
	    
	    db['Nombre']=form.d.Nombre
	    db['Apellidos']=form.d.Apellidos
	    db['Dia']=form.d.dia
	    db['Mes']=form.d.mes
	    db['Anio']=form.d.anio
	    db['DNI']=form.d.DNI
	    db['VISA']=form.d.VISA
	    db['email']=form.d.email
	    db['Direccion']=form.d.Direccion
	    db['Contrasenia']=form.d.Contrasenia
	    db['pago']=form.d.pago
	    
	    db.close()
	    
	    return render.inicio(usuario=usuario, form=form, mensaje='los datos han sido insertados correctamente')

class datos:
    def GET(self):
	usuario = comprueba_identificacion () 
	form = form_pract4()
	return render.datos (usuario = usuario, form = form)
    def POST(self):
	usuario = comprueba_identificacion () 
	form = form_pract4()
	if not form.validates():
	   return render.datos (usuario = usuario, form = form)
	else:
	    try:
		db=dbm.open(form.d.DNI, 'r')
		
		nombre=db['Nombre']
		apellidos=db['Apellidos']
		dia=db['Dia']
		mes=db['Mes']
		anio=db['Anio']
		nacimiento= dia + '/' + mes + '/' + anio
		dni=db['DNI']
		visa=db['VISA']
		email=db['email']
		direccion=db['Direccion']
		contrasenia=db['Contrasenia']
		pago=db['pago']
		
		db.close()	
	    
		return render.vista(form=form, usuario=usuario, nombre=nombre, apellidos=apellidos, nacimiento=nacimiento, dni=dni, visa=visa, email=email, direccion=direccion, contrasenia=contrasenia, pago=pago)
	    except:
		return render.inicio(form=form, usuario=usuario, mensaje="Usuario no existente en la base de datos.")
class modifica:
    def GET(self):
	usuario = comprueba_identificacion ()
	form = form_pract4()
	return render.datos (usuario = usuario, form = form)	
    def POST(self):
	usuario = comprueba_identificacion () 
	form = form_pract4()
	if not form.validates():
	   return render.datos (usuario = usuario, form = form)
	else:
	    try:
		db=dbm.open(form.d.DNI, 'r')
		
		nombre=db['Nombre']
		apellidos=db['Apellidos']
		dia=db['Dia']
		mes=db['Mes']
		anio=db['Anio']
		dni=db['DNI']
		visa=db['VISA']
		pago=db['pago']
		email=db['email']
		direccion=db['Direccion']
		contrasenia=db['Contrasenia']
		
		formi = form_pract3()
		
		formi.Nombre.value = nombre
		formi.Apellidos.value = apellidos
		formi.dia.value = int(dia)
		formi.mes.value = int(mes)
		formi.anio.value= int(anio)
		formi.DNI.value = dni
		formi.VISA.value = visa
		formi.pago.value = pago
		formi.email.value = email
		formi.Direccion.value = direccion
		formi.Contrasenia.value = contrasenia
		formi.Verificacion.value = contrasenia
		
		db.close()		
		
		return render.guarda(form=formi, usuario=usuario)
	    except:
		return render.inicio(form=form, usuario=usuario, mensaje="Usuario no existente en la base de datos.")
    
class guarda:
    def GET(self):
	usuario = comprueba_identificacion () 
	form = form_pract4()
	if not form.validates():
	   return render.datos (usuario = usuario, form = form)
	else:
	    try:
		db=dbm.open(form.d.DNI, 'r')
		
		nombre=db['Nombre']
		apellidos=db['Apellidos']
		dia=db['Dia']
		mes=db['Mes']
		anio=db['Anio']
		dni=db['DNI']
		visa=db['VISA']
		pago=db['pago']
		email=db['email']
		direccion=db['Direccion']
		contrasenia=db['Contrasenia']
		
		formi = form_pract3()
		
		formi.Nombre.value = nombre
		formi.Apellidos.value = apellidos
		formi.dia.value = int(dia)
		formi.mes.value = int(mes)
		formi.anio.value= int(anio)
		formi.DNI.value = dni
		formi.VISA.value = visa
		formi.pago.value = pago
		formi.email.value = email
		formi.Direccion.value = direccion
		formi.Contrasenia.value = contrasenia
		formi.Verificacion.value = contrasenia
		
		db.close()		
		
		return render.guarda(form=formi, usuario=usuario)
	    except:
		return render.inicio(form=form, usuario=usuario, mensaje="Usuario no existente en la base de datos.")
	    
    def POST(self):
	usuario = comprueba_identificacion () 
	form = form_pract3()
	if not form.validates():
	    return render.insercion (usuario = usuario, form = form)
	else:
	    db=dbm.open(form.d.DNI, 'w')
	    
	    db['Nombre']=form.d.Nombre
	    db['Apellidos']=form.d.Apellidos
	    db['Dia']=form.d.dia
	    db['Mes']=form.d.mes
	    db['Anio']=form.d.anio
	    db['DNI']=form.d.DNI
	    db['VISA']=form.d.VISA
	    db['email']=form.d.email
	    db['Direccion']=form.d.Direccion
	    db['Contrasenia']=form.d.Contrasenia
	    db['pago']=form.d.pago
	    
	    db.close()
	    
	    return render.inicio(usuario=usuario, form=form, mensaje='los datos han sido insertados correctamente')


class error:
   def GET(self, name):
	return '<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>ERROR</title></head><body><header>[ERROR 404] - NOT FOUND</header></body></html>' 

if __name__ == "__main__":
    app.run()
