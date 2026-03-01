| DNI:  | 00000000 |
| :---- | :------- |
| NAME: | Fairw    |

**ASIAN DISTRIBUTOR APP**

| FILE NUMBER | :    | AD-UML-01                        |
| :---------- | :--- | :------------------------------- |
| FILE TITLE  | :    | UML - Asian Distributor App      |
| START DATE  | :    | 26/02/2026                       |
| PROJECT     | :    | Distribuidora Asiática (Odoo 18) |
| PROGRAMMER  | :    | Fairw                            |

---

# 1. Diagramas Estructurales del Negocio

## 1.1. Modelo Entidad-Relación
Este diagrama ilustra gráficamente cómo se interconecta la información principal del negocio. Muestra que cada producto importado debe estar obligatoriamente enlazado a un país existente en la lista global, garantizando que no existan errores tipográficos al registrar el origen.

```mermaid
erDiagram
    CATALOGO_PRODUCTOS {
        UUID Identificador_Unico
        String Nombre_del_Articulo
        String Codigo_Comercial
        Decimal Precio_de_Venta_Fijo
    }
    
    BASE_DE_PAISES {
        UUID Identificador
        String Nombre_Oficial_del_Pais
        String Codigo_de_Area
    }

    ORDEN_DE_COMPRA {
        UUID Identificador
        String Proveedor_Vendor
        Date Fecha_Pedido
        String Estado_Tránsito
    }

    INVENTARIO_ALMACEN {
        UUID Identificador
        Int Cantidad_Disponible
        String Locacion_Bodega
    }

    ORDEN_DE_VENTA {
        UUID Identificador
        String Cliente_Local
        Decimal Total_Facturado
        String Estado_Entrega
    }

    CATALOGO_PRODUCTOS }o--|| BASE_DE_PAISES : "Es Importado desde"
    ORDEN_DE_COMPRA ||--|{ CATALOGO_PRODUCTOS : "Solicita a Fábrica"
    CATALOGO_PRODUCTOS ||--o{ INVENTARIO_ALMACEN : "Se almacena como"
    INVENTARIO_ALMACEN ||--o{ ORDEN_DE_VENTA : "Se descuenta al vender"
```

## 1.2. Estructura de la Interfaz Visual
Este diagrama muestra cómo se organiza visualmente la pantalla principal de un producto para los usuarios. Asegura que el dato más importante para aduanas (País de Origen) esté visible en la primera plana, sin que el usuario deba buscar en otras pestañas.

```mermaid
flowchart TB
    subgraph Pantalla["Pantalla: Ficha del Producto"]
        direction TB
        Header["Encabezado: Nombre del Producto | Valor: Precio de Venta"]
        
        subgraph Tabs["Pestañas de Navegación"]
            direction LR
            Tab1["[ Información General ]"]
            Tab2["[ Ventas ]"]
            Tab3["[ Compras ]"]
            Tab4["[ Inventario ]"]
        end
        
        subgraph ContenidoInfo["Pestaña: Información General"]
            direction TB
            Form1["Tipo de Producto (Almacenable)"]
            Form3["Código de Barras"]
            NewField(("➕ País de Origen (Importación)"))
            Form3 -.->|"Inyectado debajo"| NewField
        end

        subgraph ContenidoVentas["Pestaña: Ventas"]
            direction TB
            Ventas1["Política de Facturación"]
            Ventas2["Descripción para Cotizaciones"]
            Ventas3["Productos Opcionales"]
        end

        subgraph ContenidoCompras["Pestaña: Compras"]
            direction TB
            Comp1["Lista de Proveedores Asiáticos (Vendors)"]
            Comp2["Impuestos de Compra"]
            Comp3["Política de Control de Recepción"]
        end

        subgraph ContenidoInventario["Pestaña: Inventario"]
            direction TB
            Inv1["Rutas: [X] Comprar  [ ] Fabricar"]
            Inv2["Trazabilidad: Seguimiento por Lotes/Series"]
            Inv3["Logística: Peso y Volumen de Contenedor"]
            Inv4["Plazo de Entrega del Proveedor (Días)"]
        end

        Header --> Tabs
        Tabs --> ContenidoInfo
        Tabs -.-> ContenidoVentas
        Tabs -.-> ContenidoCompras
        Tabs -.-> ContenidoInventario
    end
    
    style NewField fill:#2E8B57,stroke:#006400,color:#fff,stroke-width:2px
    style ContenidoInfo stroke:#333,stroke-width:2px
    style ContenidoVentas stroke:#ccc,stroke-dasharray: 5 5
    style ContenidoCompras stroke:#ccc,stroke-dasharray: 5 5
    style ContenidoInventario stroke:#ccc,stroke-dasharray: 5 5
```

---

# 2. Diagramas de Comportamiento (Flujos)

## 2.1. Casos de Uso del Sistema
Este diagrama define de manera sencilla qué acciones puede realizar cada actor humano dentro del sistema ERP. Refleja claramente el bloqueo comercial para los vendedores.

```mermaid
graph LR
    Admin(("Personal de Compras(Gerencia)"))
    Vendedor(("Personal de Ventas(Tienda)"))

    subgraph Sistema_Central_Distribuidora[Sistema Central Distribuidora]
        UC1([Dar de alta nuevos productos])
        UC2([Asignar el País de Origen asiático])
        UC3([Definir precio de venta fijo])
        UC4([Emitir Orden de Compra Internacional])
        UC5([Consultar catálogo y origen])
        UC6([Generar Cotización y Cobro])
    end

    Admin --> UC1
    Admin --> UC2
    Admin --> UC3
    Admin --> UC4

    Vendedor --> UC5
    Vendedor --> UC6
    
    %% Relación de dependencia
    UC6 -.->|Requiere que el precio esté definido por| UC3
```

## 2.2. Flujo Operativo Core (Diagrama de Secuencia)
Este diagrama de secuencia traza el recorrido lógico y de tiempo desde que se piensa en importar un producto hasta que se le factura al cliente final, respetando las reglas de validación de almacén y precios fijos.

```mermaid
sequenceDiagram
    autonumber
    actor Compras as Personal de compras
    participant Sistema as Sistema Central (ERP)
    actor Almacen as Personal de Almacén
    actor Ventas as Personal de Ventas

    Compras->>Sistema: Crea Ficha del Artículo
    Compras->>Sistema: Selecciona "País de Origen" en el desplegable
    Sistema-->>Compras: Artículo registrado exitosamente
    
    Compras->>Sistema: Genera Orden de Compra (Fábrica Asiática)
    
    note over Sistema, Almacen: Pasan semanas (Tránsito Internacional)
    
    Almacen->>Sistema: Recibe contenedor físico y marca "Ingreso a Bodega"
    Sistema-->>Ventas: Artículos marcados como "Disponibles para vender"
    
    Ventas->>Sistema: Selecciona cliente y añade producto al carrito
    Sistema-->>Ventas: Bloquea precio usando el del catálogo
    Ventas->>Sistema: Confirma Venta Local
```
