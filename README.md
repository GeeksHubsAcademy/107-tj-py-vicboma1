<p align="center">
    <img src="https://github.com/GeeksHubsAcademy/2020-geekshubs-media/blob/master/image/logo.png" >	
</p>

    Considere el siguiente problema:

    Escriba un programa corto que permita obtener las letras de los elementos en posición par del array 
	y devuelva una string con la unión de los mismos
    
     N = 4 
    
         ['h', 'o', 'l', 'a', '!']
	i =    0    1    2    3    4

     Resultado
	 
         "hl!"

    
    En caso de que el array tenga un 'size' par, debe de contarse la última posición.
	En caso de que el array sea nulo, el resultado debe de devolver "nulo". 
	En caso de que el array sea vacío, el resultado debe de devolver "vacio". 
	El array no contiene valores nulos ni números, solamente letras.   
    
    Se atiente al siguiente ejemplo:
   
   	    N = 1        N = 2              N = 3                N = 4               
      
        ['h']        ['f', 'o']         ['f', 'o', 'o']      ['g', 'e', 'e', 'k']          
                 
    Resultado:
 	
	    "h"	 	 "fo"	   	    "foo"            	  "gek"        	              
                                  

    En la carpeta 'src/kata.py' se encuentra el fichero con la 
    definición de nuestro método vacío.
    En la carpeta 'tests/test_kata.py' se encuentra el fichero con la suite de test.
    
    El modus operandi de trabajo es el siguiente:
    
    Debes 'forkear' el proyecto a tu cuenta.
    Puedes hacer PR's ilimitadas e ir validando poco a poco la solución contra nuestro respositorio con CI.
    Puedes trabajar en local y subir la solución haciendo un PR a nuestro repositorio.
    Cuando se envíe la PR final, debes indicar el tiempo de dedicación y los intentos que has hecho.
    También puedes añadir un comentario para dar cualquier tipo de feedback.
    
    En caso de duda, revisa en el apartado de 'Referencias'.

    [Test Suite]

    tests/test_kata.py::Test_kata::test_apply_1 PASSED                       [  7%]
    tests/test_kata.py::Test_kata::test_apply_10 PASSED                      [ 14%]
    tests/test_kata.py::Test_kata::test_apply_11 PASSED                      [ 21%]
    tests/test_kata.py::Test_kata::test_apply_12 PASSED                      [ 28%]
    tests/test_kata.py::Test_kata::test_apply_13 PASSED                      [ 35%]
    tests/test_kata.py::Test_kata::test_apply_14 PASSED                      [ 42%]
    tests/test_kata.py::Test_kata::test_apply_2 PASSED                       [ 50%]
    tests/test_kata.py::Test_kata::test_apply_3 PASSED                       [ 57%]
    tests/test_kata.py::Test_kata::test_apply_4 PASSED                       [ 64%]
    tests/test_kata.py::Test_kata::test_apply_5 PASSED                       [ 71%]
    tests/test_kata.py::Test_kata::test_apply_6 PASSED                       [ 78%]
    tests/test_kata.py::Test_kata::test_apply_7 PASSED                       [ 85%]
    tests/test_kata.py::Test_kata::test_apply_8 PASSED                       [ 92%]
    tests/test_kata.py::Test_kata::test_apply_9 PASSED                       [100%]



## Referencias

* [Tutorial - Testing Automatizado](https://github.com/GeeksHubsAcademy/2020-js-vanilla-testing-FFFF/blob/master/README.md)
