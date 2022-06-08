# Proyecto Coderhouse - Entrega intermedia
Ejemplo de pagina web usada para almacenar blogs en cuentas propias - Leonel Bosch y Lautaro Gonzalez

Para poder correr el ejemplo asegurese que tiene python, Django, bootstrap y VSCode instalado;
Como instalar cada uno:
1. Instalar python: https://www.python.org/downloads/release/python-3913/
2. Instalar VSCode: https://code.visualstudio.com/Download
3. En VSCode instalar la extension de Python
4. En terminal escribir este codigo:

```bash
py pip install Django
```
Cuando se termine de instalar, instalaremos Bootstrap
```bash
pip install django-bootstrap-v5
```
5. Ahora clonamos el repositorio, y lo abrimos en VSCode
6. Lo hacemos correr:

```bash
py manage.py migrate
```
```bash
py manage.py runserver
```
Luego ingrese a [http://localhost:8000/blog](http://localhost:8000/blog)

Ahora hemos entrado en la pagina:
![image](https://user-images.githubusercontent.com/79726556/172502474-99962c61-74b9-4b6f-9ff2-0b3a82ff5011.png)

Vamos a crear un nuevo usuario:
1. Nos dirigimos a "Crear Cuenta"
2. ![image](https://user-images.githubusercontent.com/79726556/172502687-b976e6a3-328d-4f66-a33b-56c4903c6955.png)
3. Creamos una cuenta con nuestros datos:
![image](https://user-images.githubusercontent.com/79726556/172502832-eafeb873-9a1d-4d4b-9641-dd47d08ee09b.png)
4. Automaticamente que hemos terminado de crear nuestra cuenta, nos pedira ingresar a nuestra cuenta por primera vez: ![image](https://user-images.githubusercontent.com/79726556/172503208-816ee87e-17fa-40c6-a3f6-b71869d8826a.png)

Ahora entraste a tu cuenta, esta es la pagina de bienvenida:
![image](https://user-images.githubusercontent.com/79726556/172503406-bc73b5e9-293a-4886-bbde-57c7cae3549f.png)

Ahora puedes ir a "Nuevo Blog" para crear un blog
![image](https://user-images.githubusercontent.com/79726556/172503763-7668925f-eadb-4c1c-bca7-770eb062a716.png)

En la pagina de Nuevo Blog podras agregar un Titulo, Subtitulo y un Cuerpo
![image](https://user-images.githubusercontent.com/79726556/172503890-ade831a2-5f7f-45ec-b79b-ab48bb4647fc.png)
