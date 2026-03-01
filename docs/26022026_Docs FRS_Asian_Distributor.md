| DNI:  | 00000000 |
| :---- | :------- |
| NAME: | Fairw    |

**ASIAN DISTRIBUTOR APP**

| FILE NUMBER | :    | AD-FRS-01                        |
| :---------- | :--- | :------------------------------- |
| FILE TITLE  | :    | FRS - Asian Distributor App      |
| START DATE  | :    | 26/02/2026                       |
| PROJECT     | :    | Distribuidora Asiática (Odoo 18) |
| PROGRAMMER  | :    | Fairw                            |


# 1. Introducción

## 1.1. Propósito
El propósito de este documento es definir el comportamiento funcional esperado del sistema Odoo 18 para la operación de importación y venta de la Distribuidora Asiática. Este FRS (Functional Requirements Specification) documenta exactamente cómo reaccionarán las pantallas, qué datos debe ingresar el usuario y qué validaciones ejecutará el sistema antes de guardar la información, sirviendo como guía estricta para el equipo de pruebas (QA) y diseño de la interfaz.

## 1.2. Alcance Funcional
El alcance abarca la modificación del comportamiento estándar de los módulos de Inventario, Compras y Ventas. Se especificará el comportamiento de los nuevos campos de control de importación (País de Origen), las restricciones visuales aplicadas a la fuerza de ventas y los flujos de clics necesarios para completar el ciclo de vida de un producto asiático.

---

# 2. Especificación de Pantallas e Interfaces (UI)

## 2.1. Formulario de Producto (Vista Principal)
La ficha del producto es la pantalla central del sistema. Su comportamiento visual será el siguiente:
*   **Encabezado:** Mostrará el nombre del producto en fuente grande y un botón inteligente (Smart Button) indicando las unidades "A Mano" (Stock físico).
*   **Pestaña [Información General]:**
    *   Contendrá los campos estándar: Tipo de Producto, Categoría, Precio de Venta, Coste, Referencia Interna y Código de Barras.
    *   **Nuevo Comportamiento:** Exactamente debajo del "Código de Barras", existirá un campo obligatorio llamado "País de Origen". Este campo será un control de autocompletado con menú desplegable.
*   **Botones de Acción (Guardar/Editar):** Estarán visibles en la esquina superior izquierda únicamente si el usuario tiene el rol de Administrador o Analista de Compras.

## 2.2. Vistas de Lista (Catálogos)
Al ingresar al menú de Productos y visualizar el catálogo en formato de lista (tabla):
*   **Columnas Estándar:** Nombre Interno, Precio de Venta, Coste, Cantidad a Mano.
*   **Columna Adicional:** Se mostrará de forma predeterminada la columna "País de Origen" para permitir al personal identificar rápidamente la procedencia de la mercancía sin tener que abrir cada ficha de producto individualmente.

---

# 3. Casos de Uso y Funcionalidad Detallada

## 3.1. Funcionalidad: Creación de Producto Importado
Esta funcionalidad describe cómo el área de compras registra un nuevo bien adquirido en el extranjero.

*   **Actor:** Analista de Compras.
*   **Pre-condición:** El usuario debe haber iniciado sesión con credenciales de Administrador/Compras.
*   **Flujo Principal:**
    1. El usuario navega al menú *Inventario > Productos > Productos*.
    2. Hace clic en el botón *[ Nuevo ]*.
    3. El sistema despliega un formulario en blanco.
    4. El usuario completa el "Nombre del Producto" y establece el "Precio de Venta".
    5. El usuario hace clic en el campo desplegable "País de Origen".
    6. El sistema muestra una lista de todos los países del mundo.
    7. El usuario escribe "Jap" y el sistema filtra mostrando "Japón". Selecciona "Japón".
    8. Hace clic en el icono de la nube o fuera del formulario para autoguardar.
*   **Regla de Validación (Excepción):** Si el usuario intenta guardar el registro dejando el campo "País de Origen" en blanco, el sistema teñirá el borde del campo en rojo y mostrará una alerta emergente evitando el guardado: *"Campos inválidos: País de Origen"*.

## 3.2. Funcionalidad: Recepción de Mercancía de Asia
Controla la entrada de bienes físicos para evitar ventas de artículos que aún están en un barco.

*   **Actor:** Personal de Almacén.
*   **Pre-condición:** Existe una Orden de Compra confirmada ("Pedido de Compra") pero la mercancía no ha llegado físicamente.
*   **Configuración del Sistema:** En este estado, la Ficha del Producto muestra Stock "A Mano" = 0.
*   **Flujo Principal:**
    1. El contenedor llega a la bodega logística.
    2. El almacenero abre la Recepción pendiente asociada a la Orden de Compra.
    3. Verifica que las cantidades físicas coincidan con las cajas del contenedor.
    4. Hace clic en el botón *[ Validar ]*.
    5. **Comportamiento Requerido:** Inmediatamente después del clic, el sistema actualiza el stock "A Mano" del producto en el catálogo base, sumando exactamente la cantidad recibida. Solo desde este instante el producto está disponible para ser facturado por Ventas.

## 3.3. Funcionalidad: Generación de Venta Restringida
Garantiza que el precio y las condiciones de los productos importados no sean alterados por el personal comercial.

*   **Actor:** Vendedor Local.
*   **Pre-condición:** El Vendedor tiene un cliente presencial y el producto existe en el catálogo con stock mayor a cero.
*   **Flujo Principal:**
    1. El Vendedor navega a *Ventas > Pedidos > Presupuestos*.
    2. Crea un nuevo Presupuesto seleccionando al Cliente.
    3. En la sección "Líneas de Pedido", añade el producto importado (Ej. "Radio Automotriz Sony").
    4. **Comportamiento Requerido:** El sistema carga automáticamente en la línea el "Precio Unitario" fijado en el catálogo.
    5. El vendedor intenta hacer clic sobre el número del "Precio Unitario" para bajarle el costo al cliente.
*   **Regla de Validación (Bloqueo):** La celda "Precio Unitario" está sombreada en color grisáceo y no responde al teclado ni al ratón (Estado Read-Only). El vendedor se ve obligado a hacer clic en *[ Confirmar Venta ]* utilizando estrictamente el precio oficial del sistema.

---

# 4. Reglas de Validación de Datos

## 4.1. Gestión de Errores y Alertas
El sistema Odoo responderá con alertas nativas (notificaciones emergentes en la esquina superior derecha o globos rojos en los campos) bajo las siguientes condiciones:
*   **Falta de Origen:** Intentar guardar un producto sin asignar país desplegará la alerta visual subrayando en rojo el campo faltante.
*   **Falta de Stock (Warning de Ventas):** Si el vendedor intenta confirmar un pedido de venta y el producto aún no ha superado la funcionalidad de "Recepción de Mercancía de Asia" (Stock <= 0), el sistema mostrará una advertencia amarilla indicando que no hay existencias suficientes para satisfacer esa demanda.

## 4.2. Campos Obligatorios
Para asegurar la calidad de la base de datos de importaciones, los siguientes campos se marcan como funcionalmente obligatorios en la interfaz:
*   **Nombre del Producto:** Requerido para identificación.
*   **Tipo de Producto:** Debe estar fijado en "Producto Almacenable" para poder llevar un control físico.
*   **Precio de Venta:** Obligatorio para generar la lista de precios a clientes.
*   **País de Origen:** Bloqueo de importaciones "huérfanas" de procedencia.

---

# 5. Reportes y Salidas

*   **Exportación de Catálogo (Excel/CSV):** 
    En la vista de Lista de Productos, los Analistas de Compra deben tener la capacidad funcional de seleccionar todos los registros y usar el menú *Acción > Exportar*. El asistente de exportación deberá mostrar "País de Origen" como un campo disponible para añadir a la planilla de cálculo. Este archivo Excel será fundamental para reportes trimestrales de procedencia aduanera.
