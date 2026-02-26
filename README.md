# Asian Distributor Config

[![Odoo 18](https://img.shields.io/badge/Odoo-18-purple.svg)](https://www.odoo.com/)
[![Python](https://img.shields.io/badge/Python-3-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0-standalone.html)

## 📖 Acerca de Asian Distributor
Este es un módulo estructurado para extender la funcionalidad nativa de Odoo 18. Está adaptado para las necesidades operativas de una empresa importadora y distribuidora de productos asiáticos, abarcando:

- **Compras Internacionales**: Control y trazabilidad del origen de los productos importados.
- **Inventario Mayorista**: Recepción y organización de mercancías desde el extranjero.
- **Ventas B2B/B2C**: Adaptaciones en el proceso de venta para clientes.
- **Flujo Operativo**: Seguimiento ágil de tiempos e información esencial de importación.

## 🛠️ Tecnologías Utilizadas
- **Framework**: Odoo 18
- **Metodología**: SDD (Spec-Driven Development) usando Agent Teams Lite
- **Python**: Herencia de clases (`_inherit`), nuevos campos computados y estructura MVC.
- **XML**: Personalización de Vistas (xpath) para inyectar componentes en Formularios nativos de Odoo.

## 📂 Estructura del Módulo
```text
asian_distributor/
├── models/         # Lógica (Modelos, Campos y Herencias)
├── views/          # Interfaz (Inyección de Formularios y Vistas Kanban/Tree)
├── security/       # Reglas de acceso (Archivos CSV para Permisos)
└── __manifest__.py # Metadatos de configuración del módulo
```

## 🚀 Instalación y Uso
1. Clona este repositorio y coloca la carpeta dentro de tu directorio de **addons** de Odoo 18.
2. Reinicia tu servicio o contenedor de Odoo.
3. En Odoo, entra a Aplicaciones y haz clic en **Actualizar lista de aplicaciones** (requiere Modo Desarrollador encendido).
4. Busca **"Asian Distributor Config"** y haz clic en Instalar.
5. ¡Empieza a registrar tus productos con detalles de importación asiática!
