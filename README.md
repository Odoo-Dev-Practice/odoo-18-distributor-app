# Asian Distributor

[![Odoo 18](https://img.shields.io/badge/Odoo-18-purple.svg)](https://www.odoo.com/)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0-standalone.html)

## 📖 Resumen Ejecutivo
Módulo base estructurado para extender la funcionalidad nativa de **Odoo 18**, diseñado específicamente para optimizar las operaciones de empresas importadoras y distribuidoras de productos asiáticos. Este módulo centraliza la trazabilidad de importación y el control de inventario mayorista bajo estándares técnicos de alta disponibilidad y seguridad de datos.

## 🌟 Funcionalidades Principales

- **Gestión de Importación Directa**: Seguimiento detallado del país de origen y trazabilidad logística internacional integrada en la ficha de producto.
- **Optimización de Inventario**: Estructura de recepción de mercancías preparada para flujos de alta rotación en entornos de distribución masiva.
- **Control de Ventas B2B / Mayorista**: Procesos de negocio adaptados para la venta por volumen y gestión ágil de clientes.
- **Integridad de Datos**: Restricciones de borrado en datos maestros (Product Templates) para salvaguardar la consistencia contable del ERP.

## 🛠️ Stack Tecnológico
- **Core Framework**: Odoo 18.0 (Versión Community & Enterprise compatible).
- **Backend**: Python 3.12+ utilizando el ORM avanzado de Odoo, herencias de clase (`_inherit`) y decoradores de API modernos.
- **Arquitectura de Seguridad**: Implementación de RBAC (Role-Based Access Control) mediante archivos CSV y Record Rules XML para segregación multi-compañía avanzada.
- **Interfaz de Usuario**: Inyección de campos y componentes mediante Arquitectura XML (QWeb / Xpath) sobre formularios nativos.

## 📂 Estructura del Módulo
```text
asian_distributor/
├── models/         # Lógica de negocio (Modelos, Campos y Métodos)
├── views/          # Interfaz de Usuario (Herencias de Formularios y Listas)
├── security/       # Capa de Seguridad (Access Rights, Record Rules, Groups)
├── docs/           # Documentación técnica adicional
└── __manifest__.py # Declaración de metadatos y dependencias
```

## 🚀 Instalación y Despliegue
1. Localice su directorio de **addons** en el servidor de Odoo 18 y clone el repositorio.
2. Asegúrese de que las dependencias `base` y `stock` estén instaladas en su instancia.
3. Actualice la lista de aplicaciones desde el menú de la aplicación (Modo Desarrollador activado).
4. Busque **"Asian Distributor"** e inicie el proceso de instalación.
5. Los campos de importación aparecerán automáticamente en la pestaña de Inventario de las Plantillas de Producto.
