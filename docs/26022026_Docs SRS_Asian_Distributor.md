| DNI:  | 00000000 |
| :---- | :------- |
| NAME: | Fairw    |

**ASIAN DISTRIBUTOR APP**

| FILE NUMBER | :    | AD-SRS-01                        |
| :---------- | :--- | :------------------------------- |
| FILE TITLE  | :    | SRS - Asian Distributor App      |
| START DATE  | :    | 26/02/2026                       |
| PROJECT     | :    | Distribuidora Asiática (Odoo 18) |
| PROGRAMMER  | :    | Fairw                            |


# 1. Introducción

## 1.1. Propósito
El propósito de este documento es definir los requerimientos funcionales y no funcionales (Software Requirements Specification) para la implementación de la aplicación de Distribuidora Asiática. El sistema digitalizará la gestión técnica del catálogo, controlando la importación de mercancías asiáticas, el inventario y bloqueando las reglas de ventas de acuerdo al modelo de negocio de práctica.

## 1.2. Alcance del producto
El sistema extenderá las funcionalidades nativas de Odoo 18 (Inventario, Compras y Ventas) adaptándolas para controlar importaciones.
- **Gestión Técnica del Catálogo:** Creación y almacenamiento del origen de vida del producto.
- **Estandarización de Identificación:** Incorporación de un campo obligatorio llamado "País de Origen".
- **Gestión de Importaciones:** Generación de órdenes a fábricas para asegurar la llegada a almacén.
- **Transaccionalidad Restringida:** Integración de la venta obligando al usuario a usar únicamente los valores del sistema.

## 1.3. Stack tecnológico
Para cumplir con los objetivos del proyecto de práctica, se define la siguiente arquitectura técnica:

### 1.3.1. Backend e Infraestructura
- **Sistema Base:** Odoo 18 Community.
- **Base de datos:** PostgreSQL.
- **Despliegue:** Entorno de contenedores locales (Docker Compose).

### 1.3.2. Frontend
- **Framework Odoo Web:** Interfaz web nativa y responsiva.
- **Extensión de vistas:** Modificación visual de ventanas usando inyección de componentes para no alterar el código base de la plataforma.


# 2. Descripción general

## 2.1. Roles de usuarios y permisos
El acceso será jerárquico a través de los grupos predefinidos de Odoo y modificaciones a nivel de vistas/seguridad.

### 2.1.1. Matriz de permisos

|   Módulo   |              Funciones               | Administrador (Analista Compras) | Personal (Vendedores) |
| :--------: | :----------------------------------: | :------------------------------: | :-------------------: |
| Inventario |         Crear Productos base         |               CRUD               |           R           |
|            |       Asignar "País de Origen"       |               CRUD               |           R           |
|            | Modificar Precio de Venta (Catálogo) |               CRUD               |           R           |
|            |    Acceder a Inventario/Recepción    |               CRUD               |           R           |
|  Compras   |       Generar Orden de Compra        |               CRUD               |           -           |
|   Ventas   |       Generar Venta al Cliente       |               CRUD               |         CRUD          |

### 2.1.2. Definición de roles

- **Administrador / Analista de Compras:** Perfil con el control total de lectura, escritura, creación y eliminación en la gestión de productos y órdenes de importación. Único usuario con autoridad para agregar características al objeto importado y definir su precio de mercado.
- **Personal / Vendedor:** Perfil operativo comercial. Dispone de privilegios para listar bienes disponibles, pero su acceso al catálogo de productos y precios es estrictamente de lectura. Su única capacidad de creación es generar órdenes de venta hacia los clientes finales.


# 3. Requerimientos funcionales

## 3.1. Módulo de Catálogo / Inventario

### RF-INV-001 Registrar nuevo producto con Origen
- **Descripción:** El sistema debe permitir registrar datos básicos de un producto (nombre, código interno, código de barras y precio) y obligatoriamente registrar su País de Origen.
- **Reglas de Negocio:** El campo de País de Origen no aceptará texto ingresado libremente por el teclado; el usuario deberá seleccionar el país desde un menú desplegable conectado a la lista oficial de países globales del sistema.

### RF-INV-002 Visualización del origen en la ficha
- **Descripción:** El sistema debe mostrar el País de Origen de forma prominente dentro de la ventana de detalles del producto, sin necesidad de navegar por sub-menús.
- **Reglas de Negocio:** Se requiere que visualmente el campo quede ubicado inmediatamente debajo del campo "Código de Barras" en la pestaña de Información General.

### RF-INV-003 Recepción Controlada en Almacén
- **Descripción:** El sistema controlará que la mercancía importada no aparezca como "Disponible para vender" de forma automática tras emitir la compra.
- **Reglas de Negocio:** El inventario físico solo se sumará al sistema cuando el personal indique explícitamente haber recibido la transferencia de mercancía en el almacén.

## 3.2. Módulo de Compras

### RF-COM-001 Emisión de Orden de Compra Internacional
- **Descripción:** El sistema permitirá a los administradores generar solicitudes formales de mercancía hacia fábricas asiáticas, centralizando los costos y las cantidades solicitadas en un documento digital de compra.

## 3.3. Módulo de Ventas

### RF-VEN-001 Generación de Cotización y Venta
- **Descripción:** El sistema permitirá a los vendedores generar cotizaciones y confirmarlas para convertirlas en pedidos de venta oficiales.
- **Reglas de Negocio:** Al crear una venta, el sistema descontará la mercancía o la reservará basándose en el stock físico disponible en el almacén.

## 3.4. Módulo de Seguridad

### RF-SEC-001 Ocultamiento de la edición para vendedores
- **Descripción:** El catálogo de productos debe ser inmutable frente a la fuerza de venta.
- **Reglas de Negocio:** Si el usuario que ha iniciado sesión pertenece al grupo de vendedores, el sistema debe ocultar y bloquear cualquier botón o formulario que permita editar los detalles del producto (incluyendo su origen).

### RF-SEC-002 Restricción de Alteración de Precio Base
- **Descripción:** Bloqueo de libre negociación mediante la inmutabilidad de los precios.
- **Reglas de Negocio:** Al momento de agregar un producto a la orden de venta (carrito), el sistema cargará automáticamente el precio de catálogo y bloqueará la celda del monto, impidiendo al vendedor subir o bajar el costo del producto.


# 4. Requerimientos no funcionales

## 4.1. Disponibilidad
El sistema debe operar ininterrumpidamente de manera local para que todo el personal pueda interactuar bajo el mismo entorno y base de datos sin retardos perceptibles en la red de la oficina.

## 4.2. Usabilidad
La plataforma se construirá manteniendo una separación limpia de componentes. Las adiciones visuales de la distribuidora asiática (como campos o botones) se integrarán de manera transparente al sistema base sin modificar su código original, asegurando que su uso sea intuitivo y coherente con el resto del programa.

## 4.3. Escalabilidad
La infraestructura central debe residir en un gestor relacional independiente, asegurando que el registro de inventario pueda crecer a decenas de miles de productos importados sin experimentar ralentizaciones en las búsquedas ni en la visualización de datos.

## 4.4. Mantenibilidad
Las futuras actualizaciones o revisiones del sistema deben seguir una estructura estándar de programación universal, empleando un formato ordenado y modular para facilitar la lectura del entorno por futuros desarrolladores.

## 4.5. Auditoría y Trazabilidad
El sistema debe llevar un registro en segundo plano de cualquier cambio significativo en la información crítica. Si un administrador modifica el "País de Origen" de un producto que ya había sido guardado, el sistema dejará un historial visible en el registro de actividad indicando quién realizó el cambio, cuándo ocurrió y qué valor específico fue alterado.
