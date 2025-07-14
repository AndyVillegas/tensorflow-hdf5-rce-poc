# TensorFlow HDF5 RCE PoC

Prueba de concepto para una vulnerabilidad de ejecución remota de código en TensorFlow (<= 2.13.1) usando archivos `.h5` maliciosos.

---

## Descripción

El archivo `malicious_model.h5` generado por este script contiene una capa `Lambda` maliciosa que ejecuta una reverse shell al cargarse en una aplicación vulnerable.

---

## Uso

1. Cambia la IP y puerto del atacante en el script Python.
2. Inicia un listener:

   ```bash
   nc -lvnp <PUERTO>
   ```
3. Ejecuta el script para generar `malicious_model.h5`.
4. Sube el archivo a la aplicación vulnerable que utilice TensorFlow.
5. Obtén la shell reversa cuando el modelo sea cargado.

---

## Requisitos

* Python 3.x
* TensorFlow 2.13.1
* Keras

---

## Vulnerabilidad (CVE)

Este exploit aprovecha la vulnerabilidad **CVE-2024-3660**, una falla crítica en TensorFlow/Keras (versiones anteriores a la 2.13.1) que permite **ejecución remota de código** al cargar capas `Lambda` maliciosas desde modelos `.h5`.

* CVE oficial: [CVE-2024-3660 - NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-3660)

---

## Aviso

Este proyecto se publica **solo para fines educativos y en entornos controlados con autorización explícita**.
No me hago responsable por usos indebidos, ilegales o maliciosos del contenido de este repositorio.

---
