import bcrypt
# Esta puede venir de un formulario, ser leída con input o cualquier cosa
pass_texto_plano = "Jperez85!"

# Debemos tenerla como bytes
pass_texto_plano = pass_texto_plano.encode()

# La sal, necesaria para preparar nuestra contraseña
sal = bcrypt.gensalt()

# Hashear
pass_hasheada = bcrypt.hashpw(pass_texto_plano, sal)

#Nota: en casos reales no imprimas ni guardes en un log las contraseñas ni la sal
print("La contraseña en texto plano es '{}', la sal es '{}' y la hasheada es '{}'".format(pass_texto_plano, sal, pass_hasheada))

# Ahora vamos a comprobarla, recuerda que pass_hasheada puede provenir de tu base de datos o un lugar en donde la guardaste
print("Comprobando contraseñas...")
if bcrypt.checkpw(pass_texto_plano, pass_hasheada):
	print("Ok, las contraseñas coinciden")
else:
	print("Contraseña incorrecta")