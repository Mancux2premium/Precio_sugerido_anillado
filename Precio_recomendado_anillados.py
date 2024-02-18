### Precio de los insumos para la realizacion de los anillado, sin tener en cuenta los espirales ###
tapas_negras_blancas_precio = 17660
costo_envio = 4549
tapas_negras_blancas_rendimiento = 50 

### Fomula que calcula el costo de los insumos ###
coste_anillado = int((tapas_negras_blancas_precio + costo_envio) / tapas_negras_blancas_rendimiento)

### Fomula que calcula el precio recomendado ###
precio_recomendado_anillado = int(coste_anillado * 2)


### Muestra el mensaje del costo por anillado, mas una recomendacion de precio a vender ###
print("Cada anillado te sale:","$",coste_anillado,"\n""Te sugerimos poner el precio del anillado a:","$",precio_recomendado_anillado,)