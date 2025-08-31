# MiniMax MCP Setup Guide

## Prerequisitos

1. **Cuenta MiniMax**: Obtener API key de [MiniMax Global](https://www.minimax.io/platform/user-center/basic-information/interface-key) o [MiniMax China](https://platform.minimaxi.com/user-center/basic-information/interface-key)
2. **uv**: Instalar gestor de paquetes Python con `curl -LsSf https://astral.sh/uv/install.sh | sh`
3. **Host Configuration**: Configurar el host correcto según región (Global: https://api.minimax.io | China: https://api.minimaxi.com)

## Instalación

### Método 1: Instalación Global uvx (Recomendado)
```bash
# No requiere instalación previa, uvx descarga automáticamente
uvx minimax-mcp -y
```

### Método 2: Instalación con uv
```bash
# Instalar uv si no está disponible
curl -LsSf https://astral.sh/uv/install.sh | sh
# Usar el servidor MiniMax MCP
uvx minimax-mcp -y
```

## Configuración

### 1. Variables de Entorno

Las variables se configuran directamente en `.claude/settings.json`:
```env
MINIMAX_API_KEY=insert-your-api-key-here
MINIMAX_MCP_BASE_PATH=local-output-dir-path
MINIMAX_API_HOST=https://api.minimax.io
MINIMAX_API_RESOURCE_MODE=local
```

### 2. Actualizar Settings.json

En `.claude/settings.json`, reemplazar placeholders:
```json
{
  "mcpServers": {
    "MiniMax": {
      "command": "uvx",
      "args": [
        "minimax-mcp",
        "-y"
      ],
      "env": {
        "MINIMAX_API_KEY": "insert-your-api-key-here",
        "MINIMAX_MCP_BASE_PATH": "local-output-dir-path, such as /User/xxx/Desktop",
        "MINIMAX_API_HOST": "api host, https://api.minimax.io | https://api.minimaxi.com",
        "MINIMAX_API_RESOURCE_MODE": "optional, [url|local], url is default, audio/image/video are downloaded locally or provided in URL format"
      }
    }
  }
}
```

## Verificación de Instalación

### Paso 1: Verificar Conexión MCP
```bash
# En Claude Code
/mcp
```
Deberías ver el servidor "MiniMax" listado y conectado.

### Paso 2: Listar Herramientas Disponibles
```bash
# En Claude Code
/mcp MiniMax tools
```

Herramientas esperadas:
- `text_to_audio` - Convert text to audio with a given voice
- `list_voices` - List all voices available
- `voice_clone` - Clone a voice using provided audio files
- `generate_video` - Generate a video from a prompt
- `text_to_image` - Generate a image from a prompt
- `query_video_generation` - Query the result of video generation task
- `music_generation` - Generate a music track from a prompt and lyrics
- `voice_design` - Generate a voice from a prompt using preview text

### Paso 3: Prueba Básica
```bash
# Generar audio de prueba
> Usa la herramienta de MiniMax para convertir "Hola mundo, esto es una prueba" a audio
```

## Modelos Disponibles

### Text-to-Speech
- `speech-01`: Voz natural, multipropósito
- `speech-01-240228`: Versión optimizada para narrativa
- `speech-01-turbo`: Versión rápida para pruebas

### Video Generation
- `video-01`: Generación de video estándar
- `video-01-live`: Tiempo real, menor calidad
- `MiniMax-Hailuo-02`: Modelo avanzado (julio 2025)

### Music Generation
- `music-1`: Generación musical básica
- `music-1.5`: Versión mejorada con mejor calidad

## Configuración para VidGenie

### Perfiles de Voz para Locutores

Crear archivo `templates/voice-profiles/narrator-profiles.json`:
```json
{
  "locutor_a_maria": {
    "name": "María",
    "role": "Narradora Principal",
    "voice_id": "female_voice_1",
    "characteristics": {
      "gender": "female",
      "age": "adult",
      "style": "professional",
      "emotion": "warm",
      "speed": 1.0,
      "pitch": 0.0
    },
    "sample_text": "Bienvenidos a Historias de América, donde exploramos los relatos más fascinantes de nuestro continente."
  },
  "locutor_b_carlos": {
    "name": "Carlos", 
    "role": "Analista",
    "voice_id": "male_voice_1",
    "characteristics": {
      "gender": "male",
      "age": "adult", 
      "style": "conversational",
      "emotion": "curious",
      "speed": 0.9,
      "pitch": -0.1
    },
    "sample_text": "Es increíble pensar cómo estos eventos del pasado siguen influyendo en nuestro presente."
  }
}
```

## Límites y Consideraciones

### Rate Limits
- Text-to-Audio: 100 requests/minute
- Video Generation: 10 requests/minute  
- Image Generation: 50 requests/minute

### Costos Aproximados (USD)
- Text-to-Audio: $0.001 per second
- Video Generation: $0.01 per second
- Image Generation: $0.005 per image

### Límites de Contenido
- Audio: Máximo 300 segundos por request
- Video: Máximo 60 segundos por request
- Texto: Máximo 2000 caracteres por request

## Troubleshooting

### Error: "API Key Invalid"
1. Verificar que la API key esté correcta en settings.json
2. Confirmar que no haya espacios extra al inicio/final
3. Verificar que la cuenta MiniMax esté activa

### Error: "Server Not Found" 
1. Verificar instalación de Node.js
2. Comprobar conexión a internet
3. Intentar reinstalación con `npm cache clean --force`

### Error: "Rate Limit Exceeded"
1. Implementar delays entre requests
2. Considerar upgrade del plan MiniMax
3. Usar versiones "turbo" para pruebas

### Audio No Se Genera
1. Verificar que el texto no contenga caracteres especiales
2. Confirmar que el idioma esté soportado (ES, EN, ZH)
3. Reducir longitud del texto si es muy extenso

## Integración con Otros Agentes

### Voice Generator Agent
```markdown
# En .claude/agents/voice-generator.md
tools: mcp__minimax__text_to_audio, mcp__minimax__voice_clone
```

### Media Hunter Agent
```markdown  
# En .claude/agents/media-hunter.md
tools: mcp__minimax__text_to_image, mcp__minimax__generate_video
```

## Backup Plan (Sin MiniMax)

Si MiniMax no está disponible, alternativas:
1. **ElevenLabs**: Para text-to-speech
2. **RunwayML**: Para generación de video
3. **DALL-E/Midjourney**: Para generación de imágenes
4. **Pexels/Unsplash**: Para recursos gratuitos

## Próximos Pasos

1. ✅ Configurar MiniMax MCP
2. ⏭️ Crear voice-generator agent
3. ⏭️ Desarrollar media-hunter agent  
4. ⏭️ Implementar video-composer agent
5. ⏭️ Testing end-to-end del pipeline

## Soporte

- **MiniMax Docs**: [https://docs.minimax.chat](https://docs.minimax.chat)
- **GitHub Issues**: [https://github.com/MiniMax-AI/MiniMax-MCP/issues](https://github.com/MiniMax-AI/MiniMax-MCP/issues)
- **Claude Code MCP**: [https://docs.anthropic.com/en/docs/claude-code/mcp](https://docs.anthropic.com/en/docs/claude-code/mcp)