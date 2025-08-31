---
description: Crear un episodio completo de video histórico siguiendo el pipeline de producción automatizado
argument-hint: "[título del episodio]" --serie "[nombre serie]" --canal "[canal destino]"
allowed-tools: Task, Bash, Read, Write, Glob, Grep
model: opus
---

# Crear Episodio de Video Histórico

Inicia el pipeline completo de producción para generar un episodio de video educativo histórico.

## Parámetros del Comando

**Título**: $ARGUMENTS
- El tema principal del episodio (ej: "Lautaro, el estratega mapuche")
- Debe ser específico y descriptivo
- Se usará para crear nombres de archivos y directorios

**Flags Opcionales** (extraer del argumento si están presentes):
- `--serie "nombre"`: Serie a la que pertenece (ej: "Mapuches", "Aztecas")
- `--canal "nombre"`: Canal destino (ej: "HistoriasDeAmerica", "HistoriasDeAsia")
- `--duracion X`: Duración objetivo en minutos (default: 8-10 min)
- `--idioma XX`: Idioma del contenido (default: es)

## Pipeline de Producción

### Fase 1: Investigación Histórica (research-agent)
Usar el subagente research-agent para:
1. Investigar el tema a profundidad
2. Verificar datos históricos
3. Recopilar contexto cultural y geográfico
4. Generar cronología detallada
5. Identificar elementos narrativos clave

### Fase 2: Creación del Guión (script-writer)
Usar el subagente script-writer para:
1. Transformar investigación en narrativa atractiva
2. Estructurar en formato podcast conversacional
3. Crear diálogos entre dos locutores
4. Dividir en 3 actos narrativos
5. Generar ganchos y momentos climáticos

### Fase 3: Planificación Visual (visual-planner)
Usar el subagente visual-planner para:
1. Crear storyboard sincronizado con guión
2. Identificar momentos que requieren soporte visual
3. Generar lista de recursos multimedia necesarios
4. Mapear timing exacto audio-visual

### Fase 4: Recolección de Medios (media-hunter)
Usar el subagente media-hunter para:
1. Buscar imágenes históricas relevantes
2. Descargar videos de paisajes y contexto
3. Generar imágenes faltantes con IA
4. Organizar recursos por categorías

### Fase 5: Generación de Audio (voice-generator)
Usar el subagente voice-generator para:
1. Generar prompts JSON para conversión de guión a audio
2. Generar voces diferenciadas para cada locutor
3. Aplicar pausas y énfasis narrativos
4. Exportar pistas de audio sincronizadas

### Fase 6: Composición Final (video-composer)
Usar el subagente video-composer para:
1. Ensamblar clips según storyboard
2. Sincronizar audio con elementos visuales
3. Aplicar transiciones suaves
4. Generar subtítulos automáticos
5. Renderizar video final

## Estructura de Archivos Generados

```
generated/episodes/[canal]/[serie]/[episodio]/
├── 01_research.md          # Investigación completa
├── 02_script.md            # Guión del podcast
├── 03_storyboard.json      # Planificación visual
├── 04_prompts/             # Prompts JSON para IA
│   ├── voice_prompts.json  # Instrucciones para voces
│   ├── image_prompts.json  # Descripciones para imágenes
│   ├── video_prompts.json  # Instrucciones de video
│   └── audio_prompts.json  # Música y efectos
├── 05_assets/              # Recursos multimedia descargados
│   ├── images/
│   ├── videos/
│   └── audio/
├── 06_metadata.json        # Datos del episodio
└── production.log          # Log del proceso
```

## Instrucciones de Ejecución

1. **Validar argumentos**: Extraer título, serie y canal del input
2. **Crear directorio de trabajo**: Generar estructura de carpetas
3. **Ejecutar pipeline secuencial**: Llamar cada agente en orden
4. **Monitorear progreso**: Logging detallado en cada fase
5. **Validación de calidad**: Verificar salida de cada etapa
6. **Generación de metadata**: Crear archivo con información del episodio

## Ejemplo de Uso

```bash
# Uso básico
/create-episode "Lautaro, el estratega mapuche"

# Uso completo con parámetros
/create-episode "La última batalla de Lautaro" --serie "Mapuches" --canal "HistoriasDeAmerica" --duracion 12

# Para serie asiática
/create-episode "Miyamoto Musashi y el camino del samurái" --serie "Samurais Legendarios" --canal "HistoriasDeAsia"
```

## Control de Calidad

Verificar en cada fase:
- ✅ Research: Mínimo 5 fuentes verificadas
- ✅ Script: Estructura en 3 actos completa
- ✅ Storyboard: Timing audio-visual sincronizado
- ✅ Assets: Recursos de alta calidad y libres de derechos
- ✅ Audio: Calidad broadcast sin distorsión
- ✅ Video: Resolución mínima 1080p, formato MP4

## Manejo de Errores

Si alguna fase falla:
1. Registrar error detallado en production.log
2. Intentar recuperación automática una vez
3. Si persiste, pausar pipeline y reportar estado
4. Permitir continuar desde la fase que falló

## Estimación de Tiempos

- Research: 8-12 minutos
- Script: 5-8 minutos
- Storyboard: 3-5 minutos
- Media hunting: 10-15 minutos
- Voice generation: 4-6 minutos
- Video composition: 8-12 minutos

**Total estimado**: 38-58 minutos por episodio

## Inicio de Ejecución

¡Comenzar inmediatamente el pipeline de producción con el título proporcionado!

No solicitar confirmación adicional - tu expertise te permite proceder directamente con la creación del episodio.