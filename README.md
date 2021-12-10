# Crytpo VWAP

Crypto VWAP es un paquete python para el análisis de los precios de las criptomonedas en diferentes plataformas y analizar sus cambios de precios mendiante el indicador del VWAP

## Como usarlo

Hay varias formas de de ejecutar el siguiente paquete

### Heroku

Se ha desplegado este código en Heroku para su uso sin necesidad de instalar nada. Se puede encontrar en el enlace [https://cryptovwap.herokuapp.com/](https://cryptovwap.herokuapp.com/)

### pip

El paquete está disponible en el repositorio de código pip. Se puede instalar a través del comando 
```bash
pip install cryptovwap
```

Una vez instalado se podrá invocar mediante el comando de terminal
```bash
cryptovwap
```
### Clonando el repositorio

El paquete está disponible en [github](https://github.com/manso92/cryptovwap). Una vez clonado será necesario tener instalado python y el paquete poetry. Abriremos una terminal y ejecutamos los siguientes comandos:
```bash
poetry shell
poetry update
python app.py
```

## Calculo del VWAP

Este VWAP se ha calculado mediante la siguiente formula

<p align="center">
<a href="https://latex.codecogs.com/svg.latex?VWAP%20=%20\frac{\sum%20\text{Price}*\text{Volume}}{\sum%20\text{Volume}}">
  <img src="https://latex.codecogs.com/svg.latex?VWAP%20=%20\frac{\sum%20\text{Price}*\text{Volume}}{\sum%20\text{Volume}}"
       alt="Calculo del VWAP"/>
</a>
</p>

Esto se calcula mediante los siguientes pasos
- Para cada orden, calculamos el producto de precio por su volumen
- Sumamos ese calculo y el volumen al nivel que se quiere obtener el VWAP (minutos, horas)
- Para cada elemento calculamos la división
- El resultado es el vwap para cada punto definido

## Multiples Exchanges
Debido a las limitaciones que tiene la API de Kraken (requisito inicial del proyecto) se ha generado una interfaz abstracta para poder implementar todo el motor de precios sobre diferentes exchanges. Para este proyecto se han implementado los siguientes:
- [Kraken](https://www.kraken.com/)
- [Bitvavo](https://bitvavo.com/)

## Estándares de código
Para mejorár nuestro código se ha intentado desarrollar todo el código de cara al PEP8, un estándar en la industria para el código Python. Esta validación se ha realizado mediante el siguiente comando.
```bash
flake8 .
```