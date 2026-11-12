# She's Digital — Divi Child Theme
## Guía de instalación y uso

---

## 1. INSTALACIÓN

1. Instala y activa el tema **Divi** (de Elegant Themes) en tu WordPress
2. Ve a **Apariencia → Temas → Subir tema**
3. Sube el ZIP `shes-digital-divi.zip`
4. Activa el child theme **She's Digital — Divi Child**
5. Ve a **Ajustes → Enlaces permanentes → Guardar cambios**

---

## 2. COLORES DE MARCA (ya cargados automáticamente)

Al abrir el Divi Builder verás estos colores en la paleta:

| Color        | Hex       | Uso principal              |
|--------------|-----------|----------------------------|
| Dark         | #1E2420   | Fondos oscuros, texto       |
| Mint Deep    | #7CBCAD   | Acentos, links, etiquetas  |
| Mint         | #C8E8E0   | Fondos suaves              |
| Rose         | #F0D4D4   | Cards servicios 1          |
| Butter       | #F8EEBB   | Cards servicios 4          |
| Beige Warm   | #EDE0CC   | Fondos alternativos        |
| Text Mid     | #4A5045   | Texto secundario           |
| Background   | #FAFAF6   | Fondo general              |

---

## 3. TIPOGRAFÍAS

En el selector de fuentes del Builder busca:
- **Funnel Display** — para titulares (H1, H2, H3)
- **DM Sans** — para texto del cuerpo y párrafos

---

## 4. CLASES CSS PARA CADA SECCIÓN

Añade estas clases en **Divi Builder → Sección/Fila/Módulo → Avanzado → Clase CSS**:

### Secciones (aplicar a la Sección de Divi)
| Clase          | Efecto                                          |
|----------------|-------------------------------------------------|
| `sd-hero`      | Fondo crema + blobs decorativos                 |
| `sd-services`  | Fondo crema + colores automáticos en las cards  |
| `sd-projects`  | Fondo oscuro (#1E2420) + textos en blanco       |
| `sd-testimonials` | Fondo blanco + cards con hover               |
| `sd-about`     | Fondo crema + estilos de imagen y texto         |
| `sd-cta`       | Gradiente pastel (beige → rosa → mint)          |
| `sd-contact`   | Estilos para formulario y datos de contacto     |

### Módulos (aplicar al módulo concreto)
| Clase           | Efecto                              |
|-----------------|-------------------------------------|
| `sd-btn-primary`   | Botón oscuro (fondo #1E2420)     |
| `sd-btn-secondary` | Botón outline                    |
| `sd-btn-white`     | Botón blanco (para fondos oscuros)|
| `sd-label`         | Etiqueta pequeña en mayúsculas   |
| `sd-badge`         | Badge con número grande          |
| `sd-value-tag`     | Pill/etiqueta redondeada         |
| `sd-pill`          | Etiqueta verde pastel            |
| `sd-dark-bg`       | Fondo oscuro + textos blancos    |
| `sd-reveal`        | Animación de entrada al hacer scroll |

---

## 5. CÓMO MONTAR CADA SECCIÓN EN DIVI

### HERO
- Sección: clase `sd-hero`
- Layout: 2 columnas (60% / 40%)
- Col izquierda: Módulo Texto → H1 con `<em>` en la palabra cursiva
- Col derecha: Módulo Imagen o código HTML con el mockup del navegador

### SERVICIOS
- Sección: clase `sd-services`
- Layout: 3 columnas × 2 filas
- Módulo: **Blurb** (icono + título + texto)
- Los colores de fondo de cada card se aplican automáticamente por posición

### PROYECTOS
- Sección: clase `sd-projects`
- Layout: 3 columnas
- Módulo: **Portfolio** de Divi o módulo Imagen con overlay de texto

### TESTIMONIOS
- Sección: clase `sd-testimonials`
- Módulo: **Testimonial** de Divi
- Añade ★★★★★ como texto encima de cada testimonio

### SOBRE NOSOTRAS
- Sección: clase `sd-about`
- Layout: 2 columnas (imagen / texto)
- Col izquierda: Módulo Imagen
- Col derecha: Módulo Texto con H2, párrafos y etiquetas con clase `sd-value-tag`

### CTA FINAL
- Sección: clase `sd-cta`
- Layout: 1 columna centrada
- Módulo Texto + 2 botones con clases `sd-btn-white` y `sd-btn-secondary`

### CONTACTO
- Sección: clase `sd-contact`
- Layout: 2 columnas
- Col izquierda: Módulo Texto con datos de contacto
- Col derecha: Módulo **Contact Form** de Divi

---

## 6. TIPOGRAFÍA EN EL BUILDER

Para los titulares:
- Font: **Funnel Display**
- Weight: 700 o 800
- Letter spacing: -3 a -5

Para el cuerpo:
- Font: **DM Sans**
- Weight: 300 o 400
- Line height: 1.7 - 1.8

---

¿Dudas? Cualquier ajuste de estilo se hace en **style.css** de este child theme.
