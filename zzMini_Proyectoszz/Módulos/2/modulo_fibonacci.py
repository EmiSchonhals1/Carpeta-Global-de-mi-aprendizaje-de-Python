def fibonacci(tope):   # devuelve la sucesión de Fibonacci hasta el tope que le pongamos
    resultado = []
    a, b = 0, 1
    while (a < tope) :
        resultado.append(a)
        a = b
        b = a+b
    return resultado


#La sucesión comienza con los números 0 y 1, y a partir de estos, cada elemento es la suma de los dos anteriores. 
# A los elementos de esta sucesión se les llama números de Fibonacci
