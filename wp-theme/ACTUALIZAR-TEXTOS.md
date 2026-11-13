# Desplegar los cambios del panel «Textos de la web»

## 1. Conectar al servidor

```bash
ssh -p 65002 -i ~/.ssh/sheisdigitalab_deploy u857430185@31.170.164.42
```

## 2. Subir los archivos nuevos / modificados

Desde tu máquina local (Bash o PowerShell, en la raíz del repo):

```bash
# Tema completo (incluye el panel y los cambios en shesdigital-fullblank.php)
rsync -avz -e "ssh -p 65002 -i ~/.ssh/sheisdigitalab_deploy" \
  wp-theme/shes-digital/ \
  u857430185@31.170.164.42:/home/u857430185/domains/sheisdigitalab.com/public_html/wp-content/themes/shes-digital/

# Plantilla de portada con marcadores (para importarla como página)
rsync -avz -e "ssh -p 65002 -i ~/.ssh/sheisdigitalab_deploy" \
  wp-theme/portada-marcadores.html \
  u857430185@31.170.164.42:/home/u857430185/domains/sheisdigitalab.com/public_html/wp-content/themes/shes-digital/
```

## 3. Registrar la opción por defecto (una sola vez)

Desde SSH, en el directorio de WordPress:

```bash
cd /home/u857430185/domains/sheisdigitalab.com/public_html/

# Inicializar la opción con los valores por defecto del panel
wp option add sd_textos '{}' --format=json 2>/dev/null || true
```

> Si la opción ya existe (el panel se guardó antes) este comando no hace nada.

## 4. Verificar que el panel funciona

1. Accede al escritorio de WordPress → **Textos de la web** (menú lateral).
2. Modifica cualquier campo y pulsa **Guardar cambios**.
3. Visita `https://sheisdigitalab.com/` y comprueba que el texto cambia.

## 5. Importar la portada como contenido de la página ID 400

Solo si aún no está importada, o si has regenerado el marcador:

```bash
cd /home/u857430185/domains/sheisdigitalab.com/public_html/

# Volcamos el contenido del HTML en el post_content de la página ID 400
wp post update 400 \
  --post_content="$(cat wp-content/themes/shes-digital/portada-marcadores.html)" \
  --post_status=publish
```

> El filtro `the_content` (priority 10, en `textos-panel.php`) reemplazará
> los marcadores `{{sd:key}}` al servir la página.

## 6. Limpiar caché (si hay plugin de caché activo)

```bash
wp cache flush
wp w3-total-cache flush all   # si usas W3 Total Cache
wp litespeed-purge all        # si usas LiteSpeed Cache
```

## Notas

- **PHP requerido**: 8.0+. Los archivos usan `match`, `str_contains` y nullsafe operators.
- **WP-CLI** debe estar disponible en el servidor (`wp --info` para comprobarlo).
- **SSH key**: `C:\Users\Jenifer\.ssh\sheisdigitalab_deploy` (Windows) → `~/.ssh/sheisdigitalab_deploy` (Mac/Linux).
- El typo `sheisdigitallab` (doble l) ha sido corregido a `sheisdigitalab` en todos los archivos del tema.
