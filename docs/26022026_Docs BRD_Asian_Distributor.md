| DNI:  | 00000000 |
| :---- | :------- |
| NAME: | Fairw    |

**ASIAN DISTRIBUTOR APP**

| FILE NUMBER | :    | AD-BRD-01                                                |
| :---------- | :--- | :------------------------------------------------------- |
| FILE TITLE  | :    | BRD - Control de Distribuidora Asiática                  |
| START DATE  | :    | 26/02/2026                                               |
| PROJECT     | :    | Proyecto de Práctica - Comercializadora de Importaciones |
| PROGRAMMER  | :    | Fairw                                                    |

---

# 1. Contexto y problema

## 1.1. Situación actual
La empresa se dedica a importar mercancía variada directamente desde proveedores ubicados en Asia (China, Japón, Taiwán, etc.) para luego venderla a clientes locales. Actualmente, todo el manejo de qué se compra, qué llega al almacén y qué se vende, se quiere organizar en un sistema informático para llevar un control exacto del negocio.

## 1.2. Problemática
Cuando la mercancía llega al país en los contenedores, los trabajadores a veces no recuerdan o no tienen dónde anotar de qué país exactamente vino cada producto. Esto es un problema porque cuando los clientes preguntan el origen del producto, o cuando se necesitan hacer reportes de aduanas, el dato no existe o está escrito con errores (por ejemplo, algunos escriben "china", otros "China" y otros "CHN"). Además, el personal que atiende al público a veces no conoce el proceso completo de cómo llegó el artículo que están vendiendo.

## 1.3. Objetivos del negocio
El objetivo principal de este proyecto de práctica es organizar digitalmente cómo funciona la empresa. Queremos que el sistema informático controle todo el viaje del producto de principio a fin de manera estructurada. En particular, buscamos:
1. Asegurar que nadie escriba países a mano, sino que los elijan de una lista oficial.
2. Hacer que el origen del producto sea visible para todo el equipo.
3. Garantizar que se respete el proceso de compra al extranjero, llegada al almacén local y venta al cliente.

---

# 2. Definición de negocio

## 2.1. Actores del negocio

### 2.1.1. Dueño del negocio / Gerente
Es la máxima autoridad. Se encarga de evaluar si el negocio está dando ganancias y aprueba el presupuesto para comprar la mercancía internacional a los proveedores en Asia.

### 2.1.2. Analista de Compras
Es la persona que habla con las fábricas en Asia. Su trabajo consiste en registrar los productos nuevos en el sistema administrativo, creando su ficha técnica y asegurándose de señalar en el sistema de qué país exacto se está importando dicho producto.

### 2.1.3. Vendedor Local
Es la persona encargada de atender a los clientes finales dentro del país. El vendedor solo puede ver la información de los productos en el sistema para ofrecérselos al cliente, pero no puede modificar las características del producto ni sus orígenes.

## 2.2. Entidad principal

### 2.2.1. Ficha del Producto Importado
El inventario es lo más importante de este negocio. Cada artículo que vende la empresa tiene una ficha o "documento de identidad" en el sistema. En esta ficha siempre debe estar declarado cómo se llama, cuánto vale y de qué país asiático provino.

---

# 3. Procesos de negocio

## 3.1. Flujo completo del negocio (Importación y Venta)

### 3.1.1. Planificación de la importación
El Analista de Compras hace un listado de lo que se necesita traer de Asia. Entra al sistema y crea la ficha de cada producto vacío, anotando detalladamente su peso, medidas y el país de fabricación.

### 3.1.2. Compra internacional
Una vez que el dueño aprueba el presupuesto, el Analista de Compras genera un documento formal de compra y se lo envía al proveedor en el extranjero para ordenar la mercancía.

### 3.1.3. Ingreso al almacén
Semanas después, los contenedores llegan al almacén local de la empresa. El personal de bodega revisa las cajas y le dice al sistema que la mercancía física ya entró, por lo que a partir de este momento los productos ya están listos y disponibles para venderse.

### 3.1.4. Venta Local y Despacho
Un vendedor consigue a un cliente interesado. El vendedor crea el documento de venta en el sistema para cobrarle. Es importante destacar que **el vendedor no negocia el precio**; simplemente le cobra al cliente la tarifa que ya venía fijada previamente para ese producto en el catálogo. Una vez confirmada la venta, se le entrega/despacha el producto al comprador final.

---

# 4. Reglas de negocio

## 4.1. Formalidad en los países de origen
Bajo ninguna circunstancia los trabajadores pueden escribir el nombre de un país con el teclado. Para asegurar el orden y evitar errores ortográficos, el sistema debe obligarlos a elegir el país de fabricación desde una lista oficial y desplegable.

## 4.2. Flujo Completo Obligatorio
El sistema debe estar protegido para evitar trampas o saltos de procesos. Es decir, un vendedor no puede facturarle un producto a un cliente si ese producto no ha sido registrado previamente por el área de almacén como "mercancía recibida" en el sistema. Todo tiene que tener un orden.

## 4.3. Roles y Seguridad
A los vendedores se les da la información suficiente para mostrarle los catálogos a los clientes, pero ellos no tienen autorización, ni herramientas en el sistema para cambiar el nombre, los costos o el origen de lo que se importa. Esa es una tarea autorizada únicamente para Compras y Gerencia.
