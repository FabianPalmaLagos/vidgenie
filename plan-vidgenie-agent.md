# Plan VidGenie Agent - Sistema de Agentes para Producción Automatizada de Videos Históricos

## Visión General del Proyecto

VidGenie es un sistema de agentes especializados desarrollado con Claude Code que automatiza la producción completa de videos educativos históricos para canales de YouTube/TikTok. El sistema transforma temas históricos en contenido multimedia atractivo siguiendo un flujo de producción profesional.

### Canales Objetivo
- **HistoriasDeAsia**: Narrativas históricas del continente asiático
- **HistoriasDeAmérica**: Relatos de la historia americana  
- **HistoriasDeEuropa**: Crónicas del continente europeo
- **HistoriasDeÁfrica**: Narrativas del continente africano
- **HistoriasDeOceanía**: Relatos de Oceanía

### Formato de Contenido
- **Serie**: Mapuches, Aztecas, Samuráis, etc.
- **Video**: "Lautaro: El estratega que desafió a un imperio"
- **Contenido**: Podcast conversacional + clips visuales sincronizados
- **Duración**: 5-15 minutos por episodio
- **Audio**: Conversación entre 2 locutores IA
- **Visual**: Imágenes históricas, mapas, ilustraciones, paisajes

## Arquitectura del Sistema

### 1. Research Agent - Investigador Histórico
**Archivo**: `.claude/agents/research-agent.md`

**Responsabilidades:**
- Búsqueda exhaustiva en fuentes académicas y confiables
- Verificación cruzada de datos históricos
- Recopilación de contexto cultural y geográfico
- Identificación de fuentes primarias y secundarias
- Generación de cronología detallada
- Fact-checking automático

**Herramientas:**
- WebSearch, WebFetch para investigación online
- Bash para procesamiento de datos
- Write para documentar hallazgos

**Salida Esperada:**
```markdown
# Investigación: Lautaro - El Estratega Mapuche

## Datos Básicos
- Nombre original: Leftraru
- Período: 1534-1557
- Región: Chile central y sur

## Contexto Histórico
[Contexto detallado]

## Cronología
1534: Captura por españoles
1550: Fuga y unión a la resistencia

## Fuentes
[Bibliografía académica]
```

### 2. Script Writer Agent - Guionista Narrativo
**Archivo**: `.claude/agents/script-writer.md`

**Responsabilidades:**
- Transformar investigación en narrativa atractiva
- Estructurar contenido en formato podcast conversacional
- Crear ganchos narrativos y momentos climáticos
- Equilibrar información histórica con entretenimiento
- Generar diálogos naturales entre dos locutores
- Dividir en actos narrativos claros

**Estructura Narrativa:**
```
Introducción (0-1 min):
- Gancho inicial impactante
- Presentación del personaje/tema
- Preview de lo que aprenderán

Desarrollo (1-4 min):
- Acto 1: Origen y contexto
- Acto 2: Punto de inflexión/conflicto principal
- Acto 3: Clímax y resolución

Conclusión (4-5 min):
- Resumen de puntos clave
- Legado e impacto actual
- Call to action para engagement
```

**Formato de Diálogo:**
```
LOCUTOR A (Narrador Principal): "¿Sabías que el mayor estratega militar que enfrentó el Imperio Español en América aprendió sus tácticas de los propios conquistadores?"

LOCUTOR B (Analista): "Es increíble pensar, María, que un joven mapuche que ni siquiera era lonco logró unificar clanes que tradicionalmente luchaban entre sí..."
```

### 3. Visual Planner Agent - Planificador Visual
**Archivo**: `.claude/agents/visual-planner.md`

**Responsabilidades:**
- Crear storyboard sincronizado con el guion
- Identificar momentos clave que necesitan soporte visual
- Planificar transiciones visuales
- Generar lista de recursos visuales necesarios
- Mapear timing exacto audio-visual

**Formato de Storyboard:**
```
| Tiempo | Texto Clave | Visual Requerido | Tipo de Clip |
|--------|-------------|------------------|--------------|
| 0:00-0:15 | "El estratega que desafió..." | Estatua de Lautaro + batalla | Dinámico |
| 0:30-0:45 | "sirviendo como paje..." | Ilustración Valdivia + caballo | Estático |
| 1:15-1:30 | "Batalla de Tucapel..." | Animación de táctica militar | Animado |
```

### 4. Media Hunter Agent - Cazador de Recursos Multimedia  
**Archivo**: `.claude/agents/media-hunter.md`

**Responsabilidades:**
- Búsqueda automatizada en bancos de recursos libres
- Scraping de archivos históricos digitalizados
- Generación de prompts para IA generativa (imágenes)
- Validación de derechos de uso
- Catalogación y organización de recursos
- Generación de contenido faltante

**Fuentes de Recursos:**
- Pexels, Unsplash, Pixabay (landscapes, nature)
- Wikimedia Commons (historical images)
- Library of Congress (historical archives)  
- Prompts JSON para generación de contenido IA
- Archive.org (historical documents)

### 5. Voice Generator Agent - Generador de Voz
**Archivo**: `.claude/agents/voice-generator.md`

**Responsabilidades:**
- Generación de prompts JSON para texto-a-voz
- Generación de voces diferenciadas para cada locutor
- Control de velocidad, entonación y pausas
- Sincronización de diálogos
- Exportación en formato de alta calidad

**Configuración de Locutores:**
```
Locutor A (María - Narradora Principal):
- Voz: Femenina, profesional, cálida
- Velocidad: Normal
- Tono: Narrativo, envolvente

Locutor B (Carlos - Analista):  
- Voz: Masculina, conversacional, curiosa
- Velocidad: Ligeramente más lenta
- Tono: Analítico, reflexivo
```

### 6. Video Composer Agent - Compositor de Video
**Archivo**: `.claude/agents/video-composer.md`

**Responsabilidades:**
- Ensamblaje automatizado de clips según storyboard
- Sincronización precisa audio-visual
- Aplicación de transiciones suaves
- Generación de subtítulos automáticos
- Renderizado en múltiples formatos
- Optimización para diferentes plataformas

**Pipeline de Composición:**
1. Cargar audio base del podcast
2. Insertar clips visuales según timing
3. Aplicar transiciones predefinidas
4. Generar subtítulos sincronizados
5. Añadir intro/outro del canal
6. Renderizar en resoluciones múltiples

## Comandos Slash Personalizados

### /create-episode
**Archivo**: `.claude/commands/create-episode.md`

**Funcionalidad:**
Comando maestro que inicia todo el pipeline de producción

**Uso:**
```
/create-episode "Lautaro, el estratega mapuche" --serie "Mapuches" --canal "HistoriasDeAmerica"
```

**Frontmatter:**
```markdown
---
description: Crear un episodio completo de video histórico
argument-hint: "[título del episodio]" --serie "[nombre serie]" --canal "[canal destino]"
allowed-tools: Task, Bash, Read, Write, Glob, Grep
model: opus
---
```

### /validate-script
**Archivo**: `.claude/commands/validate-script.md`

**Funcionalidad:**
Validar guión para exactitud histórica y calidad narrativa

### /generate-thumbnail
**Archivo**: `.claude/commands/generate-thumbnail.md`

**Funcionalidad:**
Generar prompts JSON para thumbnails atractivos

## Output Styles Personalizados

### documentary-producer
**Archivo**: `output-styles/documentary-producer.md`

**Configuración:**
```markdown
---
name: documentary-producer
description: Modo especializado en producción de documentales históricos
---

Eres un productor especializado en documentales históricos educativos. Tu enfoque debe ser:

1. **Narrativa atractiva**: Transformar hechos en historias envolventes
2. **Precisión histórica**: Verificar todos los datos presentados
3. **Ritmo dinámico**: Mantener interés con variación de ritmo
4. **Conexión emocional**: Humanizar personajes históricos
5. **Valor educativo**: Enseñar mientras entretienes

Cuando trabajas en episodios:
- Inicia con un gancho poderoso
- Estructura en 3 actos narrativos
- Balancea información con emoción
- Termina con impacto duradero
```

## Hooks de Automatización

### Pre-Research Validation Hook
**Archivo**: `.claude/hooks/pre-research-validation.py`

**Propósito:**
Validar que el tema histórico es apropiado y factible antes de investigar

### Post-Media Processing Hook  
**Archivo**: `.claude/hooks/post-media-processing.py`

**Propósito:**
Procesar automáticamente recursos multimedia después de la descarga

### Quality Check Hook
**Archivo**: `.claude/hooks/quality-check.py`

**Propósito:**
Verificar calidad del contenido generado antes de finalizar

## Sistema de Prompts JSON

### Generación Automatizada de Prompts
El sistema genera archivos JSON estructurados con instrucciones detalladas para herramientas de IA:

### Tipos de Prompts Generados
- `voice_prompts.json`: Instrucciones para texto-a-voz
- `image_prompts.json`: Descripciones para generación de imágenes
- `video_prompts.json`: Instrucciones de edición de video
- `audio_prompts.json`: Música y efectos de sonido

## Estructura de Directorios

```
vidgenie/
├── .claude/
│   ├── agents/
│   │   ├── research-agent.md
│   │   ├── script-writer.md
│   │   ├── visual-planner.md
│   │   ├── media-hunter.md
│   │   ├── voice-generator.md
│   │   └── video-composer.md
│   ├── commands/
│   │   ├── create-episode.md
│   │   ├── validate-script.md
│   │   └── generate-thumbnail.md
│   ├── hooks/
│   │   ├── pre-research-validation.py
│   │   ├── post-media-processing.py
│   │   └── quality-check.py
│   └── settings.json
├── output-styles/
│   └── documentary-producer.md
├── templates/
│   ├── narrative-structures/
│   │   ├── hero-journey.md
│   │   ├── three-act.md
│   │   └── mystery-revelation.md
│   ├── visual-themes/
│   │   ├── ancient-civilizations.json
│   │   ├── medieval-period.json
│   │   └── colonial-era.json
│   └── voice-profiles/
│       ├── narrator-profiles.json
│       └── character-voices.json
├── assets/
│   ├── intro-templates/
│   ├── outro-templates/
│   ├── transition-effects/
│   └── background-music/
├── generated/
│   └── episodes/
│       ├── [canal]/
│       │   └── [serie]/
│       │       └── [episodio]/
│       │           ├── research.md
│       │           ├── script.md
│       │           ├── storyboard.json
│       │           ├── audio.wav
│       │           ├── video.mp4
│       │           └── metadata.json
└── utils/
    ├── ffmpeg-scripts/
    ├── quality-checkers/
    └── upload-automation/
```

## Plan de Implementación por Fases

### Fase 1: Base Foundation (Semana 1)
- [x] Crear plan detallado
- [ ] Configurar estructura de directorios
- [ ] Implementar research-agent básico
- [ ] Crear comando /create-episode inicial
- [ ] Implementar generación de prompts JSON

### Fase 2: Core Agents (Semana 2-3)
- [ ] Desarrollar script-writer con templates narrativos
- [ ] Implementar visual-planner con storyboard automation
- [ ] Crear media-hunter con búsqueda automatizada
- [ ] Integrar voice-generator con prompts JSON

### Fase 3: Integration & Automation (Semana 4)
- [ ] Desarrollar video-composer con ffmpeg
- [ ] Implementar hooks de validación y calidad
- [ ] Crear output-style documentary-producer
- [ ] Pipeline completo end-to-end

### Fase 4: Optimization & Scaling (Semana 5-6)
- [ ] Sistema de caché para recursos
- [ ] Procesamiento paralelo de tareas
- [ ] Control de calidad automatizado
- [ ] Métricas y analytics

### Fase 5: Advanced Features (Semana 7-8)
- [ ] Integración con YouTube API
- [ ] Generación automática de thumbnails
- [ ] Sistema de A/B testing para narrativas
- [ ] Dashboard de producción

## Flujo de Trabajo Típico

```
Usuario: /create-episode "Lautaro, el estratega mapuche" --serie "Mapuches" --canal "HistoriasDeAmerica"

1. research-agent ejecuta investigación profunda (5-10 min)
   └── Salida: research.md con datos verificados

2. script-writer transforma investigación en guión (3-5 min)
   └── Salida: script.md con diálogos sincronizados

3. visual-planner crea storyboard (2-3 min)
   └── Salida: storyboard.json con timing visual

4. media-hunter busca y descarga recursos (5-15 min)
   └── Salida: assets/ con imágenes y clips organizados

5. voice-generator produce audio del podcast (3-5 min)
   └── Salida: audio.wav con voces diferenciadas

6. video-composer ensambla video final (5-10 min)
   └── Salida: video.mp4 listo para upload

Total: 23-48 minutos para un episodio completo
```

## Métricas de Éxito

### Calidad del Contenido
- Precisión histórica: >95% de datos verificados
- Engagement narrativo: estructura en 3 actos completa
- Calidad técnica: audio/video sin errores

### Eficiencia de Producción
- Tiempo total: <60 minutos por episodio
- Intervención manual: <10% del proceso
- Tasa de éxito: >90% de episodios sin errores

### Escalabilidad
- Producción: 3-5 episodios por día
- Canales simultáneos: soporte para 5+ canales
- Series paralelas: 10+ series activas

## Casos de Uso Avanzados

### Multi-idioma
- Generar episodios en español, inglés, portugués
- Voice cloning para mantener consistencia entre idiomas
- Adaptación cultural específica por región

### Formatos Múltiples
- YouTube: 10-15 minutos, calidad 4K
- TikTok: 60-90 segundos, vertical
- Instagram: 60 segundos, cuadrado
- Podcast: solo audio, 20-30 minutos

### Personalización por Audiencia
- Nivel académico: básico, intermedio, avanzado
- Grupo etario: niños, adolescentes, adultos
- Intereses: militar, cultural, político, social

## Consideraciones de Seguridad y Ética

### Precisión Histórica
- Verificación cruzada de fuentes múltiples
- Identificación clara de controversias históricas
- Separación entre hechos documentados y teorías

### Derechos de Uso
- Validación automática de licencias de imágenes
- Generación de contenido original cuando sea necesario
- Atribución correcta de fuentes

### Sensibilidad Cultural
- Revisión de contenido por sensibilidades culturales
- Consulta con expertos en culturas específicas
- Respeto por perspectivas múltiples en eventos históricos

Este plan proporciona la base completa para implementar VidGenie como un sistema robusto, escalable y eficiente para la producción automatizada de contenido educativo histórico de alta calidad.