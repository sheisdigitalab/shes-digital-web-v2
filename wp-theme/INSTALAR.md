# She's Digital — Instalación del tema WordPress

## Archivos del tema

```
wp-theme/
  shes-digital/          ← carpeta del tema (subir como ZIP)
    style.css            ← declaración del tema
    functions.php        ← carga de scripts, meta SEO, limpieza de <head>
    index.php            ← plantilla de respaldo
    shesdigital-fullblank.php  ← plantilla de las 49 páginas estáticas
    page-bloques.php     ← plantilla nueva: Portada con bloques
    blocks.css           ← reset mínimo de estilos Gutenberg
  portada-bloques.html   ← contenido de la portada (pegar en el editor)
  INSTALAR.md            ← este archivo
```

---

## Paso 1 — Crear el ZIP del tema

```bash
cd wp-theme
zip -r shes-digital.zip shes-digital/
```

---

## Paso 2 — Instalar en WordPress

1. Ir a **Apariencia → Temas → Subir tema**
2. Subir `shes-digital.zip`
3. Activar el tema **She's Digital**
4. Ir a **Ajustes → Permalinks → Guardar cambios** (obligatorio)

> **Nota:** Este tema no necesita Divi ni ningún page builder.
> Si Divi sigue instalado, se puede desactivar sin perder contenido.

---

## Paso 3 — Verificar las plantillas

Ir a **Páginas → Todas las páginas** y confirmar que:

- Las 49 páginas existentes usan la plantilla **shesdigital-fullblank** (ya configurada desde la migración, no hay que tocarlas).
- La página de portada (ID 400) no tiene ninguna plantilla especial todavía → se cambiará en el Paso 5.

---

## Paso 4 — Crear la página de portada con bloques

1. Ir a **Páginas → Editar** la página de portada (ID 400) o crear una nueva.
2. En el panel lateral derecho, cambiar la **Plantilla** a **Página con bloques**.
3. Borrar todo el contenido actual del editor.
4. Abrir `portada-bloques.html` con un editor de texto.
5. Copiar **todo el contenido** del archivo.
6. En el editor de WordPress, hacer clic en los tres puntos (⋮) del menú superior → **Editor de código** (o pulsar `Ctrl + Shift + Alt + M`).
7. Pegar el contenido copiado.
8. Volver al editor visual y verificar que aparecen los bloques.
9. Guardar como borrador y previsualizarla antes de publicar.

---

## Paso 5 — Ajustar la portada estática

En **Ajustes → Lectura**:
- **Tu página principal muestra:** Una página estática
- **Página de inicio:** seleccionar la página editada en el Paso 4

---

## Editar la portada en el futuro

Cada sección es un bloque **HTML personalizado** (`wp:html`). Para editar:

1. Hacer clic en el bloque de la sección que quieras cambiar.
2. Pulsar el botón **Editar HTML** que aparece en la barra de herramientas del bloque.
3. Editar el texto directamente en el HTML.
4. Guardar.

**Qué editar normalmente:**

| Sección | Qué cambiar |
|---------|-------------|
| Hero | Texto del H1 (rotor words), párrafo lead, founder text |
| Servicios | Precios (`<b>450 €</b>`), descripciones de servicio |
| Proyectos | Título, texto y features de cada panel de sector |
| Reseñas | Texto de las `<blockquote>`, nombre del autor |
| Sobre mí | Los tres párrafos de `.about__copy` |
| Proceso | H3 y párrafo de cada `<li class="step">` |
| FAQ | `<summary>` (pregunta) y `<p>` dentro de `.qa__body` |
| Contacto | Teléfono/email en `.contact__direct` |

---

## Meta SEO por página

Cada página tiene dos campos personalizados para SEO:

- `_shes_meta_title` → title del documento (si está vacío, usa el título de la página en WP)
- `_shes_meta_desc` → meta description

Se pueden editar desde **Páginas → Editar → Panel lateral → Campos personalizados** (o con un plugin como Advanced Custom Fields).

---

## Riesgos de quitar Divi

| Riesgo | Impacto | Solución |
|--------|---------|----------|
| Las 49 páginas usan `shesdigital-fullblank` que llama a `the_content()` directamente, sin pasar por Divi Builder | **Ninguno** — el contenido HTML estático se muestra tal cual | No hay que hacer nada |
| Divi guarda diseños en `_et_pb_*` meta. Al desactivar Divi, esos datos quedan en la BD pero no se renderizan | **Ninguno** en las páginas estáticas | Se puede limpiar después |
| Si alguna página usaba Divi Builder de verdad (no estática), perdería su layout visual | Revisar si hay páginas con `_et_pb_use_builder = on` | Migrarlas antes de desactivar |

Consulta rápida para detectar páginas con Divi Builder activo:

```sql
SELECT post_id FROM wp_postmeta 
WHERE meta_key = '_et_pb_use_builder' AND meta_value = 'on';
```

Si el resultado está vacío, es seguro desactivar Divi.
