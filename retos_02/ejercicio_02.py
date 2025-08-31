luz_solar = bool(input())
humedad = int(input())
print(
    ["El sistema de riego no se activa.", "El sistema de riego se activa."][
        luz_solar != (humedad < 30)
    ]
)
