# TensorFlow HDF5 RCE PoC

Prueba de concepto para una vulnerabilidad de ejecución remota de código en TensorFlow (<= 2.13.1) usando archivos `.h5` maliciosos.

---

## Uso

1. Cambia la IP y puerto en el script.
2. Inicia un listener:

```bash
nc -lvnp <PUERTO>
```

3. Ejecuta el script para generar `malicious_model.h5`.
4. Sube el archivo a la aplicación vulnerable.
5. Obtén la shell reversa.

---

## Requisitos

* Python 3.x
* TensorFlow 2.13.1

---

## Aviso
Solo para uso educativo y entornos controlados. No me hago responsable por usos indebidos.

---
